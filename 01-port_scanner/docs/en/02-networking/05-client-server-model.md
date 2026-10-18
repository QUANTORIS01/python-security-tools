[🇮🇷 فارسی](/01-port_scanner/docs/fa/02-networking/05-client-server-model.md)

# Session 05 — What Is the Client/Server Model?

# Introduction

So far, we have learned:

✅ What a network is

✅ What an IP is

✅ What TCP is

✅ What UDP is

✅ What a Port is

---

Now we reach the most important concept on which the entire Internet is built:

```text
Client / Server Model
```

---

Almost everything you do on the Internet is based on this model.

---

For example:

- Opening a website
- Watching a video on YouTube
- Using Instagram
- Sending email
- Downloading a file
- Running a Port Scanner

are all based on the Client / Server model.

---

# What Is a Client?

A Client means:

```text
The requester
```

---

The system that sends requests.

---

Example:

When you open your browser:

```text
Google Chrome
```

or

```text
Firefox
```

---

The browser plays the role of:

```text
Client
```

---

# What Is a Server?

A Server means:

```text
The responder
```

---

The system that waits for requests and responds to them.

---

Example:

Google's server.

---

When you visit:

```text
https://google.com
```

---

Google's server receives the request and responds.

---

# A Real Example

Suppose you have entered a restaurant.

---

You say:

```text
One pizza, please
```

---

The chef responds:

```text
The pizza is ready
```

---

In this example:

```text
You = Client
```

---

```text
The chef = Server
```

---

# A Simple Communication Diagram

```text
Client  ---------- Request ----------> Server

Client <--------- Response ---------- Server
```

---

Almost the same thing happens across the entire Internet.

---

# A Website Example

When you open the following address:

```text
https://google.com
```

---

The browser sends a request:

```text
GET /
```

---

The server responds:

```html
<html>
...
</html>
```

---

The browser displays the page.

---

# Request and Response

Two very important concepts:

---

# Request

Request

---

# Response

Response

---

Example:

```text
Request:
Give Me Homepage
```

---

```text
Response:
Here Is Homepage
```

---

# Is a Server Always On?

Usually, yes.

---

A server must be ready at all times.

---

That is why it:

```text
Listening
```

---

Meaning it is waiting for new connections.

---

# What Does Listening Mean?

Suppose the server is running on port 80.

---

The server says:

```text
I am waiting for requests on Port 80
```

---

This state is called:

```text
Listening
```

---

# How Listening Relates to the Port Scanner

The port scanner checks exactly this.

---

When this command runs:

```bash
python -m src.cli 127.0.0.1 1 1000
```

---

The scanner asks:

```text
Is anyone Listening on this port?
```

---

If the answer is positive:

```text
OPEN
```

---

If the answer is negative:

```text
CLOSED
```

---

# What Role Does the Port Scanner Play in This Model?

A Port Scanner is a Client.

---

Very important:

The port scanner:

```text
Is not a Server
```

---

Rather:

```text
It is a Client
```

---

Because it sends connection requests.

---

# A Real Example

Suppose:

```text
192.168.1.100
```

is a server.

---

And it listens on:

```text
80
```

---

The port scanner tries:

```text
Connect To 192.168.1.100:80
```

---

If it succeeds:

```text
OPEN
```

---

# Behind the Scenes of `connect()`

In our project:

```python
socket.connect()
```

---

plays the role of the Client.

---

And tries to connect to the Server.

---

# How Many Clients Can Connect to One Server?

Yes.

---

Example:

Google's server.

---

There might be:

```text
Millions of Clients
```

connected at the same time.

---

# How Many Servers Can Run on One System?

Yes.

---

Example:

```text
Port 80
HTTP
```

---

```text
Port 22
SSH
```

---

```text
Port 443
HTTPS
```

---

All on one IP.

---

But on different ports.

---

# Why Do Servers Have Ports?

So they can tell:

Which service a request belongs to.

---

Example:

```text
192.168.1.10:80
```

---

Website

---

And

```text
192.168.1.10:22
```

---

SSH

---

Both are on the same IP.

---

But on different ports.

---

# Banner Grabbing in the Client/Server Model

When the port scanner retrieves a banner:

---

First:

```text
Client Connects
```

---

Then:

```text
Server Sends Banner
```

---

Example:

```text
OpenSSH_9.7
```

---

Or:

```text
Apache/2.4.58
```

---

This information is sent from the Server side.

---

# Service Detection in This Model

After connecting:

---

The port:

```text
80
```

---

is mapped to the service:

```text
HTTP
```

---

And

```text
22
```

---

to:

```text
SSH
```

---

This is exactly the Service Detection feature.

---

# The Client / Server Model in the Real World

Almost everything:

---

# Browser

Client

---

# Website

Server

---

# Email

Client ↔ Server

---

# FTP

Client ↔ Server

---

# SSH

Client ↔ Server

---

# Port Scanner

Client ↔ Server

---

# Why Is This Session Important?

Because now we understand:

What the port scanner is doing.

---

The scanner:

```text
Is not hacking
```

---

Rather:

```text
It is trying to establish a connection
```

---

And it draws conclusions from the server's response or lack of response.

---

# What We Learned Today

✅ What a Client is

✅ What a Server is

✅ What a Request is

✅ What a Response is

✅ What Listening is

✅ How the Port Scanner relates to the Client/Server model

✅ The role of `socket.connect()`

✅ How Banner Grabbing relates to the Server

✅ How Service Detection relates to the Server

---

# Next Session

File:

```text
06-dns-and-domain-names.md
```

Topic:

**DNS and Domain Names**

In the next session, we will learn:

- What a Domain is
- What DNS is
- Why we use domain names instead of IPs
- How `google.com` is converted to an IP
- How the Port Scanner can scan a domain

