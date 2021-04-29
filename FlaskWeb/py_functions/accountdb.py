import sqlite3
import os

project_root = (os.path.dirname(os.path.realpath(__file__)))[0:-12]  # 获取本py文件的绝对路径，再删掉路径返回上一级


class AccountDB:
	accountdb = sqlite3.connect(os.path.join(project_root, 'db', 'accountdb.db'))  # 创建数据库对象
	acc_db_cur = accountdb.cursor()  # 创建数据库指针

	def login_search(self, string_object):
		self.acc_db_cur.execute("\
			SELECT Uname,Upasswd FROM user1 WHERE Uname=\"" + string_object[0] + "\"")  # 执行数据库操作
		db_result = self.acc_db_cur.fetchall()  # 把查找结果赋值给db_result
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
		self.acc_db_cur.execute("\
			SELECT Uname,Umail FROM user1 WHERE Uname=\"" + string_object[0] + "\"")  # 执行数据库操作查找账号
		db_result = self.acc_db_cur.fetchall()  # 把查找结果赋值给db_result
		db_result_bool = [False, False]  # 若可以注册的条件定位True
		if len(db_result) == 0:  # 当结果列表长度为0（找不到用户，可以注册）
			db_result_bool[0] = True
		else:  # 当结果列表长度不为0（用户名已被其他用户使用，不可以注册）
			db_result_bool[0] = False
		self.acc_db_cur.execute("\
					SELECT Uname,Umail FROM user1 WHERE Umail=\"" + string_object[1] + "\"")  # 执行数据库操作查找邮箱
		db_result = self.acc_db_cur.fetchall()  # 把查找结果赋值给db_result
		if len(db_result) == 0:  # 当结果列表长度为0（找不到用户，可以注册）
			db_result_bool[1] = True
		else:  # 当结果列表长度不为0（邮箱已被其他账户使用，不可以注册）
			db_result_bool[1] = False
		return db_result_bool

	def register_write(self, write_str_object):
		self.acc_db_cur.execute("select count(UID) from user1")  # 执行数据库操作，查询数量
		db_tuple_num = str((self.acc_db_cur.fetchall()[0])[0] + 1).zfill(4)  # 把查找结果前面补0后赋值给db_result
		print("\033[0;37m|ID|\033[0m" + db_tuple_num + "\033[0;37m|Name|\033[0;m" + write_str_object[
			0] + "\033[0;37m|Email|\033[0m" + write_str_object[2], end=">>>")
		self.acc_db_cur.execute(
			'INSERT INTO user1(UID,Uright,Uname,Upasswd,Umail) VALUES("' + db_tuple_num + '",1,"' + write_str_object[
				0] + '","' + write_str_object[1] + '","' + write_str_object[2] + '")')
		self.accountdb.commit()
		temp = self.register_search([write_str_object[0], write_str_object[2]])
		if (temp[0] and temp[1]):
			print('\033[0;31m' + 'Failed' + '\033[0m')
			return 'registerfail'  # 当两个都是True,即表示用户名和邮箱都可再注册，返回0，注册失败
		elif (not (temp[0]) and not (temp[1])):
			print('\033[0;32m' + 'Success' + '\033[0m')
			return 'registersuccess'  # 当两个都是False,即表示用户名和邮箱都不可再注册，返回1，注册成功
		else:
			print('\033[0;31m' + 'Failed' + '\033[0m')
			return 'registererror'
