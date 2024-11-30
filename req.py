print("Hello world")

import requests

x = requests.get("http://httpbin.org/get")
print(x)
print(x.headers)
print(x.headers['Server'])

if x.status_code == 200:
    print("Success")
elif x.status_code == 404:
    print("Error")

print(x.elapsed)
print(x.cookies)

x = requests.get("http://httpbin.org/get", params={"id":'1'})
