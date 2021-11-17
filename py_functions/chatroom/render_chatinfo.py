import json
import os
import sqlite3
#todo 你总不能一直开关数据库吧？用内存缓存
class RenderChatInfo:
	__dbname = 'accountdb.db'  # 设置数据库名称
	dbpath = os.path.join((os.path.dirname(os.path.realpath(__file__)))[0:-21], 'db', __dbname)  # 获取本py文件的绝对路径，再删掉路径返回上2级
	def db_getChatList(self):
		accountdb = sqlite3.connect(self.dbpath)  # 创建数据库对象
		acc_db_cur = accountdb.cursor()  # 创建数据库指针
		acc_db_cur.execute("SELECT * FROM chatinfo")  # 执行数据库操作
		db_result = acc_db_cur.fetchall()  # 把查找结果赋值给db_result
		acc_db_cur.close()
		if len(db_result) == 0:  # 当结果列表长度为0（找不到用户）时返回0
			return 0
		else:
			return self.RenderJSON(db_result)

	@staticmethod
	def RenderJSON(db_obj):

		temp_dictList=[]
		for i in range(0,len(db_obj)):
			temp_dict = {}
			temp_dict["id"] = db_obj[i][0]
			temp_dict["username"] = db_obj[i][1]
			temp_dict["time"] = db_obj[i][2]
			temp_dict["text"] = db_obj[i][3]
			temp_dictList.append(temp_dict)
		return json.dumps(temp_dictList)