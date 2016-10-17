# This module contains utility functions.
from flask import session, redirect, flash
import obviforum_app.models as models
from obviforum_app.obvi import db

"""
This function should be called at the beginning of any route that requires user authentication.
"""
def require_authentication():
	if 'user_id' in session:
		# Return a user object for the user identified by user_id.
		return get_authenticated_user()
	else:
		# User is not logged in. Forward them to the login page.
		redirect(url_for('login'))

"""
Returns all data for the currently authenticated user.
"""
def get_authenticated_user():
	return models.User.query.filter_by(user_id=session['user_id']).first()
	
"""
This function may be called to determine program behavior based on the user's authentication state.
"""
def is_user_authenticated():
	if 'user_id' in session:
		return True
	else:
		return False

"""
Adds error messages from WTForm validation errors to flash messages.
"""
def queue_form_errors_in_flash (form):
	for field, errors in form.errors.items():
		for error in errors:
			flash('<label for="%s">%s:</label> %s' % (
				getattr(form, field).id,
				getattr(form, field).label.text,
				error
			), 'error')

