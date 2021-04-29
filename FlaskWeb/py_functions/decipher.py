import re
import time
from datetime import datetime
import math
from FlaskWeb.py_functions.accountdb import AccountDB


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
		res = ""  # 定义结果存储变量
		for i in self.Spliced_Encoded_Int:
			res += chr(self.Spliced_Encoded_Int[j])  # 整形ASCII码转字符
			j += 1
		cut_account = res[:res.index('/')]
		cut_passwd = res[res.index('/'):].lstrip('/')
		return [cut_account, cut_passwd]

	def process_num(self, encoded_str):
		self.pre_process(encoded_str)
		pi = (
			3, 6, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 6, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8,
			8, 4, 1, 9)  # 9796<-？？？
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
		# print("计算结果"+self.Spliced_Encoded_Float, end="->")
		result_str = self.post_process()
		# print("明文>", end="")
		# print(result_str)
		self.reset_variable()  # 执行变量重置
		return self.check_in(result_str)

	def check_in(slef, result_str):
		db_check = AccountDB()
		return db_check.search(result_str)

	def reset_variable(self):
		self.Spliced_Encoded_Float.clear()  # 清除全局存储变量
		self.Spliced_Encoded_Int.clear()  # 清除全局存储变量

# ste = Decipher()
# ste.process_num("9779087357949069878434982")
