
API_KEY = 'AIzaSyCUueQJpV5knc8fH4VEA1Q0HTqV_m_OTRg'

import simplejson, urllib
start= "Machilipatnam"
end = "Customfurnish,Hyderabad"
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=kms&origins={0}" \
      "&destinations={1}&region=IN&key={2}".format(start, end, API_KEY)
result = simplejson.load(urllib.urlopen(url))
distance = float(result['rows'][0]['elements'][0]['distance']['text'].split(" ")[0])
print distance
print result