import sqlite3
import os


class Announcement:
	__dbname = 'accountdb.db'  # 设置数据库名称
	tablename = 'announcement'  # 设置需要的表的名称
	dbpath = os.path.join((os.path.dirname(os.path.realpath(__file__)))[0:-(12 + 1 + 12)], 'db',
	                      __dbname)  # 获取本py文件的绝对路径，再删掉路径返回上一级

	def getAnnouncement(self, SearchString=None):
		announcementdb = sqlite3.connect(self.dbpath)  # 创建数据库对象
		ann_db_cur = announcementdb.cursor()  # 创建数据库指针
		if SearchString == None:
			ann_db_cur.execute('SELECT * FROM ' + self.tablename)  # 执行数据库操作
		else:
			ann_db_cur.execute('SELECT * FROM ' + self.tablename + ' WHERE ID="' + SearchString + '"')  # 执行数据库操作
		db_result = ann_db_cur.fetchall()  # 把查找结果赋值给db_result
		ann_db_cur.close()
		if len(db_result) == 0:
			return '未找到信息'
		else:
			return db_result

	def printAnnouncementHTML(self):
		result_obj = self.getAnnouncement()
		'''
		strings = '<tr>\
			<td class="announcement_ID">公告编号</td>\
			<td class="announcement_title">公告标题</td>\
			<td class="announcement_author">作者</td>\
			<td class="announcement_time">时间</td>\
		</tr>'
		'''
		strings = ''
		for i in range(len(result_obj)):
			strings += '\
		<tr>\
			<td class="announcement_ID">' + result_obj[i][0] + '</td>\
			<td class="announcement_title"><a class="announcement_link" target="_blank" onclick=AnnouncementPage("' + \
			           result_obj[i][0] + '")>' + result_obj[i][3] + '</span></td>\
			<td class="announcement_author">' + result_obj[i][2] + '</td>\
			<td class="announcement_time">' + result_obj[i][1] + '</td>\
		</tr>'
		return strings
