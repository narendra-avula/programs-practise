__author__ = 'narendra'

import urllib
url = "https://brightside.me"
# url = "https://www.google.com"
f = urllib.urlopen(url)
print f.read()



# import urllib2
# from BeautifulSoup import BeautifulSoup
#
#
# download_url = 'https://brightside.me/article/100-best-photographs-without-photoshop-46555/?utm_source=fb_r69f33&utm_campaign=pub1171&utm_medium=cpm'
#
# page = BeautifulSoup(urllib2.urlopen(download_url))
# print page.findAll('img')


# from html.parser import HTMLParser
# class MyParse(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         if tag=="img":
#             print(dict(attrs)["src"])
#
# h=MyParse()
# page=open("index.html").read()
# h.feed(page)