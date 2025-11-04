# 🏠 HouseWideWeb (HWW)
Welcome to HouseWideWeb, a decentralized network system designed to be lightweight, flexible, and fun to use. Whether you're building a local service or a distributed app, HWW gives you the tools to register, resolve, and connect — all without the baggage of traditional DNS.

## 🚀 Getting Started

Here's how you can get started with HouseWideWeb easily!

### 1. Run the DNS Registry Server

This is the backbone of HWW — a simple DNS registry that maps domains to IP addresses and ports.

```
from hww.dns import DNSRegistryServer

server = DNSRegistryServer()
server.start()
```

Run this on any computer or server. It listens for `reg ` and `get` requests to register and resolve HWW domains.

### 2. Build Your HWW Server


Use the HWW server framework to create your own service.
```
from hww import HWWServer

server = HWWServer()
server.start()
```
But guess what? That's just a starter blank server.

You can extend `HWWServer` with custom logic to handle incoming connections. It's lightweight, so any computer can be a server.

To do so, use this as an example. This is an echo server.

```
from hww import *

def handler(input, conn, addr, data):
    send = input.encode() + data
    conn.sendall(send)

# Start the server
hww = HWWServer()
hww.start(handler, "")
```

### 3. Register Your Domain

Before clients can find your server, you need to register it with the DNS registry.

Send a registration request like this using the later shown client base or a custom one:

```
reg ilove.manypieces.ofpie
```

No TLDs required — go wild with names!

### 4. Connect with the HWW Client

Use the client framework to resolve domains and interact with services.

```
from hww import DNSClient, ServiceConnector

dns = DNSClient()
status, ip_port = dns.send_request("get", "hww://example.com")

if "100 OK" in status and ip and port:
    connector = ServiceConnector(ip, int(port))
    connector.interact()
else:
    print("Failed to resolve domain.")
```

### 🧠 How It Works

- DNSRegistryServer: Accepts reg <domain> to register and get <domain> to resolve.

- HWWServer: Listens for incoming connections and handles service logic.

- DNSClient: Sends requests to the DNS server.

- ServiceConnector: Connects to resolved services and enables interaction.

### 🧪 Example Flow

1. Start your DNS server.

2. Start your HWW service.

3. Register your domain with the DNS server.

4. Use the client to resolve and connect to your service.

Example domain: hww://computerstore.com 
Example registration: reg computerstore.com 
Example resolution: get computerstore.com
