import urllib
import requests
key = 'yourapikey'
# http://cutt.ly/api/ get your api
a=input("ent link :")
url = urllib.parse.quote(f'{a}')
name  = 'nameforit'
r = requests.get(r'http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(key, url, name))
print(rf"{r}")
