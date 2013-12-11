# -*- coding: utf-8 -*-
"""
Bloggle Flask application file.
Author: David Cloutman
License: MIT
"""

from flask import Flask, url_for, render_template, session
import ObviForumsConfig as config

app = Flask(__name__)

# Enable debug mode if configured.
if config.debug_mode:
	app.debug = True


@app.route('/')
def index():
	return render_template('index.tpl')

@app.route('/thread/<thread_id>')
def view_thread(thread_id = None):
	thread_subject = "Thread #%s Topic" % thread_id
	return render_template('thread.tpl', thread_subject = thread_subject)

if __name__ == '__main__':
	app.run(host = config.application_host)
