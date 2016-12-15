

import simplejson, urllib

url = 'http://www.bankswiftifsccode.com/api/check_ifsc_code/ifsc/1234567890/format/json'
result = simplejson.load(urllib.urlopen(url))
print result