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
print(x.url)

x = requests.get("http://httpbin.org/get", params={"id":'3'}, headers = {'Acceopt':'application/json'})
print(x.text)

x = requests.delete("http://httpbin.org/delete")
print(x.text)

x = requests.post("http://httpbin.org/post",data = {'a':'b'})
print(x.text)

# adding image as part of post

files = {'file': open('google.png','rb')}

x = requests.post("http://httpbin.org/post",files = files)
print(x.text)

x = requests.get("http://httpbin.org/get", auth=('username','password'))
print(x.text)

"""
(venv) ┌─[✗]─[user@parrot]─[~/Documents/TCM/py101_for_hackers]
└──╼ $echo -ne dXNlcm5hbWU6cGFzc3dvcmQ= | base64 -d
username:password(venv) ┌─[user@parrot]─[~/Documents/TCM/py101_for_hackers]
└──╼ $
"""


"""
x = requests.get('https://expired.badssl.com')
print(x)

requests.exceptions.SSLError: HTTPSConnectionPool(host='expired.badssl.com', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:992)')))
"""

x = requests.get('https://expired.badssl.com',verify=False)
print(x)

x = requests.get('https://github.com')
print(x.headers)

x = requests.get('https://github.com',timeout = 3)
print(x.text)

x = requests.get("http://httpbin.org/cookies")
print(x.content)


x = requests.Session()
x.cookies.update({'a':'b'})
print(x.get("http://httpbin.org/cookies").text)