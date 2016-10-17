#!/usr/bin/env python
import sys
import logging
import os
logging.basicConfig(stream=sys.stderr)
file_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, file_dir)
from main import app as application
from main import db
