"""
Bloggle Flask application file.
Author: David Cloutman
License: MIT
"""

from flask import Flask
import BloggleConfig as config

app = Flask(__name__)

@app.route('/')
def index():
	return 'Welcome to Bloggle'

if __name__ == '__main__':
	app.run(host='0.0.0.0')
