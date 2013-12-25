# -*- coding: utf-8 -*-
"""
Bloggle Flask application file.
Author: David Cloutman
License: MIT
"""

from flask import Flask, url_for, render_template, flash, redirect, request, session
from flask.ext.sqlalchemy import SQLAlchemy
import ObviConfig as obvi_config
import obvi_utilities as obvi_utilities

template_folder = "themes/{0}/templates".format(obvi_config.theme)
static_folder = "themes/{0}/static".format(obvi_config.theme)


app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{0}:{1}@{2}/{3}".format(obvi_config.mysql_username, obvi_config.mysql_password, obvi_config.mysql_host, obvi_config.mysql_database)
app.config['SECRET_KEY'] = obvi_config.secret_key
db = SQLAlchemy(app)

# Enable debug mode if configured.
if obvi_config.debug_mode:
	app.debug = True

import models


@app.route('/')
def index():
	user_is_authenticated = obvi_utilities.is_user_authenticated()
	threads = models.Thread.query.order_by(models.Thread.time_started.desc())
	return render_template('index.tpl', user_is_authenticated=user_is_authenticated, threads=threads)


@app.route('/thread/<thread_id>')
def view_thread(thread_id = None):
	thread_subject = "Thread #{0} Topic".format(thread_id)
	user_is_authenticated = obvi_utilities.is_user_authenticated()
	return render_template('thread.tpl', thread_subject=thread_subject, user_is_authenticated=user_is_authenticated)


@app.route('/login', methods=['POST', 'GET'])
def login():
	if 'POST' == request.method:
		# Validate the login.
		hashed_password = models.User.hash_password(request.form['password'])
		try:
			validated_user = models.User.query.filter_by(username=request.form['username'], password=hashed_password).first()
		except:
			flash("Could not query user.")
		finally:
			if validated_user is not None:
				session['user_id'] = validated_user.user_id
				flash("Login was successful!")
				return redirect(url_for('index'))
			else:
				flash("Login failed. You supplied invalid credintials.")

		# On success.
		#if True:
		#	return redirect(url_for('index'))
		#else:
		#	flash('Invalid login.')

	# Method is either GET or the user did supply valid credintials.

	return render_template('login.tpl', user_is_authenticated=obvi_utilities.is_user_authenticated());


@app.route('/logout')
def logout():
	session.pop('user_id', None)
	return redirect(url_for('index'))


# Runs the application if called from the command line. 
# Useful for development but not for production
if __name__ == '__main__':
	app.run(host=obvi_config.application_host)
