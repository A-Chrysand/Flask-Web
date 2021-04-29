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


@app.route("/js_post/<getdata>", methods=['GET', 'POST'])
def js_post(getdata):
	print('\tPOST from>>>' + request.remote_addr + '->' + getdata, end="")
	if Decipher().process_num(getdata):
		print("->login success")
		return redirect(url_for('home'))
	else:
		print("->login failed")
		return "login fail"
