"""
Example of how requests are used
"""
import requests

print("------------------------\nDELETE\n------------------------")
r = requests.delete('http://httpbin.org/delete')
print(r)
print("------------------------\nHEAD\n------------------------")
r = requests.head('http://httpbin.org/get')
print(r)
print("------------------------\nOPTIONS\n------------------------")
r = requests.options('http://httpbin.org/get')
print(r)
print("------------------------\nPUT\n------------------------")
r = requests.put('http://httpbin.org/put', data={'key': 'value'})

print('STATUS CODE: ', r.status_code)
print('REASON: ', r.reason)
print('CONTENT: ', r.content)
print('TEXT: ', r.text)
