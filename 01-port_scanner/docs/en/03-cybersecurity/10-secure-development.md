[🇮🇷 فارسی](/01-port_scanner/docs/fa/03-cybersecurity/10-secure-development.md)

# Session 10 — Secure Development

# Introduction

Congratulations!

We have now reached the last session of the cybersecurity chapter.

So far, we have become familiar with important topics:

- What cybersecurity is
- Who attackers are
- What a vulnerability is
- The security lifecycle
- Threat modeling
- Authentication and authorization
- Injection attacks
- Input validation
- Logging and Monitoring
- Defense in Depth

But one important question still remains:

> How do we write a program from day one that is as secure as possible?

The answer to this question is:

# Secure Development

---

# What Is Secure Development?

Secure Development means:

> Developing software with security in mind from the very beginning

---

Many people first build the program and then later think about security.

But in the real world, this approach is dangerous.

---

# Two Different Approaches

The wrong approach:

```text
Build
↓
Deploy
↓
Security
```

---

The professional approach:

```text
Design
↓
Build
↓
Security
↓
Test
↓
Deploy
```

---

In the professional approach, security exists from the very beginning.

---

# What Is Secure Coding?

Secure Coding means:

> Writing code in a way that reduces the likelihood of it being exploited.

---

Example

Weak code:

```python
ip = input()
```

Using the input directly

---

Better code:

```python
ip = input()

validate_ip(ip)
```

---

This is exactly what we have done in the Port Scanner.

---

# Principle One

# Never Trust User Input

Never trust user input.

---

It does not matter:

- If it is a regular user
- If it is a system administrator
- If it is an API
- If it is a file

---

All inputs must be validated.

---

# Principle Two

# Least Privilege

We have already become familiar with this concept.

---

A program should have only the accesses it needs.

---

Wrong:

```text
Administrator Everywhere
```

---

Right:

```text
Minimum Required Access
```

---

# Principle Three

# Fail Securely

If an error occurs:

The program must remain secure.

---

A bad example:

```python
except:
    pass
```

---

The error is hidden.

---

A better example:

```python
except Exception as error:
    logger.error(error)
```

---

Recording the error

And continuing in a controlled manner

---

# Principle Four

# Keep It Simple

The more complex the system becomes:

The greater the chance of error.

---

Simpler programs:

- Are easier to test
- Are easier to maintain
- Are more secure

---

# Principle Five

# Defense in Depth

We learned this earlier.

---

Never rely on only one layer of defense.

---

Example:

```text
Validation
+
Logging
+
Authentication
+
Monitoring
```

---

All together create security.

---

# Principle Six

# Secure Defaults

The default state must be secure.

---

Example:

If the user enters an invalid value:

```text
Reject
```

---

Not:

```text
Guess
```

---

# Principle Seven

# Keep Software Updated

Many attacks succeed simply because:

The system has not been updated.

---

Example:

```text
Python
Libraries
Frameworks
Operating System
```

---

They must be updated regularly.

---

# What Is a Dependency?

The libraries that the project uses.

---

Example:

```python
pytest
```

---

is a Dependency.

---

If it has a vulnerability:

Your project will also become vulnerable.

---

# Why Should We Review Dependencies?

Sometimes hackers:

Publish infected libraries.

---

Sometimes:

An old library has a vulnerability.

---

# What Is Code Review?

Reviewing code by another person.

---

One of the most important stages of professional development.

---

Why?

Because:

All humans make mistakes.

---

A developer might miss a security issue.

But a second person finds it.

---

# What Is Security Testing?

Security testing

---

Meaning:

Checking whether the program is resistant to attacks or not.

---

Examples:

- Input Validation
- Authentication
- Authorization
- Error Handling

---

# Why Did We Write So Many Tests?

In the Port Scanner project:

We wrote more than 50 tests.

---

Reason:

To ensure the program works correctly.

---

Every time we add a new feature:

The tests check that nothing is broken.

---

# Shift Left Security

One of the modern security concepts.

---

Meaning:

Move security to the beginning of the development process.

---

The old approach:

```text
Develop
↓
Deploy
↓
Test Security
```

---

The new approach:

```text
Design
↓
Security
↓
Development
↓
Testing
```

---

This reduces cost and increases quality.

---

# Secure Development Lifecycle

The secure development lifecycle usually includes:

---

Design

```text
Design
```

---

Implementation

```text
Development
```

---

Testing

```text
Testing
```

---

Review

```text
Review
```

---

Deployment

```text
Deployment
```

---

Maintenance

```text
Maintenance
```

---

# What Has Our Port Scanner Followed?

---

Input validation

```text
Validation
```

---

Recording events

```text
Logging
```

---

Unit testing

```text
Unit Testing
```

---

Modular structure

```text
Modular Design
```

---

Error handling

```text
Exception Handling
```

---

Standard outputs

```text
JSON
CSV
```

---

All of these are used in real projects.

---

# Is Our Project Secure?

No software is 100% secure.

---

But compared to the initial version, our project has become:

- More stable
- More maintainable
- More testable
- More secure

---

# The Most Important Lesson of the Security Chapter

If you only remember one sentence from this entire chapter:

> Security is not a product; it is a continuous process.

---

There is no day when one can say:

```text
We are now secure forever.
```

---

Security always requires:

- Learning
- Reviewing
- Testing
- Improving

---

# Summary of the Cybersecurity Chapter

In this chapter, we learned:

- The basic concepts of security
- How attackers think
- What a vulnerability is
- How the security lifecycle works
- What Threat Modeling is
- What Authentication and Authorization are
- How Injection attacks are carried out
- What Input Validation is
- What Logging and Monitoring are
- What Defense in Depth is
- What Secure Development is

---

# What Will We Learn in the Next Chapter?

We now have all the necessary prerequisites.

We:

- Learned Python
- Learned networking
- Learned security

And now we are ready to enter the most important part of the entire course:

# The Fourth Chapter: The Port Scanner

In this chapter, we will examine the project we have built

**file by file**
and
**line by line**

We will learn:

- Why each file was created
- What each function does
- What role each line of code plays
- How the project's architecture was designed
- How the project can be extended

From the next session, we will enter the actual review of the project's code.
