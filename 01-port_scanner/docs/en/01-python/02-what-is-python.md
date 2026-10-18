[🇮🇷 فارسی](/01-port_scanner/docs/fa/01-python/02-what-is-python.md)

# Session 02 — What Is Python?

## Introduction

In the previous session, we learned that programming means writing instructions that the computer can execute.

But there is an important question:

If we want to give instructions to a computer, in what language should we write them?

This is where programming languages come into play.

---

## What Is a Programming Language?

Just as humans speak different languages:

- Persian
- English
- Arabic
- Turkish

computers also need a language to understand instructions.

These languages are called **programming languages**.

---

## What Is Python?

> **Python** is an open-source, powerful, and popular programming language.

This language was introduced in 1991 by:

> Guido van Rossum

The main goal of Python was:

> Programming should be simple and understandable.

---

## The First Python Program

Create the following file:

```python
hello.py
```

File content:

```python
print("Hello World")
```

Running the program:

```bash
python hello.py
```

Output:

```text
Hello World
```

---

## Why Did We Use Python for the Port Scanner Project?

There are several important reasons:

### 1. Simplicity

Python code is very readable.

Example:

```python
socket.connect(("127.0.0.1", 80))
```

Even without much knowledge, one can guess that this code is connecting to an IP and a port.

---

### 2. Ready-Made Libraries

Python has powerful libraries.

For example:

```python
socket
```

for network communication.

```python
ipaddress
```

for IP validation.

```python
json
```

for storing output.

---

### 3. Development Speed

With Python, useful tools can be developed in a short time.

Our Port Scanner project has also been implemented in this language.

---

## How This Lesson Connects to the Project

So far, we have understood:

- What Python is.
- Why it is popular.
- How it is executed.
- Why it is suitable for building security tools.

In the upcoming sessions, we will become familiar with the concepts we used in building the Port Scanner.

---

## Summary

✅ Python is a simple and powerful programming language.

✅ Python is used in various fields, including cybersecurity.

✅ Our Port Scanner project is written in Python.

✅ Python files have the `.py` extension.

---

## Exercise

Create a file named:

```text
about_me.py
```

and display three different lines of text using `print()`.
