[🇮🇷 فارسی](/01-port_scanner/docs/fa/03-cybersecurity/07-input-validation-and-injection-attacks.md)

# Session 07 — Input Validation and Injection Attacks

# Introduction

So far on our learning journey, we have become familiar with important security concepts:

- What cybersecurity is
- Who attackers are
- What a vulnerability is
- How the security lifecycle works
- What threat modeling is
- How authentication and authorization work

But now we reach one of the most dangerous parts of software security.

Where many of the biggest breaches in history began.

---

# A Golden Rule

In cybersecurity, there is a very important rule:

> Treat every user input as dangerous.

---

# Why?

Because you do not know who is sending that input.

It might be:

- A regular user
- A bot
- A hacker
- Malware

---

# A Simple Example

Suppose your program receives a name from the user:

```python
name = input("Name: ")
```

At first glance, everything looks normal.

---

But a hacker can enter something completely different:

```text
'; DROP TABLE users; --
```

Or

```text
../../../etc/passwd
```

Or

```text
&& shutdown /s
```

---

# What Is Input Validation?

Input Validation means:

> Checking the input before using it

---

Goal:

The program should only accept valid data.

---

# Example

Suppose we receive an IP.

A correct input:

```text
192.168.1.1
```

---

An invalid input:

```text
hello
```

Or:

```text
999.999.999.999
```

---

They must be checked before use.

---

# Why Does Our Port Scanner Have Validation?

For exactly this reason.

In the file:

```text
validator.py
```

we check:

- The IP is valid
- The port is valid
- The Timeout is valid
- The Workers are valid

---

# What Happens If We Don't Validate?

It is possible that:

- The program crashes
- It produces incorrect output
- It becomes vulnerable

---

# What Is Injection?

Injection means:

> Injecting a malicious command or data into the program

---

The attacker tries to make the program:

Instead of executing the original command,

execute the attacker's command.

---

# The Most Famous Type

# SQL Injection

---

Suppose the program builds this query:

```sql
SELECT * FROM users
WHERE username='admin'
```

---

The programmer makes a mistake and inserts the user input directly into SQL.

---

The user enters:

```text
' OR 1=1 --
```

---

The result:

```sql
SELECT * FROM users
WHERE username='' OR 1=1 --
```

---

The expression:

```sql
1=1
```

is always true.

As a result, the attacker can view all the information.

---

# The Danger of SQL Injection

The attacker might:

- Read user information
- Extract passwords
- Delete data
- Destroy the database

---

# The Solution

Use:

```text
Parameterized Queries
```

or

```text
Prepared Statements
```

---

Example:

```python
cursor.execute(
    "SELECT * FROM users WHERE id = ?",
    (user_id,)
)
```

---

# Command Injection

Another type of Injection.

---

Suppose the program runs an operating system command.

Example:

```python
import os

os.system("ping " + ip)
```

---

Normal input:

```text
8.8.8.8
```

---

But the attacker enters:

```text
8.8.8.8 && shutdown /s
```

---

Result:

```text
ping 8.8.8.8
shutdown /s
```

---

The program unintentionally executes the attacker's command.

---

# The Danger of Command Injection

The attacker might:

- Delete files
- Install programs
- Take control of the system

---

# Path Traversal

Another common attack.

---

Suppose we receive a file:

```text
report.txt
```

---

The program:

```python
open("files/" + filename)
```

---

A normal user:

```text
report.txt
```

---

But the attacker:

```text
../../../secret.txt
```

---

Result:

The program opens files outside the allowed folder.

---

# What Is XSS?

Short for:

```text
Cross Site Scripting
```

---

This attack mostly occurs in web applications.

---

Example:

The user enters:

```html
<script>
alert("Hacked")
</script>
```

---

If the site displays this code without checking:

The attacker's script runs in the victim's browser.

---

# Why Is Our Port Scanner Less Exposed to XSS?

Because:

- It is not a web application
- It does not generate HTML

But if we build a web version later, we must be careful.

---

# What Is a Whitelist?

The best validation method.

---

Instead of saying:

What is forbidden

We say:

What is allowed.

---

Example

For a port:

Only:

```text
1 to 65535
```

---

For an IP:

Only:

```text
A valid IPv4
```

---

This method is much more secure.

---

# What Is a Blacklist?

A weaker method.

---

Example:

```text
These characters are forbidden:
&
|
;
$
```

---

Problem:

There is always a way to bypass it.

---

# Why Is a Whitelist Better?

Because it only accepts known items.

---

# An Important Principle

Never trust input.

Even if:

- It came from the site's form
- It came from the API
- It came from a file
- It came from the administrator user

---

# An Example in the Port Scanner Project

We receive from the user:

```text
IP Address
Start Port
End Port
Timeout
Workers
```

---

All of these must be validated.

---

If we do not do this:

It is possible that:

- The program crashes
- System resources are consumed
- Incorrect output is produced

---

# Secure by Default

One of the important principles of security.

---

Meaning:

> The default state must be secure.

---

Example:

If the input was invalid:

```text
Reject
```

Not:

```text
Guess
```

---

# Summary

In this session, we learned:

- What Input Validation is
- Why every input is dangerous
- What Injection is
- What SQL Injection is
- What Command Injection is
- What Path Traversal is
- What XSS is
- What a Whitelist is
- What a Blacklist is
- Why validation is important in the Port Scanner

---

# What Will We Learn in the Next Session?

In the eighth session, we enter one of the most important defensive topics:

# Logging and Monitoring

We will learn:

- What a log is
- Why recording events is important
- What SIEM is
- How monitoring works
- What Incident Detection is
- Why hackers usually try to delete logs first

We will also see exactly what role the Logging feature we implemented in the Port Scanner project plays in software security.
