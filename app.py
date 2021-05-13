from flask import Flask
from flask import render_template
from flask import request
from py_functions.account_check import account_check

app = Flask(__name__, template_folder='templates', static_folder='static')


################################################################################

@app.route('/')
def index():
	# todo ↓↓↓此处根据EleWdith * HWR得到高度的算法有BUG
	return render_template(
		'index.html',
	)


########################################ACCOUNT########################################
@app.route("/login")
def login():
	return render_template(
		'./account/login.html'
	)


@app.route("/login_js_post/<login_getdata>", methods=['POST'])
def login_js_post(login_getdata):
	print('\tPOST from>>>' + request.remote_addr, end="")
	logincheck_result = account_check.login_check(login_getdata)
	if logincheck_result == 'success':
		print("->" + '\033[0;32m' + "login success" + '\033[0m' + "||src=" + login_getdata)
		return logincheck_result
	else:
		print("->" + '\033[0;34m' + "login failed" + '\033[0m' + "||src=" + login_getdata)
		return logincheck_result


@app.route("/register_js_post/<RegisterCheck_getdata>", methods=['POST'])
def register_js_post(RegisterCheck_getdata):
	print('\tRegistering>>>' + request.remote_addr + ">>>", end="")
	registercheck_result = account_check.register_check(RegisterCheck_getdata)
	return registercheck_result


@app.route("/usercenter")
def usercenter():
	return render_template(
		'./account/usercenter.html'
	)


########################################HOME INDEX########################################
@app.route('/home')
def home():
	return render_template(
		'apps/home.html'
	)

@app.route('/home/banner')
def banner():
	return render_template(
		'apps/01_banner.html'
	)


@app.route('/home/SmallStore')
def smallstore():
	return render_template(
		'apps/02_SmallStore.html'
	)


@app.route('/home/Busstation')
def busstation():
	return render_template(
		'apps/03_Busstation.html'

	)


@app.route('/home/Wolserver')
def wolserver():
	return render_template(
		'apps/04_Wolserver.html'
	)


@app.route('/home/report')
def report():
	return render_template(
		'apps/05_report.html'
	)


################################################################################
if __name__ == '__main__':
	app.run()
