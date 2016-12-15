__author__ = 'narendra'


# import urllib
#
# urllib.urlretrieve("http://www.digimouth.com/news/media/2011/09/google-logo.jpg", "local-filename.jpg")

import os
import urllib
import json
import url as url
import requests

category_list = [
    "study-tables", "coffee-tables", "bar-units", "chest-of-drawers", "shoe-racks", "dressing-units",
    "stools", "wardrobes", "dining-tables", "crockery-units", "beds", "pooja-units", "tv-units",
    "chairs", "sofas", "client-renders", "curtains", "cushions", "false-ceiling", "wallpapers",
    "wall-storage", "book-racks", "console-units", "facebook", "flyers", "store", "office-furnishing",
    "configurator", "wooden-flooring", "website", "looks-book", "miscellaneous"
                 ]

for category in category_list:
    category_name = category

    directory_path = os.path.join('/home/narendra/3dteam/' + category_name + '/')
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    filePath = os.path.join('/home/narendra/3dteam/' + category_name + '/')
    imagesUrl = "http://54.255.138.112/api/product-store/products?category=" + category_name

    response = urllib.urlopen(imagesUrl)
    json_obj = json.load(response)

    for obj in json_obj['result']:
        if os.path.exists(filePath + obj['name'] ):
            print obj['category'] +" " + obj['name'] + " already in backup"
        else:
            urllib.urlretrieve(obj['image'], filePath + obj['name'])
            print obj['category'] +" " + obj['name'] + ' Done'