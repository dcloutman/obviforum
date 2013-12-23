# -*- coding: utf-8 -*-
"""
Bloggle Flask application file.
Author: David Cloutman
License: MIT
"""

from flask import Flask, url_for, render_template, flash, redirect, session
from flask.ext.sqlalchemy import SQLAlchemy
import ObviConfig as obvi_config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{0}:{1}@{2}/{3}".format(obvi_config.mysql_username, obvi_config.mysql_password, obvi_config.mysql_host, obvi_config.mysql_database)
db = SQLAlchemy(app)

# Enable debug mode if configured.
if obvi_config.debug_mode:
	app.debug = True

import models


@app.route('/')
def index():
	first_user = models.User.query.filter_by(is_admin = False).first()
	return render_template('index.tpl', first_username = first_user.username)


@app.route('/thread/<thread_id>')
def view_thread(thread_id = None):
	thread_subject = "Thread #%s Topic" % thread_id
	return render_template('thread.tpl', thread_subject = thread_subject)

if __name__ == '__main__':
	app.run(host = obvi_config.application_host)
