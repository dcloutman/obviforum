#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/lampfire/obvi-forum/obviforum_app')
from obvi import app as application
from obvi import db as db
