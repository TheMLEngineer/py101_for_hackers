from pwn import *

print(cyclic(50))
print(cyclic_find("laaa"))

print(shellcraft.sh())

print(hexdump(asm(shellcraft.sh())))

# Local commection
p = process("/bin/sh")
p.sendline("echo Hi")
p.interactive()

# Remote connection (Can use any IP and PORT)
r = remote("127.0.0.1", port = 1234)
r.sendline("Hello")
r.interactive()
r.close()
"""
Remote listens here and prints what I input in interactive remote session
┌─[user@parrot]─[~]
└──╼ $nc -lp 1234
Hello

ls
pwd



"""

