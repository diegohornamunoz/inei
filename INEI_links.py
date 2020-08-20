#import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import requests
    
#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

source = requests.get('https://censos2017.inei.gob.pe/bininei/RpWebStats.exe/Frequency?BASE=CPV2017DI&ITEM=FREQVIV&lang=esp').text

soup = BeautifulSoup(source,'lxml')

#print(soup.prettify())

form = soup.find('form')
print(form.prettify())
