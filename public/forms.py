# -*- coding: utf-8 -*-         
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, HiddenField
import wtforms.validators as validators

class LoginForm (Form):
	username = StringField(label='Username', id='login_form_username', validators=[validators.InputRequired(), validators.Length(min=1, max=128)])
	password = PasswordField(label='Password', id='login_form_password', validators=[validators.InputRequired(), validators.Length(min=1, max=2048)])

class CreateThreadForm (Form):
	new_thread_title = StringField(label='Thread Title', id='new_thread_title', validators=[validators.InputRequired(), validators.Length(min=1, max=128)])
	post_content = TextAreaField(label='Message', id='new_thread_content', validators=[validators.InputRequired(), validators.Length(min=1, max=102400)])

class RespondToPostForm (Form):
	thread_id = HiddenField(validators=[validators.NumberRange(min=1)])
	# Set an arbitrary maximum on characters in post content to prevent abuse. TODO: Make this user configurable.
	post_content = TextAreaField(label='Message', id='thread_response', validators=[validators.InputRequired(), validators.Length(min=1, max=102400)])

class SignupForm (Form):
	email = StringField(label='Email', validators=[validators.InputRequired(message="You must supply a valid email address."), validators.Email("Your email address did not conform to a valid format.")])
	username = StringField(label='Username', id='account_creation_form_username', validators=[validators.InputRequired("You must create a username."), validators.Length(min=2, max=128, message="Your username must be between 2-128 characters in length.")])
	password = PasswordField(label='Password', id='account_creation_form_password', validators=[validators.InputRequired(), validators.Length(min=8, max=2048, message="Your password must be at least 8 characters long.")])
	password_confirm = PasswordField(label='Confirm Password', id='account_creation_form_password_confirm', validators=[validators.InputRequired(message="You must confirm your password."), validators.EqualTo('password', "Your passwords must match.")])
