from __future__ import division

import math


def kelvin_to_fahrenheit(kelvin_temp):
	"""Converts kelvin temp to fahrenheit"""

	return math.floor(9/5 * (kelvin_temp - 273) + 32)
