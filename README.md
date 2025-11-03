# House Wide Web
This is HouseWideWeb (HWW), a decentralized network system.

## How do I use it?
To get started with HWW, follow these instructions. (By the way, a server can just be a computer because HWW is lightweight.)

Use the DNS in a project, `hww.dns`, make a python app to run it, and put it on a server or computer.

For example, you can use
```
from hww.dns import DNSRegistryServer

server = DNSRegistryServer()
server.start()
```

Next, you'll want to grab the server framework.

It's `hww.HWWServer`, so you'll want to grab it, import it in your code: `import hww.HWWServer`. Next, build on it using the functions.

After you set up the server, run it on a server or computer.

Also, before you can use it, you have to send a `reg` request using the client.
 
It would be something like `reg <domain>`. Luckily, there are no TLDs, so you can go wild with URLS!

For example, if you're a lazybones like me and want an example, here's one for the server.

```
from hww import HWWServer

server = HWWServer()
server.start()
```

You're almost done!
If you want, you can make a HWW client by using `hww.DNSClient` and `hww.ServiceConnector`, and then that'll be that.

If you want to know how to use the client framework, you can use this as a help tool:

```
from hww import DNSClient, ServiceConnector

dns = DNSClient()
status, ip_port = dns.send_request("get", "hww://example.com")

if "100 OK" in status and ip_port:
    ip, port = ip_port.split(":")
    connector = ServiceConnector(ip, int(port))
    connector.interact()
else:
    print("Failed to resolve domain.")
```

Now, to actually connect to your HWW server, use the client to connect to the DNS, then send a `get` request with the server's HWW domain, such as `ilove.manypieces.ofpie`. The full request would be something like `get ilove.manypieces.ofpie`. It will return an IP like `10.0.0.15`, then update your code to take that IP and connect to it.

After that, run your client with the HWW address, such as `hww://computerstore.com`.