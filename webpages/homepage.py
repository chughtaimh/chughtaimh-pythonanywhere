# -*- coding: UTF-8 -*-
#!/usr/bin/env python
"""Contains code for homepage request handling"""
import os
import sys

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
sys.path.append(CURRENT_DIRECTORY + '/')


def homepage(*args, **kwargs):
	"""An HTTP request handler that returns the homepage"""
	with open('home.html', 'r') as f:
		return f.read()
