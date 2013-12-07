"""
BLOGGLE CONFIGURATION FILE
-- Copy this file to BloggleConfig.py, remove this line, and below, change the values to match your environment. ---
Author: David Cloutman
License: MIT
"""

application_host = '127.0.0.1' # The I.P. address upon which the Flask application runs. 0.0.0.0 will listen on all public IP addresses.

debug_mode = False # Set to true to run the Flask application in debug mode. DO NOT USE DEBUG MODE IN PRODUCTION!

mysql_host = '127.0.0.1' # The domain or I.P. address that your MySQL instance is running on.
mysql_database = '' # Give bloggle its own database to avoid conflicts with other applications.
mysql_username = '' # Create a non-root user for Bloggle.
mysql_password = '' # Use a strong password.
