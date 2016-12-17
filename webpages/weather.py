# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import json
import os
import requests
import sys

from cgi import parse_qs

from utils import kelvin_to_fahrenheit

SLACKRESPONSE = """\
{o[temp]}*F ({o[temp_min]}F - {o[temp_max]}F)
{o[humidity]}% humidity
"""


def request_data(request_body):
	"""Returns a dict containing data from wsgi.input's
	:request_body:."""

	return parse_qs(request_body)


def weather(request_type, request_body):
	"""An HTTP request handler that returns the weather
	for a given location."""

	APIKEY = '0f02e726e5ba577af096f8d3a2efc18b'
	BASEURL = 'http://api.openweathermap.org/data/2.5/weather'

	if request_type == 'POST':
		d = request_data(request_body)
		zip_code = str(d.get('text')[0])

		r = requests.post(BASEURL, params=dict(APPID=APIKEY, zip=zip_code))
		content = json.loads(r.content)
		weather = content.get('main')

   # Convert to fahrenheit
		for t in ('temp_min', 'temp_max', 'temp'):
			weather[t] = kelvin_to_fahrenheit(weather.get(t))
		return SLACKRESPONSE.format(o=weather)

	elif request_type == 'GET':
		# TO DO: HANDLE GET REQUEST
		return 'Handling weather get request'
	else:
		raise ValueError('Invalid Request Type', request_type)
