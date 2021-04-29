"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWeb import app
from flask import request, url_for, redirect
from FlaskWeb.py_functions.decipher import Decipher


@app.route('/')
@app.route("/login")
def login():
	return render_template(
		'./account/login.html',
		title='Dreamweaver',
		year=datetime.now().year,
	)


@app.route('/home')
def home():
	"""Renders the home page."""
	return render_template(
		'./host/home.html',
		title='Home Page',
		year=datetime.now().year,
	)


@app.route("/login_js_post/<login_getdata>", methods=['POST'])
def login_js_post(login_getdata):
	print('\tPOST from>>>' + request.remote_addr, end="")
	logincheck_result = Decipher().login_check(login_getdata)
	if logincheck_result == 'success':
		print("->" + '\033[0;32m' + "login success" + '\033[0m' + "||src=" + login_getdata)
		return logincheck_result
	else:
		print("->" + '\033[0;34m' + "login failed" + '\033[0m' + "||src=" + login_getdata)
		return logincheck_result


@app.route("/register_js_post/<RegisterCheck_getdata>", methods=['POST'])
def register_js_post(RegisterCheck_getdata):
	print('\tRegistering>>>' + request.remote_addr+">>>", end="")
	registercheck_result = Decipher().register_check(RegisterCheck_getdata)
	return registercheck_result
