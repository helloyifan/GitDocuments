#!/usr/bin/env python
#encoding=utf-8

import urllib2
import urllib

import yaml
import json
from pprint import pprint


#uWaterloo Api Key:  9a8276106f4a6c0d953f054a3e90ced2

#sample call: http://api.uwaterloo.ca/v2/foodservices/watcard.json?key=9a8276106f4a6c0d953f054a3e90ced2


def fetch(url, args):
	url = url + '?' + urllib.urlencode(args)
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	data = response.read()
	return data

