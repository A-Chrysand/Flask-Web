from pathlib import Path


class WebDav_FileTree:
	tree_str = ''

	def generate_tree(self, pathname, n=0):
		if pathname.is_file():
			self.tree_str += self.makeHTML('file', pathname.name, n)
		elif pathname.is_dir():
			self.tree_str += self.makeHTML('dir', str(pathname.relative_to(pathname.parent)), n)
			for cp in pathname.iterdir():
				self.generate_tree(cp, n + 1)

	def makeHTML(self, para, filename, n):
		if para == 'file':
			# return '    |' * n + '-' * 4 + filename + '\n'
			return '<p class=webdav_file style="padding-left:' + str(n * 2) + 'em"><span>文件</span>' + filename + '</p>'
		elif para == 'dir':
			# return '    |' * n + '-' * 4 + filename + '\\' + '\n'
			return '<p class=webdav_dir style="padding-left:' + str(n * 2) + 'em"><span>目录</span>' + filename + '\\</p>'

	def print_tree(self):
		path = 'E:\Code\HTML\Dreamweaver\py_functions'
		self.generate_tree(Path(path), 0)
		result = self.tree_str
		self.filetreegc()
		return result

	def filetreegc(self):
		self.tree_str = ""


'''
	def makeTree(self, para, filename, n):
		if para == 'file':
			return '    |' * n + '-' * 4 + filename + '\n'
		elif para == 'dir':
			return '    |' * n + '-' * 4 + filename + '\\' + '\n'
'''
