# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, TextAreaField
import wtforms.validators as validators

class LoginForm (Form):
	username = StringField(label='Username', id='login_form_username', validators=[validators.required(), validators.length(min=1, max=128)])
	password = PasswordField(label='Password', id='login_form_password', validators=[validators.required(), validators.length(min=1, max=128)])
