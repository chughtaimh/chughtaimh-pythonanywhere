# This file contains the WSGI configuration required to serve up your
# web application at http://chughtaimh.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#

# +++++++++++ GENERAL DEBUGGING TIPS +++++++++++
# getting imports and sys.path right can be fiddly!
# We've tried to collect some general tips here:
# https://www.pythonanywhere.com/wiki/DebuggingImportError
import os
import sys

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
sys.path.append(CURRENT_DIRECTORY + '/')
from webpages import homepage, weather

PAGES = {
	'/': homepage,
	'/weather': weather
}


def application(environ, start_response):

	page = environ.get('PATH_INFO')
	request_type = environ.get('REQUEST_METHOD')
	request_body = environ.get('wsgi.input').read()

	try:
		status = '200 OK'
		content = get_content(page, request_type, request_body)
	except:
		status = '404 NOT FOUND'
		content = 'Page not found.'

	response_headers = [('Content-Type', 'text/html'),
						('Content-Length', str(len(content)))]
	start_response(status, response_headers)
	yield content.encode('utf8')


def get_content(page, request_type, request_body):
	"""Returns content for page given"""

	f = PAGES.get(page)
	return f(request_type, request_body)
