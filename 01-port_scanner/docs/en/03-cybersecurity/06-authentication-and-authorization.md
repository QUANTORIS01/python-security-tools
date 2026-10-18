[🇮🇷 فارسی](/01-port_scanner/docs/fa/03-cybersecurity/06-authentication-and-authorization.md)

# Session 06 — Authentication and Authorization

# Introduction

So far on our learning journey, we have become familiar with important concepts:

- What cybersecurity is
- Who attackers are
- What a vulnerability is
- How the security lifecycle works
- What threat modeling is

Now we reach one of the most important parts of software security.

Almost every application you see today uses these concepts:

- Instagram
- Telegram
- Gmail
- GitHub
- Digikala
- Amazon
- Online banks

If this part is implemented incorrectly, the entire system may be compromised.

---

# What Is Authentication?

Authentication means:

> Proving identity

Or, in simple terms:

> "Who are you, really?"

---

# A Real-World Example

Suppose you walk into a bank.

The bank clerk asks:

- Do you have your national ID?
- What is your account number?

What is the goal?

Proving your identity.

This is Authentication.

---

# An Internet Example

When logging in to Gmail:

```text
Username
Password
```

Google checks:

Are you really the owner of this account?

If yes:

It grants access.

---

# What Is Authorization?

Authorization means:

> Determining the level of access

Or:

> After we know who you are, what are you allowed to do?

---

# A Real-World Example

You have entered a company.

Authentication:

It is verified that you are an employee.

Authorization:

It is determined which rooms you are allowed to enter.

---

# The Main Difference

Authentication:

```text
Who are you?
```

Authorization:

```text
What can you do?
```

---

# A Simple Example

Suppose we have entered the site's admin panel.

First user:

```text
admin
```

Second user:

```text
user
```

Both have logged in.

But only the administrator can:

- Delete users
- Change settings
- View reports

---

# So...

Authentication:

Logging in to the system

Authorization:

The level of access inside the system

---

# How Does the Login Process Work?

Usually like this:

```text
User
 |
 v
Username + Password
 |
 v
Server
 |
 v
Database
 |
 v
Success / Fail
```

---

# How Are Passwords Stored?

One of the biggest mistakes of beginner programmers:

Storing passwords in plain text.

A dangerous example:

```text
password123
```

in the database.

---

# Why Is It Dangerous?

If the database leaks:

All passwords are exposed.

---

# What Is the Solution?

Hash

---

# What Is a Hash?

A Hash is a one-way function.

Example:

```text
password123
```

is converted to:

```text
482c811da5d5b4bc6d497ffa98491e38
```

---

# The Property of a Hash

You can do:

```text
Password
→ Hash
```

But the reverse is almost impossible.

---

# Common Algorithms

Old:

```text
MD5
SHA1
```

are not recommended today.

---

# Suitable Algorithms

```text
bcrypt
scrypt
Argon2
```

---

# What Is a Session?

After login, the user is not supposed to enter their password every second.

So the server creates something called a Session.

---

# Example

```text
User Login
```

↓

```text
Session Created
```

↓

```text
Session ID
```

↓

```text
Browser
```

The user does not log in again as long as the Session is valid.

---

# What Is a Cookie?

Usually, the Session ID is stored inside a Cookie.

---

Example:

```text
session_id=abc123xyz
```

The browser stores this value.

---

# Every Subsequent Request

```text
GET /profile
```

is sent along with the Session.

The server recognizes:

This is the same user as before.

---

# What Is JWT?

JWT stands for:

```text
JSON Web Token
```

---

It is used a lot in modern systems.

For example:

- APIs
- Microservices
- Mobile Apps

---

# The Structure of a JWT

It has three parts:

```text
Header
Payload
Signature
```

---

Example:

```text
xxxxx.yyyyy.zzzzz
```

---

# What Is the Payload?

The user's information:

For example:

```json
{
  "id": 5,
  "role": "admin"
}
```

---

# What Is the Signature?

A signature

to prevent tampering with the information.

---

# The Brute Force Attack

One of the most famous Login attacks.

---

The hacker tries:

```text
123456
12345678
password
admin
qwerty
```

and thousands of other passwords.

---

# How to Counter It

- Limit the number of attempts
- Captcha
- MFA
- Temporary account lockout

---

# What Is MFA?

Multi-Factor Authentication

or:

Multi-step authentication

---

Example:

1. Password
2. SMS code

---

Or:

1. Password
2. Google Authenticator

---

# Why Is MFA Important?

Even if the password leaks:

There is still a second step.

---

# Principle of Least Privilege

One of the most important rules of security.

---

Meaning:

> Each user should have only as much access as they need.

---

Wrong:

```text
Everyone = Administrator
```

---

Right:

```text
Everyone has only the access they need.
```

---

# An Example in the Port Scanner

Suppose we have built a web version.

A regular user:

- Runs scans

---

An administrator:

- Views logs
- Deletes users
- System settings

---

This is Authorization.

---

# A Common Mistake by Programmers

Checking the level of access only in the Front-End.

---

Example:

They hide the delete button.

But the API is still active.

---

The hacker calls the API directly.

---

The level of access must be checked on the server.

Always.

---

# Summary

In this session, we learned:

- What Authentication is
- What Authorization is
- What the difference between them is
- How Login works
- What a Hash is
- What a Session is
- What a Cookie is
- What JWT is
- What MFA is
- What Brute Force is
- What the Principle of Least Privilege is

---

# What Will We Learn in the Next Session?

In the seventh session, we enter one of the most dangerous and famous attacks in the security world:

# Input Validation and Injection Attacks

We will learn:

- Why every user input is dangerous
- What SQL Injection is
- What Command Injection is
- What Path Traversal is
- How to secure inputs

This topic is directly related to our Port Scanner project as well, because we also receive inputs such as IP, port, and settings from the user.
