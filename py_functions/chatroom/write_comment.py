import sqlite3
import os
import time


class WriteComment:
	__dbname = 'accountdb.db'  # 设置数据库名称
	dbpath = os.path.join((os.path.dirname(os.path.realpath(__file__)))[0:-21], 'db', __dbname)

	# 获取本py文件的绝对路径，再删掉路径返回上2级

	def write_comment(self, str_username, str_text):
		str_now = time.strftime("%Y%m%d%H%M%S")

		obj_db = sqlite3.connect(self.dbpath)  # 创建数据库对象
		db_cursor = obj_db.cursor()  # 创建数据库指针
		#db_cursor.execute("select count(id) from chatinfo")  # 执行数据库操作，查询数量
		#id = str((db_cursor.fetchall()[0])[0] + 1)

		db_cursor.execute(
			'INSERT INTO chatinfo(uname,time,info) VALUES("' + str_username + '", "' + str_now + '", "' + str_text + '")')
		#db_cursor.execute("select count(id) from chatinfo")  # 执行数据库操作，查询数量
		#id2 = str((db_cursor.fetchall()[0])[0])
		obj_db.commit()
		db_cursor.close()
		#if id == id2:
		return "Submit Successful"

