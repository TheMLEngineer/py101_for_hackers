from pwn import *
import sys


"""

(env) ┌─[user@parrot]─[~/Documents/py101_for_hackers]
└──╼ $echo -ne hannah | sha256sum
fc881aa34d44660e1012dec26ccda0b469d6c8359e91dc674dab4c095b9fe832  -

WE HAVE TO GET SHA256SUM for any passwoed that is present in the file and then compare

"""

if len(sys.argv) != 2:
    print("Invalid args")
    print(f"{sys.argv[0]} <sha256sum>")
    exit()

wanted_hash = sys.argv[1]
print(f"Wanted Hash : {wanted_hash}")

password_file = 'rockyou_part_aa'
attempts = 0

with log.progress(f"Attempting to back: {wanted_hash}!\n") as p:
    with open(password_file,'r',encoding='latin-1') as password_list:
        for password in password_list:
            password = password.strip('\n').encode('latin-1')
            password_hash = sha256sumhex(password)
            p.status(f"{attempts} {password.decode('latin-1')} == {password_hash}")
            if password_hash == wanted_hash:
                p.success(f"Password hash found after {attempts} attempts! {password.decode('latin-1')} hashes to {password_hash} ")
            attempts += 1
        p.failure("Password hash NOT FOUND")

"""


(env) ┌─[✗]─[user@parrot]─[~/Documents/py101_for_hackers]
└──╼ $python3 sha_256_password_cracking.py fc881aa34d44660e1012dec26ccda0b469d6c8359e91dc674dab4c095b9fe832 
Wanted Hash : fc881aa34d44660e1012dec26ccda0b469d6c8359e91dc674dab4c095b9fe832
[◢] Attempting to back: fc881aa34d44660e1012dec26ccda0b469d6c8359e91dc674dab4c095b9fe832!
[+] : Password hash found after 49 attempts! hannah hashes to fc881aa34d44660e1012dec26ccda0b469d6c8359e91dc674dab4c095b9fe832 
(env) ┌─[user@parrot]─[~/Documents/py101_for_hackers]
└──╼ $

"""