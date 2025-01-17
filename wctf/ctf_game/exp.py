from pwn import *
import sys
from time import sleep
from LibcSearcher import *

proc = './CTF_Game'
if len(sys.argv) == 1:
    c = process(proc)
elif len(sys.argv) == 2:
    serverport = sys.argv[1].split(':')
    c = remote(serverport[0], int(serverport[1]))
else:
    c = remote(sys.argv[1], int(sys.argv[2]))
context.binary = proc
elf = ELF(proc)
rop = ROP(proc)


c.interactive()
