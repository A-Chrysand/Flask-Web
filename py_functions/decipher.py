import re
import time
from datetime import datetime
import math
from py_functions.accountdb import AccountDB


class Decipher:
	Spliced_Encoded_Float = []  # 定义全局存储变量，存储浮点式
	Spliced_Encoded_Int = []  # 定义全局存储变量，存储整形
	Jingdu = 2

	def pre_process(self, encoded_str):
		spliced_encoded_str = (re.findall(self.Jingdu * '.' + '...?', encoded_str))  # 分割字符串，储存到字符串列表里
		# print("切割后的字符串>", end="")
		# print(spliced_encoded_str)
		j = 0  # 定义索引
		for i in spliced_encoded_str:
			list1 = list(spliced_encoded_str[j])  # 列表里的单个字符串转列表
			list1.insert(3, '.')  # 往字符串列表中添加小数点
			self.Spliced_Encoded_Float.append(float(''.join(list1)))  # 字符串列表转浮点
			j += 1

	# print("OrgFloat>")
	# print(self.Spliced_Encoded_Float)

	def post_process(self):
		j = 0
		res = ""  # 定义解密结果字符串存储变量
		temp = []  # 定义切分结果列表存储变量
		for i in self.Spliced_Encoded_Int:
			res += chr(self.Spliced_Encoded_Int[j])  # 整形ASCII码转字符
			j += 1
		num_of_v = res.count('/')
		# print("解码结果(" + str(num_of_v) + '/)>' + res)
		for i in range(num_of_v + 1):
			if i != num_of_v:
				temp.append(res[:res.index('/')])
				res = res.lstrip(temp[i])  # 删除字符串前第i次切的
				res = res.lstrip('/')  # 删除切掉后遗留的'/' #若与上面一起切的话，如果遇到账号=密码，那么会把相同的都切掉
			else:
				temp.append(res)
				break
		return temp

	def process_num(self, encoded_str):
		self.pre_process(encoded_str)
		pi = (
			3, 6, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 6, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8,
			8, 4, 1, 9)  # 9796<-？？？
		pi = pi + pi
		j = 0
		for i in self.Spliced_Encoded_Float:
			self.Spliced_Encoded_Float[j] -= pi[j]
			self.Spliced_Encoded_Float[j] /= 2.236
			self.Spliced_Encoded_Float[j] += int(time.strftime("%M"))  # 获取提交时间(分钟)
			self.Spliced_Encoded_Float[j] -= 233  # 减去offset
			self.Spliced_Encoded_Float[j] -= math.pow(int(datetime.now().isoweekday() + 1), 2)  # 获取++星期的平方
			self.Spliced_Encoded_Float[j] -= pi[j]
			self.Spliced_Encoded_Int.append(int(round(self.Spliced_Encoded_Float[j], 1)))
			j += 1
		result_strs = self.post_process()  # 这个result_strs是列表[]
		self.reset_variable()  # 执行变量重置
		return result_strs

	def login_check(self, check_str):
		temp = self.process_num(check_str)  # temp是列表[]
		db_login_check = AccountDB()
		dbreturn = db_login_check.login_search(temp)
		if dbreturn == 0:
			print('>>>' + '\033[0;33m' + 'dbcheck false' + '\033[0m', end="")
			print('\033[0;36m' + '(User NotFound)' + '\033[0m', end="")
			return 'usernotfound'
		elif dbreturn == 1:
			print('>>>' + '\033[0;33m' + 'password incorrect' + '\033[0m', end="")
			return 'passwderr'
		elif dbreturn == 2:
			print('>>>' + '\033[0;33m' + 'dbcheck false' + '\033[0m', end="")
			print('>>>' + '\033[1;31;40m' + 'dbcheck false(too many item)' + '\033[0m', end="")
			return 'toomany'
		elif dbreturn == 10:
			print('>>>' + '\033[0;32m' + 'dbcheck success' + '\033[0m', end="")
			return 'success'

	def register_check(self, check_str_object):
		temp = self.process_num(check_str_object)
		if len(temp[1]) < 6:
			print('\033[0;31m' + 'invailed password length!!!' + '\033[0m')
			return "passwdlengtherr"
		temp_accpsw = [temp[0], temp[2]]
		registercheck = AccountDB()
		dbreturn = registercheck.register_search(temp_accpsw)
		if (dbreturn[0] and dbreturn[1]):
			return registercheck.register_write(temp)
		elif (dbreturn[0] == False):
			print("User Registed")
			return 'userregisted'
		elif (dbreturn[1] == False):
			print("Email Registed")
			return 'mailregisted'

	def reset_variable(self):
		self.Spliced_Encoded_Float.clear()  # 清除全局存储变量
		self.Spliced_Encoded_Int.clear()  # 清除全局存储变量

# st = Decipher()
# st.post_process()
