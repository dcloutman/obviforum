from obvi import db
from obvi import obvi_config
from datetime import datetime
import hashlib

class User(db.Model):
	__tablename__ = 'Users'

	# Declare columns for members.
	user_id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(128), unique = True)
	password = db.Column(db.String(256))
	email = db.Column(db.String(90), unique = True)
	is_admin = db.Column(db.Boolean)

	def __init__ (self, username, email, password, is_admin):
		self.username = username
		self.email = email
		self.is_admin = is_admin

		#Use sha256 hashing to store the algorithm. Salt is appended to the user input to make reverse lookup more difficult.
		sha = hashlib.sha256()
		sha.update( password + obvi_config.user_password_salt )
		self.password = sha.hexdigest()


	def __repr__ (self):
		return '<User {0}: {1}>'.format(self.user_id, self.username)
