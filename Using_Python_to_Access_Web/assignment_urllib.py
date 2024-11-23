import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = urllib.request.urlopen('https://py4e-data.dr-chuck.net/comments_2122792.html')
soup = BeautifulSoup(url, 'html.parser')

count = 0

tags = soup('span')
for tag in tags:
    tag = re.findall('[0-9]+', tag.text)
    for num in tag:
        count += int(num)
print(count)
    