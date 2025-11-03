import socket
from .config import HOST, PORT, BUFFER_SIZE
from .utils import parse_response

class DNSClient:
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port

    def send_request(self, command, domain):
        domain = domain.replace("hww://", "")
        message = f"{command} {domain}"

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as dns_socket:
            dns_socket.connect((self.host, self.port))
            dns_socket.sendall(message.encode())
            response = dns_socket.recv(BUFFER_SIZE).decode()

        return parse_response(response)

class ServiceConnector:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def interact(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as service_socket:
            service_socket.connect((self.ip, self.port))
            print(f"Connected to {self.ip}:{self.port}")

            while True:
                recv_data = service_socket.recv(BUFFER_SIZE).decode()
                if not recv_data:
                    print("Disconnected from service.")
                    break
                print("Service says:", recv_data)

                send = input("You: ")
                if send.lower() == "":
                    break
                service_socket.sendall(send.encode())
