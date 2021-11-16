from py_functions.account.account_decipher import Decipher
import sqlite3
import os


class AccountChange:
	__dbname = 'accountdb.db'  # 设置数据库名称
	dbpath = os.path.join((os.path.dirname(os.path.realpath(__file__)))[0:-21], 'db',
	                      __dbname)  # 获取本py文件的绝对路径，再删掉路径返回上2级

	def BasicInfoChange(self, ciphertext):
		obj_Deciher = Decipher()
		list_decoded = obj_Deciher.process_num(ciphertext)
		# todo 输入合法性检查
		accountdb = sqlite3.connect(self.dbpath)  # 创建数据库对象
		acc_db_cur = accountdb.cursor()  # 创建数据库指针
		''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
		strname = 'UPDATE user1 SET Uname="' + list_decoded[0] + '", Umail="' + list_decoded[1] + '", Uphone="' + \
		          list_decoded[2] + '", Uxuehao="' + list_decoded[3] + '" WHERE Uname=="' + list_decoded[0] + '"'
		acc_db_cur.execute(strname)
		accountdb.commit()
		# temp = self.register_search([write_str_object[0], write_str_object[2]])
		acc_db_cur.close()
		return 'success'

	def SecretInfoChange(self, ciphertext):
		obj_Deciher = Decipher()
		list_decoded = obj_Deciher.process_num(ciphertext)
		# todo 输入合法性检查
		accountdb = sqlite3.connect(self.dbpath)  # 创建数据库对象
		acc_db_cur = accountdb.cursor()  # 创建数据库指针
		''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
		strname = 'UPDATE user1 SET Upasswd="' + list_decoded[1] + '" WHERE Uname=="' + list_decoded[0] + '"'
		acc_db_cur.execute(strname)
		accountdb.commit()
		# temp = self.register_search([write_str_object[0], write_str_object[2]])
		acc_db_cur.close()
		return 'success'
