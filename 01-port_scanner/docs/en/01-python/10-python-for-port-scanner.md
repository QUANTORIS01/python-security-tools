[🇮🇷 فارسی](/01-port_scanner/docs/fa/01-python/10-python-for-port-scanner.md)

# Session 10 — Putting It Together: Python for Building a Port Scanner

## Goal of This Session

So far, we have learned almost all the Python tools we needed to build the Port Scanner project.

In this session, we want to see exactly which Python concepts each part of our real project uses.

After this session ends, we will be ready to enter the Networking chapter.

---

# A Bird's-Eye View of the Project

Our port scanner looks simple on the surface:

1. Receive IP
2. Receive port range
3. Check whether ports are open
4. Detect services
5. Retrieve Banner
6. Display results
7. Save output

But behind the scenes, we have used almost all the important Python concepts.

---

# Getting Input from the User

File:

```python
cli.py
```

Example:

```python
parser.add_argument("ip")
parser.add_argument("start_port")
parser.add_argument("end_port")
```

Here we have used:

- Variables
- Functions
- Modules
- The `argparse` library

---

# Validating Inputs

File:

```python
validator.py
```

Example:

```python
if port < 1 or port > 65535:
    raise ValueError()
```

Here we have used:

- Conditions
- Operators
- Exceptions

---

# Scanning Ports

File:

```python
scanner.py
```

Example:

```python
for port in range(start_port, end_port + 1):
```

Here we have used:

- Loops
- Functions
- `ThreadPoolExecutor`

---

# Working with Sockets

Example:

```python
with socket.socket() as sock:
    ...
```

Here we have used:

- Context Manager
- The `socket` module
- Resource management

---

# Detecting Services

File:

```python
services.py
```

Example:

```python
COMMON_PORTS = {
    80: "http",
    443: "https",
}
```

Here we have used:

- Dictionary
- Fast lookup

---

# Banner Grabbing

File:

```python
banner.py
```

Example:

```python
banner = sock.recv(1024)
```

Here we have used:

- Bytes
- Decode
- Error handling

---

# Building the Data Model

File:

```python
models.py
```

Example:

```python
@dataclass(frozen=True)
class ScanResult:
```

Here we have used:

- Class
- Dataclass
- Object

---

# Saving JSON Output

File:

```python
exporter.py
```

Example:

```python
json.dump(data, file)
```

Concepts:

- Files
- JSON
- Dictionary

---

# Saving CSV Output

File:

```python
csv_exporter.py
```

Example:

```python
writer.writerow(row)
```

Concepts:

- CSV
- File Handling

---

# Displaying Results

File:

```python
formatter.py
```

Example:

```python
f"{result.port:<8}"
```

Concepts:

- String Formatting
- f-string

---

# Logging

File:

```python
logger.py
```

Example:

```python
logger.info("Scan started")
```

Concepts:

- Logging
- File Writing

---

# Testing

Folder:

```python
tests/
```

Example:

```python
def test_scan_open_port():
```

Concepts:

- Unit Testing
- Pytest
- Mocking

---

# What We Have Learned So Far

By now, you have become familiar with the following concepts:

✓ Variables
✓ Data types
✓ Conditions
✓ Loops
✓ Functions
✓ Modules
✓ Files
✓ JSON
✓ CSV
✓ Exceptions
✓ Sockets
✓ Logging
✓ Dataclass
✓ Testing

---

# Can We Build a Port Scanner Now?

Yes.

In fact, the project we have built so far is written with exactly this knowledge.

But one important piece is still missing:

"Knowing the network."

We have learned how to write code so far.

But we still do not know:

- What is an IP?
- What is a Port?
- What is TCP?
- What is UDP?
- What is DNS?
- What is a Router?
- What is a Packet?

Without knowing these concepts, understanding the Port Scanner will be incomplete.

---

# End of the First Chapter

Congratulations 🎉

You have finished the Python chapter.

You are now ready to enter the second chapter:

**02-networking**

And there, we will become familiar with networking from scratch, up to the level needed to fully understand the Port Scanner.
