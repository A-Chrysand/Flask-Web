import sqlite3
import os
import random


class AccountDB:
	__dbname = 'accountdb.db'  # 设置数据库名称
	dbpath = os.path.join((os.path.dirname(os.path.realpath(__file__)))[0:-21],
	                      'db', __dbname)  # 获取本py文件的绝对路径，再删掉路径返回上2级

	def login_search(self, string_object):
		accountdb = sqlite3.connect(self.dbpath)  # 创建数据库对象
		acc_db_cur = accountdb.cursor()  # 创建数据库指针
		'''''' '''''' '''''' '''''' '''''' '''''' '''''' '''''' '''''' '''''' ''
		if '@' in string_object[0]:  # 判断提交的字符串是否含有@号(邮箱)
			acc_db_cur.execute("\
				SELECT Umail,Upasswd FROM user1 WHERE Umail=\"" + string_object[0] +
			                   "\"")  # 执行数据库操作
		else:
			acc_db_cur.execute("\
				SELECT Uname,Upasswd FROM user1 WHERE Uname=\"" + string_object[0] +
			                   "\"")  # 执行数据库操作
		db_result = acc_db_cur.fetchall()  # 把查找结果赋值给db_result
		acc_db_cur.close()
		if len(db_result) == 0:  # 当结果列表长度为0（找不到用户）时返回0
			return 0
		else:
			if len(db_result) > 1:  # 当结果列表长度>1（重复用户）时返回2
				return 2
			elif len(db_result) == 1:  # 当结果列表长度为1时继续判断密码
				if (db_result[0])[1] != string_object[1]:  # 判断密码是否一致
					return 1
				else:  # 密码错误返回10
					return 10

	def register_search(self, string_object):
		accountdb = sqlite3.connect(self.dbpath)  # 创建数据库对象
		acc_db_cur = accountdb.cursor()  # 创建数据库指针
		'''''' '''''' '''''' '''''' '''''' '''''' '''''' '''''' '''''' '''''' ''
		# 密码长度的查找交给最初的register_check()了，但是数据库库内也定义了check()
		acc_db_cur.execute("\
			SELECT Uname,Umail FROM user1 WHERE Uname=\"" + string_object[0] +
		                   "\"")  # 执行数据库操作查找账号
		db_result = acc_db_cur.fetchall()  # 把查找结果赋值给db_result
		db_result_bool = [False, False]  # 若可以注册的条件定位True
		if len(db_result) == 0:  # 当结果列表长度为0（找不到用户，可以注册）
			db_result_bool[0] = True
		else:  # 当结果列表长度不为0（用户名已被其他用户使用，不可以注册）
			db_result_bool[0] = False
		acc_db_cur.execute("\
					SELECT Uname,Umail FROM user1 WHERE Umail=\"" + string_object[1] +
		                   "\"")  # 执行数据库操作查找邮箱
		db_result = acc_db_cur.fetchall()  # 把查找结果赋值给db_result
		acc_db_cur.close()
		if len(db_result) == 0:  # 当结果列表长度为0（找不到用户，可以注册）
			db_result_bool[1] = True
		else:  # 当结果列表长度不为0（邮箱已被其他账户使用，不可以注册）
			db_result_bool[1] = False
		return db_result_bool

	def register_write(self, write_str_object):
		accountdb = sqlite3.connect(self.dbpath)  # 创建数据库对象
		acc_db_cur = accountdb.cursor()  # 创建数据库指针
		'''''' '''''' '''''' '''''' '''''' '''''' '''''' '''''' '''''' '''''' ''
		acc_db_cur.execute("select count(UID) from user1")  # 执行数据库操作，查询数量
		db_tuple_num = str((acc_db_cur.fetchall()[0])[0] + 1).zfill(
		    4)  # 把查找结果前面补0后赋值给db_result
		print("\033[0;37m|ID|\033[0m" + db_tuple_num +
		      "\033[0;37m|Name|\033[0;m" + write_str_object[0] +
		      "\033[0;37m|Email|\033[0m" + write_str_object[2],
		      end=">>>")
		Usynthnum = random.randrange(1000, 9999, 1)
		acc_db_cur.execute(
		    'INSERT INTO user1(UID,Uright,Uname,Upasswd,Umail,Usynthtext) VALUES("'
		    + db_tuple_num + '",1,"' + write_str_object[0] + '","' +
		    write_str_object[1] + '","' + write_str_object[2] + '","' +
		    str(Usynthnum) + '")')
		accountdb.commit()
		temp = self.register_search([write_str_object[0], write_str_object[2]])
		acc_db_cur.close()
		if (temp[0] and temp[1]):
			print('\033[0;31m' + 'Failed' + '\033[0m')
			return 'registerfail'  # 当两个都是True,即表示用户名和邮箱都可再注册，返回registerfail，注册失败
		elif (not (temp[0]) and not (temp[1])):
			print('\033[0;32m' + 'Success' + '\033[0m')
			return 'registersuccess'  # 当两个都是False,即表示用户名和邮箱都不可再注册，返回registersuccess，注册成功
		else:
			print('\033[0;31m' + 'Failed' + '\033[0m')
			return 'registererror'

	def db_getbasicinfo(self, username):
		accountdb = sqlite3.connect(self.dbpath)  # 创建数据库对象
		acc_db_cur = accountdb.cursor()  # 创建数据库指针
		'''''' '''''' '''''' '''''' '''''' '''''' '''''' '''''' '''''' '''''' ''
		acc_db_cur.execute("\
				SELECT Uname,Umail,Uxuehao FROM user1 WHERE Uname=\"" + username +
		                   "\"")  # 执行数据库操作
		db_result = acc_db_cur.fetchall()  # 把查找结果赋值给db_result
		temp_dict = {'Uname': db_result[0][0],\
           'Umail': db_result[0][1],\
           'Uxuehao': db_result[0][2]}
		acc_db_cur.close()
		return temp_dict
