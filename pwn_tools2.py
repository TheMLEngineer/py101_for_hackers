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
print("*"*50)

r = ROP(l)
print(r.rbx)

print(xor('A', 'B'))
print("*"*50)

print(b64e(b"Hi"))
print(b64d(b"SGk="))

print(md5sumhex(b"Hi"))
print(sha1sumhex(b"Hi"))

print(bits(b'a'))
print(unbits([0, 1, 1, 0, 0, 0, 0, 1]))