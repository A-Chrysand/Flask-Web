from pathlib import Path


class WebDav_FileTree:
	tree_str = ''

	def print_tree(self):
		path = 'P:\Code\Dreamweaver_py\static\Media\img'
		self.generate_tree(Path(path), 0)
		result = self.tree_str
		self.filetreegc()
		return result

	def generate_tree(self, pathname, n=0):
		if pathname.is_file():
			self.tree_str += self.printFireTreeHTML('file', pathname, n)
		elif pathname.is_dir():
			self.tree_str += self.printFireTreeHTML(
			    'dir', str(pathname.relative_to(pathname.parent)), n)
			for cp in pathname.iterdir():
				self.generate_tree(cp, n + 1)

	def printFireTreeHTML(self, para, filename, n):
		if para == 'file':
			str_filedir = cutstring(str(filename.parent), '\\', 4)
			str_filedir = str(str_filedir[4]).replace("\\", "/")
			str_filedir += '/'
			str_filename = str(filename.name)
			return '<p class=webdav_file style="padding-left:' + str(
			    n * 2
			) + 'em"><span>文件</span><a target="_blank" href="static/' + str_filedir + str_filename + '">' + str_filename + '</a></p>'
		elif para == 'dir':
			return '<p class=webdav_dir style="padding-left:' + str(
			    n * 2) + 'em"><span>目录</span>' + filename + '\\</p>'

	def filetreegc(self):
		self.tree_str = ""


def cutstring(operation_string, splicechar=";", para_num_of_splicechar=0):
	try:
		operation_string.index(splicechar)  # 检测operation_string里是否含有切割标记字符
	except ValueError:
		print("切割的字符串不含切割标记字符")
		return
	temp = []
	if para_num_of_splicechar:
		num_of_splicechar = para_num_of_splicechar
	else:
		num_of_splicechar = operation_string.count(splicechar)
	# 如果num_of_splicechar设置错误，那么会导致最后一个splicechar之后为一整块(分割不完全)
	for i in range(num_of_splicechar + 1):
		if i != num_of_splicechar:
			temp.append(operation_string[:operation_string.index(splicechar)]
			            )  # 切割从开头到分割标记字符之前的字符串并push到列表中
			operation_string = operation_string.lstrip(
			    temp[i])  # 从左向右删除刚刚切割掉的字符
			operation_string = operation_string.lstrip(
			    splicechar)  # 从左向右删除标记字符
		else:
			temp.append(operation_string)
			break
	return temp
