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
	authenticated_user = None
	user_is_authenticated = obvi_utilities.is_user_authenticated()
	if user_is_authenticated:
		authenticated_user = obvi_utilities.get_authenticated_user()

	threads = models.Thread.query.join(models.User, models.Thread.originator_user_id==models.User.user_id).order_by(models.Thread.time_started.desc())
	return render_template('index.tpl', user_is_authenticated=user_is_authenticated, threads=threads, authenticated_user=authenticated_user, welcome_text=obvi_config.welcome_text)


@app.route('/thread/<thread_id>')
def view_thread(thread_id = None):
	authenticated_user = None
	user_is_authenticated = obvi_utilities.is_user_authenticated()
	if user_is_authenticated:
		authenticated_user = obvi_utilities.get_authenticated_user()

	thread = models.Thread.query.filter_by(thread_id=thread_id).first()

	if thread:
		posts = models.Post.query.filter_by(thread_id=thread.thread_id).join(models.User, models.User.user_id==models.Post.user_id).order_by(models.Post.post_datetime)

	return render_template('thread.tpl', thread=thread, user_is_authenticated=user_is_authenticated, authenticated_user=authenticated_user, posts=posts)


@app.route('/thread/create', methods=['POST'])
def create_thread():
	authenticated_user = obvi_utilities.require_authentication()

	db.session.commit()
	if authenticated_user:
		try:
			new_thread = models.Thread(request.form['new_thread_title'], originator_user_id = authenticated_user.user_id)
			first_post = models.Post(new_thread, request.form['post_content'], user_id = authenticated_user.user_id )

			db.session.add(new_thread)
			db.session.add(first_post)
			db.session.commit()
			flash("Your post was saved.")
			return redirect(url_for('index'))
		except:
			db.session.rollback()
			flash("Your post could not be saved.")
			return redirect(url_for('index'))


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
	authenticated_user = None
	user_is_authenticated = obvi_utilities.is_user_authenticated()
	if user_is_authenticated:
		authenticated_user = obvi_utilities.get_authenticated_user()

	return render_template('login.tpl', user_is_authenticated=user_is_authenticated, authenticated_user=authenticated_user);


@app.route('/logout')
def logout():
	session.pop('user_id', None)
	return redirect(url_for('index'))


@app.teardown_request
def teardown_request(exception):
	if db is not None:
		db.session.close()

@app.teardown_appcontext
def shutdown_session(response):
	db.session.remove()


# Runs the application if called from the command line. 
# Useful for development but not for production
if __name__ == '__main__':
	app.run(host=obvi_config.application_host)
