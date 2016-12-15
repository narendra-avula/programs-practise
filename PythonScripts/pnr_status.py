import os, sys
from time import sleep
import requests
from bs4 import BeautifulSoup

def sendmessage(title, message):
  os.system('notify-send "'+title+'" "'+message+'"')

try:
    # pnr = input('Enter pnr ')
    pnr = '4321564208'
    url = 'http://www.railyatri.in/pnr-status/' + pnr
    sc = requests.get(url)
    soup = BeautifulSoup(sc.text, 'html5lib')
    cs = soup.findAll('span', {'class': 'arrival_span'})
    bs = soup.findAll('span', {'class': 'departure'})
    sendmessage('PNR Status', 'Booking Satus: ' + bs[1].text + '\n' + 'Curent Satus: ' + cs[2].text)

except requests.exceptions.ConnectionError:
    sendmessage('Connection Issue', 'No internet found')