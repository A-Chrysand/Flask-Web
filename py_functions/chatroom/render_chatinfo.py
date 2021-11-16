import os
import sqlite3

class RenderChatInfo:
	__dbname = 'accountdb.db'  # 设置数据库名称
	dbpath = os.path.join((os.path.dirname(os.path.realpath(__file__)))[0:-21], 'db', __dbname)  # 获取本py文件的绝对路径，再删掉路径返回上2级
	def db_getChatList(self):
		accountdb = sqlite3.connect(self.dbpath)  # 创建数据库对象
		acc_db_cur = accountdb.cursor()  # 创建数据库指针
		acc_db_cur.execute("SELECT * FROM chatinfo")  # 执行数据库操作
		db_result = acc_db_cur.fetchall()  # 把查找结果赋值给db_result
		print(db_result)
		acc_db_cur.close()
		if len(db_result) == 0:  # 当结果列表长度为0（找不到用户）时返回0
			return 0
		else:
			return self.RenderJSON(db_result)

	@staticmethod
	def RenderJSON(db_obj):
		print(db_obj)
		pass