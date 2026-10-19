[🇮🇷 فارسی](/02-dns_lookup/docs/fa/01-python-fundamentals/03-loops.md)

# Lesson 3: Loops in Python

## Introduction

So far, we have learned how to store data in variables and how to make decisions using conditions.

But in real programs, we usually do not deal with just one value.

For example, in the DNS Lookup project, we might receive several DNS records:

```python
[
    "1.1.1.1",
    "8.8.8.8",
    "9.9.9.9",
]
```

If we wanted to display all these values, writing separate code for each value would not be logical.

To solve this problem, we use **Loops**.

---

# What Is a Loop?

A loop is a tool that runs a piece of code several times.

Example:

```python
for number in [1, 2, 3]:
    print(number)
```

Output:

```text
1
2
3
```

---

# The `for` Loop

The most common loop in Python is `for`.

General structure:

```python
for item in collection:
    # code
```

Example:

```python
domains = [
    "google.com",
    "github.com",
    "python.org",
]

for domain in domains:
    print(domain)
```

Output:

```text
google.com
github.com
python.org
```

---

# Iterating Over Strings

A string is also a collection of characters.

Example:

```python
for char in "DNS":
    print(char)
```

Output:

```text
D
N
S
```

---

# The `range()` Function

Used to generate a sequence of numbers.

Example:

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

---

# Specifying Start and End

Example:

```python
for number in range(1, 6):
    print(number)
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

# Specifying a Step

Example:

```python
for number in range(0, 10, 2):
    print(number)
```

Output:

```text
0
2
4
6
8
```

---

# Looping Over Lists

One of the most important uses of loops in the DNS Lookup project is processing the list of records.

Example:

```python
records = [
    "1.1.1.1",
    "8.8.8.8",
]

for record in records:
    print(record)
```

---

# Building a List with a Loop

Example:

```python
results = []

for value in ["1.1.1.1", "8.8.8.8"]:
    results.append(value)
```

Now:

```python
print(results)
```

Output:

```text
['1.1.1.1', '8.8.8.8']
```

---

# List Comprehension

Python also has a shorter way to build a list.

Example:

```python
results = [
    value
    for value in ["1.1.1.1", "8.8.8.8"]
]
```

This is exactly equivalent to the previous example.

---

# Direct Connection to the Project

In the file:

```python
results.py
```

we have used List Comprehension:

```python
return [
    DNSRecord(
        domain=domain,
        record_type=record_type,
        value=value,
    )
    for value in values
]
```

This code moves over all the returned DNS values and creates a `DNSRecord` object for each value.

---

# The Loop in `formatter.py`

In the file:

```python
formatter.py
```

we have also used a loop:

```python
for result in results:
    lines.append(
        f"{result.domain:<30} "
        f"{result.record_type:<8} "
        f"{result.value}"
    )
```

This loop processes all the DNS records and adds them to the text output.

---

# The `break` Statement

Used to exit the loop immediately.

Example:

```python
for number in range(10):
    if number == 5:
        break

    print(number)
```

Output:

```text
0
1
2
3
4
```

---

# The `continue` Statement

Used to skip one iteration.

Example:

```python
for number in range(5):
    if number == 2:
        continue

    print(number)
```

Output:

```text
0
1
3
4
```

---

# The `enumerate()` Function

If we need both the index and the value at the same time:

```python
records = [
    "1.1.1.1",
    "8.8.8.8",
]

for index, value in enumerate(records):
    print(index, value)
```

Output:

```text
0 1.1.1.1
1 8.8.8.8
```

---

# The `while` Loop

Another type of loop that continues as long as a condition holds.

Example:

```python
count = 0

while count < 3:
    print(count)
    count += 1
```

Output:

```text
0
1
2
```

---

# Why Did We Use `for` in the Project?

Because:

- The number of records is not known in advance.
- We need to move over a collection of results.
- `for` is more readable and safer than `while`.

That is why `for` and List Comprehension have been used in most parts of the project.

---

# Exercise

1. Create a list containing three domains.

2. Use `for` to print all the domains.

3. Use `range()` to print the numbers 1 through 10.

4. Create a list of IPs and use List Comprehension to create a new version of the same list.

5. Write a program that exits the loop when it reaches the number 5.

---

# Lesson Summary

In this lesson, we learned:

- The `for` loop
- The `while` loop
- The `range` function
- Iterating over lists
- List Comprehension
- `break`
- `continue`
- `enumerate`

These concepts are used in the DNS Lookup project for processing DNS results, building data models, and producing the final output.

In the next lesson, we will become familiar with Functions; a concept on which almost all the project's files are built.
