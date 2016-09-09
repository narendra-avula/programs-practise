
import os, sys
from time import sleep
import requests
from bs4 import BeautifulSoup

def sendmessage(title, message):
  os.system('notify-send "'+title+'" "'+message+'"')

url = "http://static.cricinfo.com/rss/livescores.xml"
sc = requests.get(url)
soup = BeautifulSoup(sc.text, "html5lib")

i = 1
for data in soup.findAll('item'):
    print str(i)+'. '+data.find('description').text
    i += 1

list_links = []
for link in soup.findAll('item'):
    list_links.append(link.find('guid').text)

print 'Enter match no. or enter 0 to exit:'
while True:
    try:
        user_input = int(input())
    except NameError:
        print 'Enter correct input'
        continue
    except SyntaxError:
        print 'Enter correct input'
    if user_input < 0 or user_input > 30:
        print 'Enter correct input'
        continue
    else:
        break

url = list_links[user_input - 1]
sc = requests.get(url)
soup = BeautifulSoup(sc.text, "html5lib")

while True:
    url = list_links[user_input - 1]
    sc = requests.get(url)
    soup = BeautifulSoup(sc.text, "html5lib")
    score = soup.findAll('title')
    try:
        sc.raise_for_status()
    except Exception as exc:
        print ('Connection Issue')
        continue
    sendmessage('Live Score',score[0].text)
    sleep(30)