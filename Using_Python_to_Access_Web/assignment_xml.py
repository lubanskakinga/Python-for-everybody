import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'https://py4e-data.dr-chuck.net/comments_2122794.xml'

uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)

count = 0
sum = 0

counts = tree.findall('.//count')
nums = list()
for result in counts:
    count += 1
    sum += int(result.text)

print('Count:', count)
print('Sum:', sum)