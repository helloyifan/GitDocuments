#https://www.youtube.com/watch?v=9Xt2e9x4xwQ

import urllib2
import simplejson

url='''
https://api.twitter.com/1/statuses//user_timeline.json?include_entities=true&include_rts=true%screen_name=twitterapi&count=2
'''

if __name__ == "__main__":
	req = urllib2.Request(url)
	opener = urllib2.build_opener()
	f = opener.open(req)
	json = simplejosn.load(f)
