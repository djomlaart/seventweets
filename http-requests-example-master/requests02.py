"""
Example of a more complex POST request
"""
import requests

r = requests.post(
    url='http://httpbin.org/post',
    params={'my-param-name': 'param-value'},
    headers={'my-header-name': 'header-value'},
    data='my data'
)


print('STATUS CODE: ', r.status_code)
print('REASON: ', r.reason)
print('CONTENT: ', r.content)
print('TEXT: ', r.text)

