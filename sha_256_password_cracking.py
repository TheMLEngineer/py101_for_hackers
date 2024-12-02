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
    with