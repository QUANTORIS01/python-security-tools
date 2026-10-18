[🇮🇷 فارسی](/01-port_scanner/docs/fa/01-python/04-conditions-and-loops.md)

# Session 04 — Conditions and Loops

# Introduction

Suppose we have scanned a port.

If the port is open:

```text
OPEN
```

display it.

And if it is closed:

```text
CLOSED
```

display that.

Or suppose we want to check ports 1 through 1000 one by one.

To do such things, we need two very important concepts:

- Conditions
- Loops

Almost all real programs use these two concepts.

---

# What Is a Condition?

A condition lets the program make decisions.

Example:

```python
port_is_open = True

if port_is_open:
    print("Port is open")
```

Output:

```text
Port is open
```

---

In plain words:

```text
If this condition is true,
execute this code.
```

---

# The `if` Structure

General form:

```python
if condition:
    code
```

Example:

```python
port = 80

if port == 80:
    print("HTTP Port")
```

Output:

```text
HTTP Port
```

---

# The `==` Operator

Many beginners get this part wrong.

This:

```python
=
```

is for storing a value.

Example:

```python
port = 80
```

But this:

```python
==
```

is for comparison.

Example:

```python
port == 80
```

means:

```text
Is the value of port equal to 80?
```

---

# Using `else`

Sometimes we want something else to happen if the condition is not true.

Example:

```python
port = 443

if port == 80:
    print("HTTP")
else:
    print("Not HTTP")
```

Output:

```text
Not HTTP
```

---

# Using `elif`

Sometimes we have more than two cases.

Example:

```python
port = 443

if port == 80:
    print("HTTP")

elif port == 443:
    print("HTTPS")

else:
    print("Unknown")
```

Output:

```text
HTTPS
```

---

# Comparison Operators

Equal:

```python
==
```

---

Not equal:

```python
!=
```

Example:

```python
port != 80
```

---

Greater than:

```python
>
```

---

Less than:

```python
<
```

---

Greater than or equal to:

```python
>=
```

---

Less than or equal to:

```python
<=
```

---

# A Real Example

Checking a port number:

```python
port = 8080

if port > 1024:
    print("User Port")
```

---

# What Is a Loop?

Sometimes we need to repeat a task many times.

Suppose we want to display:

```text
Scanning Port 1
Scanning Port 2
Scanning Port 3
...
Scanning Port 1000
```

Writing a thousand lines of code is not logical.

That is why we use loops.

---

# The `for` Loop

Example:

```python
for port in range(1, 6):
    print(port)
```

Output:

```text
1
2
3
4
5
```

---

# What Is `range`?

The function:

```python
range()
```

generates a sequence of numbers.

Example:

```python
range(1, 6)
```

produces the numbers:

```text
1
2
3
4
5
```

Note:

```text
The last number is not included.
```

---

# A Real Port Scanner Example

Suppose we want to check ports 1 through 10:

```python
for port in range(1, 11):
    print(f"Scanning Port {port}")
```

Output:

```text
Scanning Port 1
Scanning Port 2
Scanning Port 3
...
Scanning Port 10
```

---

# Using `if` Inside `for`

This is exactly like what happens in a port scanner.

Example:

```python
for port in range(1, 6):

    if port == 3:
        print("Open")

    else:
        print("Closed")
```

Output:

```text
Closed
Closed
Open
Closed
Closed
```

---

# The `while` Loop

Another type of loop:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

---

# Why Do We Use `for` More in the Port Scanner?

Because we usually have a specific range of ports:

```python
1 - 1000
```

or:

```python
1 - 65535
```

So:

```python
for port in range(...)
```

is much more suitable.

---

# An Example Close to the Real Project

Code similar to what we do in the scanner:

```python
open_ports = [80, 443]

for port in range(1, 6):

    if port in open_ports:
        print(f"{port} OPEN")

    else:
        print(f"{port} CLOSED")
```

Output:

```text
1 CLOSED
2 CLOSED
3 CLOSED
4 CLOSED
5 CLOSED
```

If port 80 had been in the range:

```text
80 OPEN
```

would have been displayed.

---

# How This Lesson Connects to the Project

In the Port Scanner project:

We use conditions to:

- Detect whether a port is open
- Detect whether a port is closed
- Detect services
- Check for errors

---

We use loops to:

- Iterate over ports
- Process results
- Build outputs
- Display information

---

# Summary

✅ Conditions let the program make decisions.

✅ We use `if` to check a condition.

✅ We use `else` for the alternative case.

✅ We use `elif` for multiple conditions.

✅ Loops are for repeating operations.

✅ The `for` loop is the most-used loop in the Port Scanner project.

---

# Exercise

Write a program that:

- Checks ports 1 through 10.
- If the port number is even, display:

```text
Even Port
```

- If it is odd, display:

```text
Odd Port
```
