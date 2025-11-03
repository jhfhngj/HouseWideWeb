import socket
from .config import HOST, PORT, BUFFER_SIZE
from .registry import load_registry, save_registry

class DNSRegistryServer:
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"HWW DNS listening on {self.host}:{self.port}")

            while True:
                conn, addr = s.accept()
                with conn:
                    self.handle_connection(conn, addr)

    def handle_connection(self, conn, addr):
        data = conn.recv(BUFFER_SIZE)
        if not data:
            print("No data received.")
            return

        message = data.decode().strip()
        print(f"Received: {message}")

        registry = load_registry()

        if message.startswith("reg "):
            domain = message[4:]
            print(f"Registering domain: {domain}")
            registry[domain] = {"ip": addr[0], "port": addr[1]}
            save_registry(registry)
            conn.sendall(b"HWW/1.0 100 OK\n")

        elif message.startswith("get "):
            domain = message[4:]
            print(f"Looking up domain: {domain}")
            if domain in registry:
                result = f"HWW/1.0 100 OK\n{registry[domain]['ip']}:{registry[domain]['port']}\n"
                conn.sendall(result.encode())
            else:
                conn.sendall(b"HWW/1.0 101 Not Found\n")

        else:
            print("Unknown request type.")
            conn.sendall(b"HWW/1.0 102 Malformed Request\n")

        print("Connection closed.")
