# This module contains utility functions.
from flask import session, redirect
import models
from obvi import db

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


