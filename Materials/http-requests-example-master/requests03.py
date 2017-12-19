"""
Example of requests with json as body
"""
import requests
import json

r = requests.post(
    url='http://httpbin.org/post',
    params={'my-param-name': 'param-value'},
    headers={'my-header-name': 'header-value'},
    json=json.dumps({'some': 'value'})
)

print('STATUS CODE: ', r.status_code)
print()
print('REASON: ', r.reason)
print()
print('CONTENT: ', r.content)
print()
print('TEXT: ', r.text)
print()
print('JSON: ', r.json())
print()
print('JSON TYPE: ', r.json().__class__.__name__)
