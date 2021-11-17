import os
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from py_functions.account.account_check import account_check
from py_functions.WebDav.webdav_filetree import WebDav_FileTree
from py_functions.Announcement.announcement_list import Announcement
from py_functions.Announcement.urldecode import UrlDecode
from py_functions.chatroom.render_chatinfo import RenderChatInfo
from py_functions.chatroom.write_comment import WriteComment
from py_functions.account.account_userdb import AccountDB
from py_functions.account.account_change import AccountChange

app = Flask(__name__, template_folder='templates', static_folder='static')
'''
TODO 数据库锁库问题，
TODO 前后端中文字符串传输问题(及数据库中文支持问题)
'''


################################################################################


@app.route('/')
def index():
	# todo ↓↓↓此处根据EleWdith * HWR得到高度的算法有BUG
	return render_template('index.html',
	                       # 'account/login.html'
	                       # './account/usercenter.html'
	                       )


########################################ACCOUNT########################################
@app.route("/login")
def login():
	return render_template('./account/login.html')


@app.route("/login_js_post/<login_getdata>", methods=['POST'])
def login_js_post(login_getdata):
	print('\tPOST from>>>' + request.remote_addr, end="")
	logincheck_result = account_check.login_check(login_getdata)
	if logincheck_result == 'success':
		print("->" + '\033[0;32m' + "login success" + '\033[0m' + "||src=" +
		      login_getdata)
		return logincheck_result
	else:
		print("->" + '\033[0;34m' + "login failed" + '\033[0m' + "||src=" +
		      login_getdata)
		return logincheck_result


@app.route("/register_js_post/<RegisterCheck_getdata>", methods=['POST'])
def register_js_post(RegisterCheck_getdata):
	print('\tRegistering>>>' + request.remote_addr + ">>>", end="")
	registercheck_result = account_check.register_check(RegisterCheck_getdata)
	return registercheck_result


# return "注册已禁止"


@app.route("/usercenter/<username>")
def usercenter(username):
	return render_template('./account/usercenter.html',
	                       file_currentuser=username)


@app.route("/usercenter/js_post_basicinfo")
def usercenter_basic_info_page():
	return render_template('./account/usercenter_fn/basicinfo.html')


@app.route("/usercenter/js_post_basicinfo/getbasicinfo/<username>",
           methods=['POST'])
def usercenter_get_basic_info(username):
	logincheck_result = AccountDB()
	return logincheck_result.db_getbasicinfo(username)


@app.route("/submit_BaisicInfoChange_js_post/<Bencodedtext>", methods=['POST'])
def submit_BaisicInfoChange_js_post(Bencodedtext):
	obj_accc = AccountChange()
	return obj_accc.BasicInfoChange(Bencodedtext)


@app.route('/sbumit_Userimg_form_post/<username>',
           methods=['POST'],
           strict_slashes=False)
def api_upload(username):
	def allowed_file(filename):
		ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG'])  # 允许上传的文件后缀
		return '.' in filename and filename.rsplit('.',
		                                           1)[1] in ALLOWED_EXTENSIONS

	UPLOAD_FOLDER = '\\static\\Media\\img\\user\\icon\\'
	basedir = os.path.abspath(os.path.dirname(__file__))  # 获取当前项目的绝对路径
	file_dir = basedir + UPLOAD_FOLDER

	incoming_file = request.files['myfile']  # 从表单的file字段获取文件，myfile为该表单的name值
	if incoming_file and allowed_file(
			incoming_file.filename):  # 判断是否是允许上传的文件类型
		# fname = incoming_file.filename
		# ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
		ext = 'ico'
		new_filename = str(username) + '.' + ext  # 修改文件名
		incoming_file.save(os.path.join(file_dir,
		                                new_filename))  # 保存文件到upload目录
		return render_template(
			'./alertwindows/redirectToHome.html',
			message="修改成功",
			tusername=username,
		)
	else:
		return render_template(
			'./alertwindows/redirectToHome.html',
			message="修改失败",
			tusername=username,
		)


@app.route("/submit_SecretInfoChange_js_post/<Sencodedtext>", methods=['POST'])
def submit_SecretInfoChange_js_post(Sencodedtext):
	obj_accc = AccountChange()
	return obj_accc.SecretInfoChange(Sencodedtext)


@app.route("/usercenter/js_post_secretinfo")
def usercenter_secretinfo():
	return render_template('./account/usercenter_fn/secretinfo.html')


@app.route("/usercenter/js_post_setting")
def usercenter_setting():
	return render_template('./account/usercenter_fn/setting.html')


@app.route("/usercenter/js_post_diss")
def usercenter_diss():
	return render_template('./account/usercenter_fn/diss.html')


@app.route("/source/usericon/<username>")
def register_js_2post(username):
	return 'df'


########################################HOME INDEX########################################
@app.route('/home')
def home():
	i = request.args['i']
	if (i == None):
		i = 0
	return render_template('/apps/home.html', OnloadScriptString=i)


####################
@app.route('/home/banner')
def banner():
	return render_template('apps/01_banner.html')


@app.route("/announcementlist_js_post/", methods=['POST'])
def announcementlist_js_post():
	obj_announcement = Announcement()
	announcementResult = obj_announcement.printAnnouncementHTML()
	return announcementResult


@app.route("/home/announcement/<string>", methods=['POST', 'GET'])
def announcementinfo(string):
	result = UrlDecode.Decode(string)
	obj_announcement = Announcement()
	announcementResult = obj_announcement.getAnnouncement(result[0])
	if result[1] != 'null':
		return render_template('/apps/sub_apps/11_announcement.html',
		                       username=result[1],
		                       ID=announcementResult[0][0],
		                       title=announcementResult[0][3],
		                       time=announcementResult[0][1],
		                       author=announcementResult[0][2],
		                       text=announcementResult[0][4])
	else:
		return '请先登录<br>Please Login'


####################
@app.route('/home/SmallStore')
def smallstore():
	return render_template('apps/02_SmallStore.html')


@app.route('/home/SmallStore/chatlist', methods=["GET"])
def chatlisti():
	temp_obj = RenderChatInfo()
	return temp_obj.db_getChatList()


@app.route('/JSPOST/submitComment/<username>/<text>', methods=["POST"])
def JSPOST_comments(username, text):
	temp_obj = WriteComment()
	return temp_obj.write_comment(username, text)


####################
@app.route('/home/Busstation')
def Busstation():
	return render_template('apps/03_Busstation.html')


@app.route("/filetree_js_post/", methods=['POST'])
def filetree_js_post():
	print('\tGettingFileTree>>>' + request.remote_addr)
	Obj_WebDav_FileTree = WebDav_FileTree()
	filetree_result = Obj_WebDav_FileTree.print_tree()
	return filetree_result


####################


@app.route('/home/Wolserver')
def wolserver():
	return render_template('apps/04_Wolserver.html')


@app.route('/home/report')
def report():
	return render_template('apps/05_report.html')


################################################################################
if __name__ == '__main__':
	# app.run()
	# 如果你想实际开服，请使用下面那条
	app.run(host='0.0.0.0', port=5000)
