import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://py4e-data.dr-chuck.net/known_by_Babur.html'
count = 7
position = 18

for tag in range(count):
    
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    tags = soup('a')
    
    url = tags[position - 1].get('href', None)
    last_name = url.split('_')[-1].split('.')[0]
    
print(last_name)
