__author__ = 'narendra'


import urllib2
import re

#connect to a URL
url = 'http://www.customfurnish.com'
website = urllib2.urlopen(url)

#read html code
html = website.read()

#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

print links
