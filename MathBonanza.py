from pwn import *
from itertools import islice

r = remote('math.tghack.no', 10000)
i = 0
while True:
   msg = r.recv()
   lines = msg.splitlines()
   print lines
   r.send(str(eval(lines[1+i]))+"\n")
   print eval(lines[1+i])
   i = 1
