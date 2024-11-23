import urllib.request
import json

url = urllib.request.urlopen('https://py4e-data.dr-chuck.net/comments_2122795.json').read()

js = json.loads(url)
    
lst = js['comments']

count = 0
sum = 0

for item in lst:
    num = item['count']
    count += 1
    sum += int(num)
print(sum)
