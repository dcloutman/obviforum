from obvi import db
from obvi import obvi_config
from datetime import datetime
from sqlalchemy.dialects import mysql
import hashlib

class User(db.Model):
	__tablename__ = 'Users'

	# Declare columns for Users.
	user_id = db.Column(mysql.MEDIUMINT(9, unsigned = True), primary_key = True)
	username = db.Column(mysql.VARCHAR(128), unique = True)
	password = db.Column(mysql.VARCHAR(256))
	email = db.Column(mysql.VARCHAR(190), unique = True)
	is_admin = db.Column(db.Boolean)

	def __init__ (self, username, email, password, is_admin = 0):
		self.username = username
		self.email = email
		self.is_admin = is_admin

		self.password = self.hash_password(password)


	def __repr__ (self):
		return '<User {0}: {1}>'.format(self.user_id, self.username)

	# A helper function to encapsulate password hashing
	@staticmethod
	def hash_password (password):
		#Use sha256 hashing to store the algorithm. Salt is appended to the user input to make reverse lookup more difficult.
		sha = hashlib.sha256()
		sha.update( password + obvi_config.user_password_salt )
		return sha.hexdigest()



class Thread(db.Model):
	__tablename__ = 'Threads'

	# Declare columns for Threads
	thread_id = db.Column(mysql.BIGINT(20, unsigned = True), primary_key = True)
	subject = db.Column(mysql.VARCHAR(2048))
	time_started = db.Column(mysql.TIMESTAMP)
	originator_user_id = db.Column(mysql.MEDIUMINT(9), db.ForeignKey('Users.user_id'))

	# Object members for one-many relationships
	originator = db.relationship('User', backref = db.backref('Threads', lazy='dynamic'))

	def __init__ (self, subject, originator = None, originator_user_id = None, time_started = None):
		self.subject = subject
		if time_started is None:
			self.time_started = datetime.now()
		else:
			self.time_started = time_started

		if originator_user_id is not None:
			self.originator_user_id = originator_user_id

		self.originator = originator

	def __repr__ (self):
		return '<Thread {0}: "{1}">'.format(self.thread_id, self.subject)



class Post(db.Model):
	__tablename__ = 'Posts'

	#Declare columns for Posts
	post_id = db.Column(mysql.BIGINT(20, unsigned = True), primary_key = True)
	thread_id = db.Column(mysql.BIGINT(20, unsigned = True), db.ForeignKey('Threads.thread_id'))
	user_id = db.Column(mysql.MEDIUMINT(9), db.ForeignKey('Users.user_id'))
	post_datetime = db.Column(mysql.DATETIME)
	post_message = db.Column(mysql.TEXT)

	# Object members for one-many relationships
	thread = db.relationship('Thread', backref = db.backref('Posts', lazy = 'dynamic'))
	user = db.relationship('User', backref = db.backref('Posts', lazy = 'dynamic'))

	def __init__ (self, post_message, thread=None, thread_id=None, user = None, user_id = None, post_datetime = None):
		self.thread = thread
		self.thread_id = thread_id
		self.user = user
		self.post_message = post_message
		if post_datetime is None:
			self.post_datetime = datetime.now()
		else:
			self.post_datetime = post_datetime

		if user_id is not None:
			self.user_id = user_id

	def __repr__ (self):
		return '<Post {0}: {1}>'.format(self.post_id, self.thread_id)
	