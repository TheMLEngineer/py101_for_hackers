from pwn import *

print(p32(0x1337))

print(hex(u32(p32(0x1337))))

l = ELF('/bin/bash')
print(hex(l.address))
print(hex(l.entry))

print(hex(l.got['write']))
print(hex(l.plt['write']))

print("*"*50)
for address in l.search(b'/bin/sh\x00'):
    print(hex(address))

print("*"*50)

print(hex(next(l.search(asm('jmp esp')))))