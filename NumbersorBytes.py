from pwn import *
from itertools import islice
import hashlib
from Crypto.Util.number import long_to_bytes
from Crypto.Util.number import bytes_to_long
import binascii
import time

r = remote('bytes.tghack.no', 2010)
i = 0
l = 0
while True:
   try:
      msg = r.recv()
   except EOFError as e:
      print msg
      break
   lines = msg.splitlines()
   if lines[0+i] == 'Here\'s a number:':
      result = long_to_bytes(lines[1+i].encode())
      r.send(binascii.hexlify(result)+"\n")
   if lines[0+i] == 'Here\'s some bytes:':
      result = bytes_to_long(binascii.unhexlify(lines[1+i].encode()))
      r.send(str(result)+"\n")
   i = 1
   l = l + 1
   if l > 1001:
      break
print msg
