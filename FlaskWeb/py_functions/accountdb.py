import sqlite3
import os

project_root = (os.path.dirname(os.path.realpath(__file__)))[0:-12]  # 获取本py文件的绝对路径，再删掉路径返回上一级


class AccountDB:
	accountdb = sqlite3.connect(os.path.join(project_root, 'db', 'accountdb.db'))
	acc_db_cur = accountdb.cursor()

	def search(self, string_object):
		self.acc_db_cur.execute("\
			SELECT Uname,Upasswd FROM user1 WHERE Uname=\"" + string_object[0] + "\"")

		db_result = self.acc_db_cur.fetchall()
		# print("indb:" + str(len(db_result)) + ">", end="")
		# print(db_result)
		if len(db_result) == 0:
			print('>>>dbcheck false(User Notfound)', end="")
			return False
		else:
			if len(db_result) > 1:
				print('>>>dbcheck false(too many item)', end="")
				return False
			elif len(db_result) == 1:
				# tar =
				# print(tar)
				if (db_result[0])[1] != string_object[1]:
					print('>>>password incorrect', end="")
					return False
				else:
					print('>>>dbcheck success', end="")
					return True

# elif (len((self.acc_db_cur.fetchall())[0]) > 2):

# else:
#	print(self.acc_db_cur.fetchall()[0])
##	tar = '1'
#	if tar != string_object[1]:
##		return False
#	else:
#		print('>>>dbcheck success', end="")
#		return True
