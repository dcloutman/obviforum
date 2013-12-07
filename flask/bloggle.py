"""
Bloggle Flask application file.
Author: David Cloutman
License: MIT
"""

from flask import Flask
import BloggleConfig as config

app = Flask(__name__)
if config.debug_mode:
	app.debug = True

@app.route('/')
def index():
	return 'Welcome to Bloggle'

if __name__ == '__main__':
	app.run(host = config.application_host)
