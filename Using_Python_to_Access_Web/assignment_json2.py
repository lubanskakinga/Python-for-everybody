import urllib.request, urllib.parse
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

add = input('Enter location: ')

parms = dict()
parms['q'] = add

url = serviceurl + urllib.parse.urlencode(parms)

html = urllib.request.urlopen(url, context=ctx).read().decode()
js = json.loads(html)

lst = js['features'][0]['properties']['plus_code']

print(lst)


