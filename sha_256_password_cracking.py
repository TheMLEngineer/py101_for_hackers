from pwn import *
import sys

if len(sys.argv) != 2:
    print("Invalid args")
    print(f"{sys.argv[0]} <sha256sum>")
    exit()

wanted_hash = sys.argv[1]
print(f"Wanted Hash : {wanted_hash}")

password_file = 'rockyou.txt'
attempts = 0

with log.process(f"Attempting to back: {wanted_hash}!\n") as p:
    with open(password_file,'r',encoding='latin-1') as password_list:
        for password in password_list:
            password = password.strip('\n').encode('latin-1')
            password_hash = sha256sum(password)
            
