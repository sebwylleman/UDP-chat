import socket

MAX_SIZE_BYTES = 65535  # Mazimum size of a UDP datagram


def server(port):
    host = "127.0.0.1"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host, port))


def client(port):
    pass
    # Your code goes here
