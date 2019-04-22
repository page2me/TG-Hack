from pwn import *
from itertools import islice
from hashlib import md5
from hashlib import sha256
from hashlib import sha512

#f = open('out.txt', 'w')
r = remote('hash.tghack.no', 2001)
i = 0
l = 0
while True:
   try:
      msg = r.recv()
   except EOFError as e:
      print(msg)
   lines = msg.splitlines()
   y4 = lines[3-i]
   x2 = lines[4-i]
   print y4
   print x2
   #result = {
   #  'MD5':  md5(x2),
   #  'SHA256': sha256(x2),
   #  'SHA512': sha512(x2)
   #}[y4](x2)
   if y4 == 'MD5':
      result = md5(x)
   elif y4 == 'SHA256':
      result = sha256(x)
   elif y4 == 'SHA512':
      result = sha512(x)
   #print(msg)
   try:
      r.send(result.hexdigest()+"\n")
   except EOFError as e:
      print(msg)
#   print >> f, lines[3-i]+lines[4-i]+":"+result.hexdigest()
   msg = ""
   i = 3
   l = l + 1
   if l > 1001:
      break
