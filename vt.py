from __future__ import print_function
import json
import hashlib
from virus_total_apis import PublicApi as VirusTotalPublicApi

#var url_site = window.location.href

API_KEY = 'd80559c1630c37cc117eb7ea2d7fe14af4ee80317b2842ce1c684e120d5af85b'

vt = VirusTotalPublicApi(API_KEY)
import requests
url = 'https://www.virustotal.com/vtapi/v2/url/report'
params = {'apikey': API_KEY, 'resource':'https://www.youtube.com/'}
response = requests.get(url, params=params)
#print(response.json())
result = response.json()
p = result['positives']

if p > 0:
    print('The site is safe.')
else:
    print('Phishing detected!!!')

