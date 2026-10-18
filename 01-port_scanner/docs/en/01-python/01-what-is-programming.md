[🇮🇷 فارسی](/01-port_scanner/docs/fa/01-python/01-what-is-programming.md)

# Lesson 1 — What Is Programming?

## Introduction

Before we learn Python, we need to answer a simple but very important question:

**What is programming?**

If we don't understand this concept properly, we might be able to memorize Python code, but when we face a new problem, we won't know where to start.

The goal of this course is not to memorize code.

The goal is to learn:

> To break a problem down into small steps, express those steps in a language the computer can understand, and ultimately build a working program.

The same thing will happen in our project.

In the end, we want to start from a simple problem:

> "How do we find out whether a TCP port is open on a system?"

And turn it, step by step, into a real Port Scanner.

---

# 1. What Is a Computer?

Before programming, we need to know what we're talking to.

A computer is a device that can:

- Receive data
- Process data
- Store data
- Produce output

But unlike humans, a computer does not naturally understand the meaning of human sentences.

For example, if we tell a computer:

> "Go check whether port 80 is open."

This sentence is understandable to a human, but to do it, the computer needs precise instructions.

We must specify exactly:

1. Which IP to connect to?
2. Which protocol to use?
3. Which port to connect to?
4. How long to wait for a response?
5. What to do if the connection succeeds?
6. What to do if the connection fails?

This is where **programming** comes in.

---

# 2. What Is Programming?

> **Programming** means writing a set of instructions for the computer to perform a specific task.

In simple terms:

> Programming = turning a problem into precise, executable instructions for the computer

For example, suppose we want to write a program that adds two numbers.

The problem:

```text
first number = 10
second number = 20
```

What we want to do:

```text
10 + 20
```

The result:

```text
30
```

For a human, this is very simple.

But the program has to express this in a way that the programming language understands.

For example, in Python:

```python
print(10 + 20)
```

Output:

```text
30
```

We turned a human problem into an executable instruction.

---

# 3. What Is a Program?

> A **Program** is a set of instructions written to accomplish a specific task.

For example, a program can be:

- A calculator
- A web browser
- A game
- A file management system
- A web server
- A port scanner

The program we build in our project is also a set of instructions whose job is to check the status of TCP ports.

---

# 4. What Is Code?

> **Code** refers to the instructions we write using a programming language.

For example:

```python
print("Hello")
```

This is a piece of **Python code**.

Here:

```python
print
```

is a built-in Python function used to display a value.

And:

```python
"Hello"
```

is the text we want to display.

When we put the two together:

```python
print("Hello")
```

Python executes it, and the result is:

```text
Hello
```

---

# 5. What Is a Programming Language?

A computer needs precise instructions to run programs.

To write those instructions, we use a **Programming Language**.

There are many different programming languages, such as:

- Python
- C
- C++
- Java
- JavaScript
- Go
- Rust

Each language has its own syntax and rules.

For example, in Python:

```python
print("Hello")
```

But in other languages, the way to express the same concept may be different.

Therefore:

> A Programming Language is a tool that lets us write machine-understandable instructions in a structured way.

---

# 6. Why Python?

In this project, we use Python.

Python is suitable for this project for several reasons:

### Readability

Its syntax is relatively simple and readable.

For example:

```python
print("Hello")
```

is very understandable to a human.

### Standard Libraries

Python gives us facilities for things like:

- networking
- sockets
- files
- JSON
- concurrency
- testing
- command-line applications

In the current project, we also use parts of Python's standard library, such as:

```python
socket
```

and:

```python
concurrent.futures
```

### Suitable for Learning

Python lets us focus more on **problem-solving** and get less bogged down in complex syntax.

---

# 7. What Is Python Itself?

> Python is a **programming language**.

But there is a more important question:

If Python is just a language, how does the computer execute our Python code?

This is where the concept of the **Python Interpreter** comes in.

---

# 8. What Is an Interpreter?

When we write:

```python
print("Hello")
```

the computer's processor does not directly execute this expression as a Python instruction.

An implementation of Python, such as **CPython**, receives the Python code and processes it for execution.

In simple terms, we can imagine the path like this:

```text
Python Code
     ↓
Python Interpreter
     ↓
Execution
     ↓
Output
```

For example:

```text
print("Hello")
```

↓

```text
Python
```

↓

```text
Hello
```

This mental model is enough to start with.

We will examine the internal details of Python execution later in the lessons on the interpreter and runtime.

---

# 9. The First Python Program

Now let's write our first program:

```python
print("Hello, World!")
```

If we run it, we will see:

```text
Hello, World!
```

---

# 10. What Is `print()`?

In Python, `print()` is used to write information to **standard output**.

In the simplest case, this means we see the information in the terminal.

For example:

```python
print("Hello")
```

Output:

```text
Hello
```

Let's break this statement into parts.

```python
print("Hello")
```

`print`

is the name of the function.

### `(` and `)`

These parentheses are used to call the function and pass its arguments.

`"Hello"`

is a **string**.

### The Whole Statement

```python
print("Hello")
```

means:

> Send the value `"Hello"` to standard output for display.

---

# 11. What Is a Function?

> A Function is one of the most important concepts in Python.

> For now, we can imagine a Function like this:

> A part of the program that performs a specific task.

For example:

```python
print()
```

Its job is to display information.

Later, we will build our own functions too.

For example:

```python
def say_hello():
    print("Hello")
```

Here:

```python
def
```

is used to define a function.

And:

```python
say_hello
```

is the name of the function.

Later, we will talk in full about:

- function
- parameter
- argument
- return
- scope

For now, just keep this concept in mind:

> A Function is a reusable part of a program responsible for performing a specific task.

---

# 12. What Is a String?

In the example:

```python
print("Hello")
```

the expression:

```python
"Hello"
```

is a **string**.

> A String means textual data.

For example:

```python
"Hello"
```

or:

```python
"Python"
```

or:

```python
"127.0.0.1"
```

are all strings.

Even this:

```python
"80"
```

is a string.

Pay attention:

```python
80
```

and:

```python
"80"
```

are not the same.

The first is a number.

The second is text.

This difference is very important in programming and will be examined in full later.

---

# 13. What Is a Terminal?

Throughout the project, we will work a lot with the **Terminal**.

> A Terminal is an environment where we can run text commands.

For example:

```powershell
python --version
```

or:

```powershell
python
```

or running a program:

```powershell
python src/cli.py
```

In our project, the Terminal is very important, because the Port Scanner is a **CLI application**.

> CLI means:

> Command-Line Interface

Meaning the user interacts with the program through the command line.

---

# 14. What Is Standard Output?

When a program displays something with `print()`, this information usually goes to **stdout** or **standard output**.

For example:

```python
print("Hello")
```

Conceptually:

```text
Python Program
      |
      v
    stdout
      |
      v
   Terminal
```

Later, when we work with:

- logging
- pipes
- shell commands
- redirection

the difference between stdout and other streams will become more important.

---

# 15. Programming Is Not Just Writing Code

This is one of the most important parts of this lesson.

Many people think programming means:

> "Write code."

But real programming starts before writing code.

Suppose the problem is:

> Build a Port Scanner.

If we immediately start writing:

```python
socket.socket(...)
```

we might write a program that works, but it will probably have many problems.

First, we must analyze the problem.

For example:

```text
Problem
  ↓
Requirements
  ↓
Design
  ↓
Implementation
  ↓
Testing
  ↓
Debugging
  ↓
Refactoring
```

This workflow is one of the most important things we will learn in this project.

---

# 16. Example: Designing a Port Scanner

The problem:

> We want to know whether a TCP port is open or not.

First, we break the problem down into smaller questions.

### Question 1

> What is the target?

For example:

```text
127.0.0.1
```

### Question 2

Which port should we check?

For example:

```text
80
```

### Question 3

How should we check it?

We can try to establish a TCP connection.

### Question 4

What if the connection succeeds?

The port is probably open.

### Question 5

What if the connection fails?

The port is probably not reachable.

### Question 6

What if the connection takes too long?

We need a timeout.

Now the problem is gradually becoming implementable.

---

# 17. What Is an Algorithm?

Before writing code, we can express the steps of solving the problem as an **Algorithm**.

For a single port:

> 1. Get the target IP.
> 2. Get the port.
> 3. Create a TCP socket.
> 4. Set a timeout.
> 5. Try to connect to the target.
> 6. If the connection succeeds:  
>       port = OPEN
> 7. If the connection fails:  
>       port = NOT OPEN
> 8. Close the socket.

This is not Python code yet.

But it is a plan for writing Python code.

This difference is very important:

> Algorithm = the method of solving the problem

> Code = the implementation of that method in a programming language

---

# 18. Why Is This Important for Cybersecurity?

In Cybersecurity, we constantly face problems that we must break down into smaller steps.

For example:

```text
Reconnaissance
      ↓
Identify Host
      ↓
Identify Ports
      ↓
Identify Services
      ↓
Identify Versions
      ↓
Analyze Attack Surface
```

Each step is itself a problem.

If we learn Python only as syntax, we might be able to write:

```python
for
if
def
import
```

But we won't know **when and why** to use them.

The goal of this course is to learn, in addition to syntax, the ability to solve problems.

---

# 19. Common Mistake #1: Memorizing Code

Suppose you have memorized this code:

```python
print("Hello")
```

If tomorrow someone asks you:

> How do we add two numbers?

You might only know that same code and not know what to do.

But if you have understood the concept, you can analyze the problem:

```text
We have two values
      ↓
We add them together
      ↓
We display the result
```

And you arrive at:

```python
print(10 + 20)
```

So:

> The goal of learning Programming is not to memorize syntax; it is the ability to build a solution.

---

# 20. Common Mistake #2: Starting Directly from Code

When you receive a problem, before writing code, ask these questions:

> What is the Problem?  
> What is the Input?  
> What is the Output?  
> What are the Rules?  
> What are the Constraints?  
> What are the Edge Cases?

For example, for a Port Scanner:

Input

```text
IP address
Start port
End port
Timeout
Workers
```

Output

For example:

```text
80 OPEN
443 OPEN
```

Constraints

For example:

> Port must be between 0 and 65535.  
> Timeout must be positive.

This kind of thinking will be very important later in project design.

---

# 21. How This Lesson Connects to the Project

In our project:

```text
Problem
   ↓
Network Concepts
   ↓
Python Concepts
   ↓
Algorithm
   ↓
Implementation
   ↓
Tests
   ↓
Working Tool
```

For example:

> "Build a Port Scanner"

leads to:

```text
socket
```

Then:

```text
socket
+
timeout
+
connection
```

leads to:

```text
scan_port()
```

Then:

```text
scan_port()
+
multiple ports
+
concurrency
```

leads to:

```text
scan_range()
```

And then:

```text
scanner
+
service detection
+
banner grabbing
+
results
+
formatting
+
export
```

becomes our current tool.

So every project file will be the result of a specific concept and a specific problem.

---

# 22. Exercises

## Exercise 1

Without running Python, explain what this code does:

```python
print("Python")
```

---

## Exercise 2

Explain the difference between these two:

```python
print(80)
```

and:

```python
print("80")
```

---

## Exercise 3

Break this problem down into small steps:

> Build a program that receives the user's name and then greets them.

For now, don't write code.

Just write the Algorithm.

For example:

```text
1. ...
2. ...
3. ...
```

---

## Exercise 4 — Challenge

The problem:

> We want a program that receives an IP and a port and checks whether it can connect to that port or not.

For now, don't write Python code.

Just specify:

What is the Input?

What is the Output?

### What are the steps of the Algorithm?

### What things might cause the operation to fail?

This exercise is the direct introduction to our entry into the Networking section and then `scanner.py`.

---

# 23. Summary

In this lesson, we learned:

- What a computer is.
- What programming is.
- What a program is.
- What code is.
- What a programming language is.
- What Python is.
- What role the interpreter plays.
- What `print()` is.
- What a function is.
- What a string is.
- What a terminal is.
- What stdout is.
- What an algorithm is.
- Why we should analyze the problem before writing code.
- Why memorizing code is different from learning programming.

The most important concept of this lesson:

> **A programmer is not someone who only knows syntax; a programmer is someone who can analyze a problem and build an executable solution for it.**

In our project, we start this skill from the simplest concepts and eventually use it to build a Network Reconnaissance Tool.
