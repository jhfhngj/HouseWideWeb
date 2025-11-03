import socket
from .configserver import HOST, PORT, BUFFER_SIZE
from .handlers import handle_client

class HWWServer:
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port

    def start(self, extra, inputs):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Test service listening on {self.host}:{self.port}")

            while True:
                conn, addr = s.accept()
                with conn:
                    handle_client(conn, addr, BUFFER_SIZE, extra, inputs)
