from pwn import *
from itertools import islice
import hashlib

r = remote('hash.tghack.no', 2001)
i = 0
l = 0
while True:
   try:
      msg = r.recv()
   except EOFError as e:
      print (msg)
   lines = msg.splitlines()
   print (l)
   print (msg)
   if lines[3-i] == 'Hash me using MD5, please:':
      result = hashlib.md5(lines[4-i].encode())
   if lines[3-i] == 'Hash me using SHA256, please:':
      result = hashlib.sha256(lines[4-i].encode())
   if lines[3-i] == 'Hash me using SHA512, please:':
      result = hashlib.sha512(lines[4-i].encode())
   resp = r.send(result.hexdigest()+"\n")
   print (result.hexdigest())
   i = 3
   l = l + 1
   if l > 1001:
      break
print (msg)
