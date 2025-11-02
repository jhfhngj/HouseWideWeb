# House Wide Web
This is HouseWideWeb (HWW), a decentralized network system.

## How do I use it?
To get started with HWW, follow these instructions. (By the way, a server can just be a computer because HWW is lightweight.)

Run the DNS, `hww.dns`, if you've configured it, and put it on a server or computer.

Next, you'll want to grab the server framework.

It's `hww.server`, so you'll want to grab it, import it in your code: `import hww.server`. Next, build on it using the functions.

After you set up the server, run it on a server or computer.

Also, before you can use it, you have to send a `reg` request using the client.
 
It would be something like `reg <domain>`. Luckily, there are no TLDs, so you can go wild with URLS!

You're done!
If you want, you can make a HWW client by building on `hww.client`, and then that'll be that.

Now, to actually connect to your HWW server, use the client to connect to the DNS, then send a `get` request with the server's HWW domain, such as `ilove.manypieces.ofpie`. The full request would be something like `get ilove.manypieces.ofpie`. It will return an IP like `10.0.0.15`, then update your code to take that IP and connect to it.

After that, run your client with the HWW address, such as `hww://computerstore.com`.