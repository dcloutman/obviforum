"""
ObviForums CONFIGURATION FILE
-- Copy this file to ObviConfig.py, remove this line, and below, change the values to match your environment. ---
Author: David Cloutman
License: MIT
"""

# The I.P. address upon which the Flask application runs. 0.0.0.0 will listen on all public IP addresses.
application_host = '127.0.0.1'

# Set to true to run the Flask application in debug mode. DO NOT USE DEBUG MODE IN PRODUCTION!
debug_mode = False


# DATABASE CONFIGURATION

# The domain or I.P. address that your MySQL instance is running on.
mysql_host = '127.0.0.1' 

# Give ObviForums its own database to avoid conflicts with other applications.
mysql_database = ''

# Create a non-root user for ObviForums.
mysql_username = ''

# Use a strong password.
mysql_password = ''


# This string mixes in with the user-supplied password to make reverse hashing more difficult. Choose something random.
user_password_salt = ''


# FOR WTForms


CSRF_ENABLED = True

# Make this something truly random. This will protect against malicious posts doing harm to your users.
SECRET_KEY = ''

