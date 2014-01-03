# -*- coding: utf-8 -*-
"""
ObviForum Flask application file.
Author: David Cloutman
License: MIT
"""

from flask import Flask, url_for, render_template, flash, redirect, request, session, abort
from flask.ext.sqlalchemy import SQLAlchemy
import obvi_config as obvi_config
import obvi_utilities as obvi_utilities
import forms

template_folder = "themes/{0}/templates".format(obvi_config.theme)
static_folder = "themes/{0}/static".format(obvi_config.theme)


app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{0}:{1}@{2}/{3}".format(obvi_config.mysql_username, obvi_config.mysql_password, obvi_config.mysql_host, obvi_config.mysql_database)
app.config['SECRET_KEY'] = obvi_config.secret_key
app.config['CSRF_ENABLED'] = obvi_config.csrf_enabled

db = SQLAlchemy(app, session_options={'autoflush':True})

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

	threads = models.Thread.query.join(models.User, models.Thread.originator_user_id==models.User.user_id).order_by(models.Thread.time_started.desc()).all()
	return render_template('index.tpl', user_is_authenticated=user_is_authenticated, threads=threads, authenticated_user=authenticated_user, welcome_text=obvi_config.welcome_text, login_form=forms.LoginForm())


@app.route('/thread/<thread_id>')
def view_thread(thread_id = None):

	thread = models.Thread.query.filter_by(thread_id=thread_id).first()

	if thread:
		posts = models.Post.query.filter_by(thread_id=thread.thread_id).join(models.User, models.User.user_id==models.Post.user_id).order_by(models.Post.post_datetime)

		authenticated_user = None
		user_is_authenticated = obvi_utilities.is_user_authenticated()
		if user_is_authenticated:
			authenticated_user = obvi_utilities.get_authenticated_user()
			response_form = forms.RespondToPostForm(thread_id=thread_id)
			return render_template('thread.tpl', thread=thread, user_is_authenticated=user_is_authenticated, authenticated_user=authenticated_user, posts=posts, response_form=response_form)
		else:
			return render_template('thread.tpl', thread=thread, user_is_authenticated=user_is_authenticated, authenticated_user=authenticated_user, posts=posts, login_form=forms.LoginForm())
	else:
		abort(404) 

@app.route('/thread/create', methods=['POST'])
def create_thread():
	authenticated_user = obvi_utilities.require_authentication()

	if authenticated_user:
		try:
			new_thread = models.Thread(request.form['new_thread_title'], originator_user_id = authenticated_user.user_id)
			first_post = models.Post(request.form['post_content'], thread = new_thread, user_id = authenticated_user.user_id )

			db.session.add(new_thread)
			db.session.add(first_post)
			db.session.commit()
			flash("Your post created a new thread.", 'success')
			return redirect(url_for('index'))
		except:
			db.session.rollback()
			flash("Your post could not be saved.", 'error')
			return redirect(url_for('index'))
	else:
		return redirect(url_for('login'))


@app.route('/thread/respond', methods=['POST'])
def add_post_to_thread():
	authenticated_user = obvi_utilities.require_authentication()

	if authenticated_user:
		try:
			current_thread = models.Thread.query.filter_by(thread_id=request.form['thread_id']).first()
			if current_thread:
				new_post = models.Post(request.form['post_content'], thread_id = current_thread.thread_id, user_id=authenticated_user.user_id)

				db.session.add(new_post)
				db.session.commit()
				flash("Your post was added to the thread.", 'success')
				return redirect("/thread/{0}".format(request.form['thread_id']))
			else:
				flash("Bad thread id.", 'error')
				return redirect(url_for('index'))
		except:
			db.session.rollback()
			flash("Your post could not be saved.", 'error')
			return redirect("/thread/{0}".format(request.form['thread_id']))
	else:
		return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
	login_form = forms.LoginForm()

	if 'POST' == request.method:
		# Validate the login.
		hashed_password = models.User.hash_password(request.form['password'])
		try:
			validated_user = None
			if login_form.validate_on_submit():
				validated_user = models.User.query.filter_by(username=request.form['username'], password=hashed_password).first()
			else:
				raise Exception('Login form did not pass validation.')
		except:
			flash("Could not query user. You may have forgotten to enter your username or password.", 'error')
		finally:
			if validated_user is not None:
				session['user_id'] = validated_user.user_id
				flash("Login was successful!", 'success')
				return redirect(request.referrer)
			else:
				flash("Login failed. You supplied invalid credintials.", 'warning')

	# Method is either GET or the user did supply valid credintials.
	authenticated_user = None
	user_is_authenticated = obvi_utilities.is_user_authenticated()
	if user_is_authenticated:
		authenticated_user = obvi_utilities.get_authenticated_user()

	return render_template('login.tpl', user_is_authenticated=user_is_authenticated, authenticated_user=authenticated_user, login_form=login_form);


@app.route('/logout')
def logout():
	session.pop('user_id', None)
	return redirect(request.referrer)

# Routes to the terms of service page.
@app.route('/tos')
def tos():
	return render_template('tos.tpl')


@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.tpl'), 404

@app.teardown_request
def teardown_request(exception):
	if db is not None:
		db.session.close_all()

@app.teardown_appcontext
def shutdown_session(response):
	if db is not None:
		db.session.close_all()


# Runs the application if called from the command line. 
# Useful for development but not for production
if __name__ == '__main__':
	app.run(host=obvi_config.application_host)
