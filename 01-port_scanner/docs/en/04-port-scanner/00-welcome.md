[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/00-welcome.md)

# Chapter Four: A Complete Walkthrough of the Port Scanner Project

# Introduction

Congratulations!

If you have followed the course up to this point, you have now learned all the prerequisites needed to build a real port scanner.

In the past three chapters, we became familiar with the most important required concepts:

- Programming with Python
- Networking concepts
- Cybersecurity concepts

Now it is time to put all this knowledge together and see how a real tool is built.

---

# What Have We Learned So Far?

## Chapter One: Python

In the Python chapter, we learned:

- Variables
- Data types
- Conditions
- Loops
- Functions
- Modules
- Classes
- Exception Handling
- Working with JSON files
- Working with CSV files

And finally, we learned how these concepts are used in a real project.

---

## Chapter Two: Networking

In the networking chapter, we learned:

- What a network is
- What an IP is
- What a Port is
- What TCP is
- What UDP is
- What a Socket is
- What DNS is
- What a Service is
- What HTTP is
- What HTTPS is

And finally, we understood exactly which part of the network the port scanner operates in.

---

## Chapter Three: Cyber Security

In the security chapter, we learned:

- CIA Triad
- Threat
- Vulnerability
- Risk
- Attack Surface
- Security Lifecycle
- Footprinting
- Reconnaissance
- Enumeration
- Vulnerability Assessment
- Penetration Testing

And we understood what role the port scanner plays in the penetration testing cycle.

---

# What Is the Goal of This Chapter?

The goal of this chapter is not just to read code.

The goal is to:

- Be able to understand all the project's code
- Understand the reason for each file's existence
- Understand the reason for each function's existence
- Understand the reason for each line of code's existence
- Be able to extend the project
- Be able to rewrite the project
- Be able to create a similar project from scratch

---

# Do We Only Review the Main Code?

No.

This chapter is divided into two main parts:

## Part One

Reviewing the project's main code

```text
src/
```

In this part, we will learn:

- How the project's architecture was designed
- What each file's responsibility is
- What each function does
- What each class is used for

---

## Part Two

Reviewing the project's tests

```text
tests/
```

In this part, we will learn:

- What a test is
- Why we write tests
- How to write tests
- What a Mock is
- What Monkeypatch is
- How Pytest works

And most importantly:

How to write professional tests for our own projects.

---

# Why Is This the Most Important Chapter of the Course?

Because in this chapter, all the concepts from the past three chapters come together.

Here you will see how:

```text
Python + Networking + Security
```

form a real tool.

---

# What Abilities Will You Have After Finishing This Chapter?

If you study this entire chapter completely, you will be able to:

- Build your own port scanner
- Add new features
- Implement Banner Grabbing
- Add different exports
- Add Logging
- Write tests for the project
- Refactor the project
- Produce similar security tools

---

# Roadmap for the Rest of the Chapter

First, we enter the following folder:

```text
src/
```

And we review the files in order:

```text
__init__.py
models.py
validator.py
services.py
banner.py
scanner.py
results.py
exporter.py
csv_exporter.py
formatter.py
logger.py
cli.py
```

Then we will enter the folder:

```text
tests/
```

And we will review all the tests line by line.

---

# Summary

In the past three chapters, we learned:

- How to program
- How networking works
- How cybersecurity works

Now we have entered the most important part of the course:

A complete walkthrough of the Port Scanner project.

From the next session, we begin reviewing the file:

```python
src/__init__.py
```
