[🇮🇷 فارسی](/01-port_scanner/docs/fa/02-networking/01-what-is-a-network.md)

# Session 01 — What Is a Network?

# Before We Begin

So far on this journey, we have learned how to write programs.

But a Port Scanner is not just a Python program.

A Port Scanner is, in fact, a network tool.

That is why, before we dive into security concepts and analyzing the project's code, we need to understand networks.

In this chapter, we are not trying to become network engineers.

The goal is to learn enough about networking that we can:

- Fully understand the Port Scanner.
- Know exactly what the scanner is doing.
- Build similar security tools.
- Analyze the behavior of services and ports.

---

# What Is a Network, Really?

In simple terms:

A network means that several devices can communicate with each other.

Example:

- A laptop
- A mobile phone
- A server
- A printer
- A CCTV camera

If they can exchange data, a network has been formed.

---

# A Real-Life Example

Suppose two people are in two different rooms.

If they have no way to communicate:

❌ They cannot talk to each other.

But if there is a telephone between them:

✅ They can communicate.

A network does exactly this for computers.

---

# Why Was the Network Invented?

Before networks, every computer was an isolated island.

For example:

Computer A

and

Computer B

had no way to exchange information.

If you wanted to transfer a file, you had to move:

- A floppy disk
- A CD
- A DVD
- A USB flash drive

Networks solved this problem.

---

# A Few Examples of Networks Around Us

---

## The Internet

The largest network in the world.

Billions of devices are connected to each other.

## A Home Network

For example:

- A laptop
- A phone
- A TV
- A modem

are all on the same network.

---

## A Company Network

For example:

- An accounting server
- Employee systems
- Cameras
- Printers

are all connected to each other.

---

# What Travels Across a Network?

Information.

Or, in other words:

```text
Data
```

For example:

- Text
- Images
- Video
- Audio
- Files
- Messages

All of these ultimately become data.

---

# How Does the Internet Work?

Suppose you type in your browser:

```text
google.com
```

The browser sends a request.

The request passes through:

- Your computer
- The modem
- Your internet service provider
- Several routers
- Google's server

The response comes back.

And the page is displayed.

This entire path is part of the network.

---

# Devices You Will Find in a Network

There are a few important devices you will always see.

---

# Client

The requester.

Example:

- A browser
- A phone
- A laptop

---

Example:

When you visit Google:

```text
Laptop --> Google
```

The laptop plays the role of the Client.

---

# Server

The service provider.

Example:

- Google's server
- GitHub's server
- Instagram's server

---

A Server waits for requests.

When a request arrives, it responds.

---

# A Real Example

Suppose you visit GitHub.

```text
Browser ----> GitHub Server
```

The browser is the:

Client

GitHub is the:

Server

---

# Why Is This Important for the Port Scanner?

Because in our project:

We connect to various servers.

For example:

```python
socket.connect(("192.168.1.10", 80))
```

At this moment:

Our port scanner is the Client.

And the target device is the Server.

---

# Is a Network Possible Without Addressing?

No.

Suppose you want to send a letter to a friend.

If you have no address:

❌ The letter will not reach its destination.

Computers have exactly the same problem.

That is why something called:

```text
IP Address
```

was created.

---

# What Is an IP?

For now, simply:

An IP is the address of a device on a network.

Like:

```text
192.168.1.10
```

or

```text
8.8.8.8
```

---

We will examine IP in full in the upcoming sessions.

---

# Is a Network Possible Without Rules?

Suppose:

I speak Persian.

You speak German.

Communication becomes difficult.

Computers also need a common language.

These common languages are called:

```text
Protocol
```

---

Example:

- HTTP
- HTTPS
- FTP
- SSH
- DNS

---

We will learn each of them later.

---

# What Exactly Does a Port Scanner Do on a Network?

A Port Scanner goes to the target device.

And asks the question:

```text
Is this port open?
```

For example:

```text
80
```

If it receives a response:

The port is open.

If it does not receive a response:

The port is closed.

---

Our entire project is built on this concept.

But before understanding Port, we need to:

Learn IP.

---

# What We Learned Today

✅ What a network is

✅ What a Client is

✅ What a Server is

✅ What data is

✅ How the Internet works

✅ Why we need IP

✅ Why we need Protocol

✅ What role the Port Scanner plays in a network

---

# Next Session

File:

```text
02-ip-address.md
```

Topic:

What Is an IP Address and How Does It Work?

In the next session, we will learn:

- What an IP is
- What IPv4 is
- What IPv6 is
- What a Public IP is
- What a Private IP is
- Why every device needs an IP
