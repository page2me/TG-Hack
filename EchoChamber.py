from pwn import *

r = remote('echo.tghack.no', 5555)
while True:
   msg = r.recv()
   r.send(msg)
   print msg
