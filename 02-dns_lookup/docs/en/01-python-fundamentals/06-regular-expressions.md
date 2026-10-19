[🇮🇷 فارسی](/02-dns_lookup/docs/fa/01-python-fundamentals/06-regular-expressions.md)

# Lesson 6: Regular Expressions (Regex)

## Introduction

In the DNS Lookup project, the first place where we used a relatively advanced Python tool was the file:

```text
validator.py
```

In this file, the function:

```python
validate_domain()
```

uses Regex to check the validity of a domain name.

If Regex did not exist, we would have had to write dozens of different conditions.

That is why Regex is considered one of the most important data-validation tools in programming.

---

# What Is Regex?

Regex stands for:

```text
Regular Expression
```

Regex is a small language for searching and matching patterns in text.

For example:

- Validating an email
- Validating a phone number
- Validating an IP
- Validating a domain
- Extracting data from text

are all common uses of Regex.

---

# The First Example

Suppose we want to check whether a string contains only digits or not.

```python
import re

pattern = r"\d+"

print(bool(re.fullmatch(pattern, "12345")))
```

Output:

```text
True
```

But:

```python
print(bool(re.fullmatch(pattern, "123abc")))
```

Output:

```text
False
```

---

# The `re` Module

In Python, Regex is implemented by the module:

```python
import re
```

Almost all Regex operations are performed through this module.

---

# The `fullmatch` Function

In the project, we have used:

```python
re.fullmatch()
```

Example:

```python
re.fullmatch(r"\d+", "123")
```

Result:

```text
Match
```

But:

```python
re.fullmatch(r"\d+", "123abc")
```

Result:

```text
None
```

---

# Why `fullmatch`?

Because we want the entire string to be checked.

Not just a part of it.

Example:

```python
re.search(r"\d+", "abc123xyz")
```

succeeds.

But:

```python
re.fullmatch(r"\d+", "abc123xyz")
```

fails.

---

# Raw String

In Regex, we usually write:

```python
r"\d+"
```

The letter:

```text
r
```

before the string means:

```text
Raw String
```

so that backslashes are interpreted correctly.

---

# Important Regex Characters

## Dot

```python
.
```

means:

```text
Any character
```

Example:

```python
re.fullmatch(r"a.c", "abc")
```

succeeds.

---

## Asterisk

```python
*
```

means:

```text
Zero or more
```

Example:

```python
ab*
```

accepts:

```text
a
ab
abb
abbb
```

---

## Plus Sign

```python
+
```

means:

```text
One or more
```

Example:

```python
ab+
```

accepts:

```text
ab
abb
abbb
```

But does not accept:

```text
a
```

---

## Question Mark

```python
?
```

means:

```text
Zero or one time
```

Example:

```python
colou?r
```

accepts:

```text
color
colour
```

---

# Character Classes

## Digits

```python
\d
```

equivalent to:

```text
0-9
```

---

## Letters and Digits

```python
\w
```

---

## Whitespace

```python
\s
```

---

# Brackets

Example:

```python
[A-Z]
```

means:

All uppercase English letters.

---

Example:

```python
[a-z]
```

All lowercase letters.

---

Example:

```python
[0-9]
```

All digits.

---

# Ranges

Example:

```python
[A-Za-z]
```

means:

All English letters.

---

Example:

```python
[A-Za-z0-9]
```

means:

All letters and digits.

---

# Reviewing the Project's Regex

In the file:

```python
validator.py
```

we have:

```python
pattern = (
    r"^(?!-)"
    r"(?:[A-Za-z0-9-]{1,63}\.)+"
    r"[A-Za-z]{2,63}$"
)
```

Now we review it part by part.

---

# The First Part

```python
^
```

means:

```text
Start of the string
```

The Regex must start from the beginning of the text.

---

# The Second Part

```python
(?!-)
```

This is a:

```text
Negative Lookahead
```

Meaning:

```text
The domain must not start with -
```

---

Valid example:

```text
google.com
```

---

Invalid example:

```text
-google.com
```

---

# The Third Part

```python
[A-Za-z0-9-]
```

Allows:

- Letters
- Digits
- Hyphen

to exist in the domain.

---

# The Fourth Part

```python
{1,63}
```

means:

```text
At least 1 and at most 63 characters
```

Because each label in DNS has a maximum of 63 characters.

---

Example:

```text
google
```

is valid.

---

# The Fifth Part

```python
\.
```

represents the actual dot in the domain.

Example:

```text
google.com
```

---

# The Sixth Part

```python
(?: ... )+
```

This part says:

```text
One or more labels
```

must exist.

---

Example:

```text
google.com
```

---

Example:

```text
mail.google.com
```

---

Example:

```text
docs.mail.google.com
```

are all valid.

---

# The Last Part

```python
[A-Za-z]{2,63}
```

is for the TLD.

Example:

```text
com
net
org
io
dev
academy
```

---

# End of the String

```python
$
```

means:

```text
End of the string
```

Therefore, nothing is allowed after the TLD.

---

# Valid Examples

```text
google.com
```

```text
openai.com
```

```text
mail.google.com
```

```text
example.org
```

---

# Invalid Examples

```text
-google.com
```

---

```text
google
```

---

```text
google.
```

---

```text
google..com
```

---

```text
@google.com
```

---

# The Project's Tests

In the file:

```text
test_validator.py
```

we wrote many tests for this Regex.

Example:

```python
assert validate_domain("google.com")
```

---

Example:

```python
assert not validate_domain("google")
```

---

Example:

```python
assert not validate_domain("-google.com")
```

---

# Why Is Regex Important?

In security tools, we constantly deal with data validation.

Examples:

- Domain Validation
- Email Validation
- URL Validation
- IP Validation
- Log Parsing
- IOC Extraction

Therefore, Regex is one of the most important skills required in security tools.

---

# The Limitation of the Current Regex

Our Regex is simple and educational.

It does not cover all the RFC rules for domains.

But for this project:

```text
Learning-Oriented
```

is completely sufficient and appropriate.

---

# Exercise

1. Write a Regex that accepts only digits.

---

2. Write a Regex that accepts only English letters.

---

3. Write a Regex that accepts the following domains:

```text
google.com
openai.com
example.org
```

---

4. Check:

```python
re.search()
```

and

```python
re.fullmatch()
```

What is the difference between them?

---

5. Explain the project's current Regex line by line.

---

# Lesson Summary

In this lesson, we learned:

- What Regex is
- The `re` module
- `fullmatch`
- Raw String
- Character classes
- Quantifiers
- Lookahead
- Domain validation with Regex

This was the first concept extracted and analyzed directly from the actual code of the DNS Lookup project.

In the next lesson, we enter **Dataclass**; a concept used in the file `models.py` to build the `DNSRecord` model.
