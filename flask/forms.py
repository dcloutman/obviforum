# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, HiddenField
import wtforms.validators as validators

class LoginForm (Form):
	username = StringField(label='Username', id='login_form_username', validators=[validators.required(), validators.length(min=1, max=128)])
	password = PasswordField(label='Password', id='login_form_password', validators=[validators.required(), validators.length(min=1, max=128)])

class CreateThreadForm (Form):
	pass

class RespondToPostForm (Form):
	thread_id = HiddenField(validators=[validators.NumberRange(min=1)])
	# Set an arbitrary maximum on characters in post content to prevent abuse. TODO: Make this user configurable.
	post_content = TextAreaField(label='Message', id='thread_response', validators=[validators.required(), validators.length(min=1, max=102400)])

class CreateUserForm (Form):
	pass