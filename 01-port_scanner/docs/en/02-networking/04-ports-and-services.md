[🇮🇷 فارسی](/01-port_scanner/docs/fa/02-networking/04-ports-and-services.md)

# Session 04 — What Is a Port?

# Introduction

So far, we have learned:

✅ What a network is

✅ What an IP is

✅ What TCP is

✅ What UDP is

But one important question still remains:

---

If a computer has only one IP, how can it simultaneously:

- Run a website
- Receive email
- Have DNS
- Have FTP
- Have SSH

?

---

The answer:

```text
Port
```

---

# What Is a Port?

A port can be imagined as:

```text
The door of a building
```

---

Suppose the building's address is:

```text
192.168.1.10
```

---

This building has only one address.

But it has several rooms.

---

For example:

```text
Room 1
```

---

```text
Room 2
```

---

```text
Room 3
```

---

Each room does a different job.

---

In a network, too:

```text
IP = building
```

and

```text
Port = room
```

---

# A Real Example

Suppose:

```text
192.168.1.10
```

is a server.

---

On this same server:

- A website runs
- SSH runs
- DNS runs

---

All on one IP.

---

But on different ports.

---

Example:

```text
192.168.1.10:80
```

Website

---

```text
192.168.1.10:22
```

SSH

---

```text
192.168.1.10:53
```

DNS

---

# The IP and Port Display Format

Usually it is written like this:

```text
IP:PORT
```

---

Example:

```text
192.168.1.10:80
```

---

Or:

```text
8.8.8.8:53
```

---

# How Many Ports Are There?

Ports range from:

```text
0
```

to:

```text
65535
```

---

That means:

```text
65536
```

different ports.

---

# Why Does a Full Scan Take So Long?

When Nmap or a Port Scanner runs:

---

We might want to check:

```text
1 to 65535
```

---

That means:

```text
65535 different connections
```

---

That is why a full scan can take a long time.

---

# Port Categories

# Well-Known Ports

From:

```text
0 - 1023
```

---

Famous Internet services.

---

# Registered Ports

From:

```text
1024 - 49151
```

---

For various software and services.

---

# Dynamic Ports

From:

```text
49152 - 65535
```

---

Usually temporary.

---

# The Most Famous Ports in the World

# SSH

```text
22
```

---

Secure connection to a server

---

# FTP

```text
21
```

---

File transfer

---

# SMTP

```text
25
```

---

Sending email

---

# DNS

```text
53
```

---

Converting a domain name to an IP

---

# HTTP

```text
80
```

---

Website

---

# POP3

```text
110
```

---

Receiving email

---

# HTTPS

```text
443
```

---

Secure web

---

# SMB

```text
445
```

---

Windows file sharing

---

# RDP

```text
3389
```

---

Windows Remote Desktop

---

# Why Are Ports Important to Hackers?

Suppose we have a server.

---

If we only know the IP:

```text
192.168.1.50
```

---

We still do not know:

- Does it have a web server?
- Does it have SSH?
- Does it have a database?

---

But if we find the ports:

```text
22
80
443
3306
```

---

We realize:

- SSH is active
- HTTP is active
- HTTPS is active
- MySQL is active

---

That is why:

```text
Port Scanning
```

is the first step of many penetration tests.

---

# What Exactly Does Our Port Scanner Do?

Example:

```bash
python -m src.cli 127.0.0.1 1 1000
```

---

The scanner checks ports:

```text
1 to 1000
```

---

For example:

```text
53
135
445
```

---

If it receives a response:

```text
OPEN
```

it displays.

---

# What Is an Open Port?

It means:

A service is running on that port.

---

Example:

```text
80 OPEN
```

---

Usually means:

```text
Web Server
```

is running.

---

# What Is a Closed Port?

It means:

No service is listening.

---

Example:

```text
8080 CLOSED
```

---

It means no program is active on this port.

---

# What Is Listening?

When a program is ready to receive connections, we say:

```text
Listening
```

---

Example:

```text
Web Server Listening On Port 80
```

---

It means:

The server is waiting for users to connect.

---

# What Is a Socket?

In network programming:

Connecting to ports is done with:

```python
socket
```

---

In our project:

```python
socket.connect()
```

---

tries to connect to:

```text
IP + Port
```

---

# A Real Example

Suppose:

```text
127.0.0.1:80
```

---

The scanner tries to connect.

---

If it succeeds:

```text
OPEN
```

---

If it fails:

```text
CLOSED
```

---

# What Is Service Detection?

Later, we added the following feature:

```text
Service Detection
```

---

Example:

Instead of:

```text
80
```

we display:

```text
http
```

---

And instead of:

```text
443
```

we display:

```text
https
```

---

# What Is Banner Grabbing?

After finding a port:

Sometimes we can get more information.

---

For example:

```text
Apache/2.4.58
```

---

Or:

```text
OpenSSH_9.7
```

---

This information is called:

```text
Banner
```

---

We have also added this feature to the project.

---

# A Real Output from the Project

Sample:

```text
PORT     STATUS   SERVICE       BANNER
--------------------------------------------------
53       OPEN     domain        -
135      OPEN     epmap         -
445      OPEN     microsoft-ds  -
```

---

The same thing you recently received from the project.

---

# Why Did Nmap Become Famous?

Because it does not just say:

```text
Port Open
```

---

But also:

- Detects the service
- Detects the service version
- Guesses the operating system
- Runs scripts
- Finds vulnerabilities

---

But all of these features start from the same point:

```text
Port Scanning
```

---

# What We Learned Today

✅ What a Port is

✅ The difference between IP and Port

✅ Well-Known Ports

✅ Open Port

✅ Closed Port

✅ Listening

✅ Socket

✅ Service Detection

✅ Banner Grabbing

✅ How Port relates directly to the Port Scanner project

---

# Next Session

File:

```text
05-client-server-model.md
```

Topic:

**The Client / Server Model**

In the next session, we will learn:

- What exactly a client is
- What exactly a server is
- How a browser communicates with a website
- What role the Port Scanner plays in this model
- Why an open port means a Server is Listening

