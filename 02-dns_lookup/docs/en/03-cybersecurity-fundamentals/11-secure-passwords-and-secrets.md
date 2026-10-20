[🇮🇷 فارسی](/02-dns_lookup/docs/fa/03-cybersecurity-fundamentals/11-secure-passwords-and-secrets.md)

# Lesson 11: Secure Management of Passwords and Secrets

## Secure Passwords & Secrets

## 1. What Are Secrets?

In software development, a **Secret** refers to information whose disclosure could compromise the security of a system or user account.

Common examples:

- User or service account passwords
- API Keys
- Access Tokens
- Refresh Tokens
- Private encryption keys
- Database passwords
- Digital signing keys
- Connection information for external services

For example, suppose a Python application uses an API Key to connect to an external service. If this key is published in a public GitHub repository, someone else might use it for unauthorized access or resource consumption.

**Important principle:** Secrets should not be stored in source code, public files, Logs, or Git repositories without necessity.

---

## 2. The Difference Between API Keys, Passwords, and Tokens

These terms are related, but not identical.

| Type | Typical use | Example |
|---|---|---|
| Password | Authenticating a user or account | Login password |
| API Key | Identifying or authorizing an application or API consumer | Access key for a service |
| Access Token | Providing information or access permission within a specific period or context | API access Token |
| Refresh Token | Obtaining a new Access Token according to the system policy | Access renewal Token |
| Private Key | Performing cryptographic or signing operations with a private key | Digital signature key |

The exact use of this information depends on the service design. For example, not all API Keys have the same mechanism, and we should not assume that any key alone provides strong authentication or precise permissions.

---

## 3. Why Should We Not Place Secrets in Code?

Suppose we have written an application with this code:

```python
API_KEY = "my-secret-api-key"
```

This approach is problematic; because the key might be disclosed in various ways:

- The code is published in public GitHub.
- The file is sent to someone else.
- The key remains in Git history.
- A copy of the code is stored in a Backup or another system.
- Someone with access to the repository views the key.

Even if we later delete the line containing the key, the previous value might still exist in Git history.

### A Better Approach

Separate secrets from code and receive them from an appropriate source at runtime; for example:

- Environment Variables
- A local file outside the Git repository
- A Secret Manager
- A key management system, if necessary

For small educational projects, an environment variable or a local file ignored by Git can be a simple option.

For enterprise systems, access management, key rotation, event logging, and Secret lifecycle must also be considered.

---

## 4. Using Environment Variables in Python

Environment variables allow the application to receive settings outside of code.

Python provides the standard `os` module for accessing them.

### Example

```python
import os

api_key = os.getenv("MY_API_KEY")

if not api_key:
    raise RuntimeError("MY_API_KEY is not configured")

# Use api_key with the intended service.
```

In this example:

- `os.getenv()` reads the value of the environment variable.
- If the variable does not exist, it returns `None`.
- The program raises a specific error instead of continuing with incomplete configuration.

Of course, in a real application, it should be verified that the received value is in the expected format and that its use with the target service is properly managed.

### Setting the Variable in Linux and macOS

In a terminal, you can write:

```bash
export MY_API_KEY="your-secret-value"
python app.py
```

This variable will usually be available to processes executed from the same terminal environment.

### Setting the Variable in PowerShell

```powershell
$env:MY_API_KEY = "your-secret-value"
python app.py
```

This value usually remains for the lifetime of the same environment session.

### A Security Note

An Environment Variable is not by itself a complete Secret Manager. Depending on the operating system, process permissions, system management tools, and execution method, environment information might be exposed to observation.

Also, we should not print the Secret value to verify the configuration.

---

## 5. Using a `.env` File in Python Projects

In local projects, sometimes a `.env` file is used to hold environment settings.

Example file content:

```dotenv
MY_API_KEY=your-secret-value
DEBUG=false
```

The `.env` file can be suitable for the development environment, but should usually remain outside the Git repository.

To read this file in Python, a library such as `python-dotenv` can be used.

Install:

```bash
python -m pip install python-dotenv
```

Usage:

```python
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("MY_API_KEY")

if not api_key:
    raise RuntimeError("MY_API_KEY is not configured")
```

The `load_dotenv()` function loads the variables defined in the `.env` file into the application environment.

### Important Notes

- Do not make the `.env` file public.
- Do not add the `.env` file to Git.
- For teams, create a template like `.env.example` that only shows the required settings names.
- Do not place the actual Secret value in `.env.example`.
- In the operational environment, use a Secret management method appropriate to the infrastructure.

Example of a `.env.example` file:

```dotenv
MY_API_KEY=
DEBUG=false
```

This file shows the developer what settings are needed, without disclosing the actual confidential information.

---

## 6. Preventing Secrets from Being Committed to Git

One of the common mistakes is placing files containing confidential information in the Git repository.

The `.gitignore` file is used to specify files that should not normally be tracked by Git.

For example:

```gitignore
.env
.env.*
!.env.example
__pycache__/
*.py[cod]
.venv/
venv/
```

These settings ignore the `.env` file and similar files, but exclude `.env.example`.

However, this pattern alone does not cover all possible files; the project structure and file naming policy must also be considered.

### A Very Important Note About Git

`.gitignore` only prevents ignored files from being automatically added to the repository.

If a file has already been committed, adding its name to `.gitignore` does not remove it from Git history.

To check the status:

```bash
git status
```

To check whether Git is tracking a file:

```bash
git ls-files .env
```

If the file has already been committed, in addition to removing it from the tracked state of the repository, we must also examine the possibility of information disclosure.

**If a real Secret has been published, deleting the file alone is not enough; revoke or replace the Secret from the corresponding service.**

If necessary, the repository history must also be carefully cleaned; but this does not replace replacing the disclosed Secret.

---

## 7. Securely Managing User Passwords

In the previous lesson, we learned that passwords should not be stored in plain text.

But why?

Suppose a database of an application is stolen. If passwords are stored in plain text, the attacker will have them directly.

That is why standard authentication systems must use specialized password storage methods.

### Common Methods

- Argon2id
- scrypt
- bcrypt
- PBKDF2

These methods are designed to derive an output from a password, and using their proper settings increases the cost of bulk password guessing.

### Salt

Salt is a value used uniquely for each password.

Salt helps ensure that identical passwords do not necessarily have identical stored values, and makes the use of precomputed tables harder.

Salt is usually not confidential, and an appropriate password storage library can manage it.

### Note

For storing passwords, we should not use just this method:

```python
import hashlib

password_hash = hashlib.sha256(
    password.encode("utf-8")
).hexdigest()
```

This code computes a Hash, but is not a suitable method for storing user passwords; because SHA-256 is fast and allows testing a large number of guesses.

For this use case, we must use a specialized password storage library and algorithm.

---

## 8. The Difference Between Hashing and Encrypting a Password

These two methods do not have the same purpose.

### Encrypting a Password

If we encrypt a password with a symmetric encryption algorithm, its recovery with the appropriate key is possible.

This method is usually not a suitable choice for storing user login passwords; because the application should not need to recover the original password text.

### Specialized Password Hashing

In the standard method, the application, upon registration, stores the output of a specialized algorithm.

At login, the entered password is checked again to determine whether it matches the stored value.

In this process, there is no need to recover the original password text from the stored value.

**Important principle:** We store passwords for user login so that we can verify them, not so that we can later recover their original text.

Of course, some systems might, for different use cases, encrypt confidential information that truly needs recovery. That scenario is different from storing a login password.

---

## 9. Managing Tokens and API Keys

Tokens and API Keys might provide important access to resources. Therefore, we should treat them like confidential information.

### Important Principles

#### 9.1. Least Privilege

Enable only the necessary permissions for each key.

If a tool only needs to read information, use a key with read permission if the service supports it; not a key with full administrative access.

#### 9.2. Restricting the Scope of Use

If the target service allows restricting a key by project, resource, IP, or operation type, use the appropriate restrictions.

#### 9.3. Expiration and Rotation

For Tokens and keys that have expiration or rotation capability, define an appropriate policy.

Key rotation should be planned so that authorized services are not disrupted.

#### 9.4. Revoking a Disclosed Key

If a key is published or stolen:

1. Revoke or disable the key at the issuing service.
2. Create a new key with the appropriate permissions.
3. Examine the places where the previous key was used.
4. Check the related Logs for suspicious activity.
5. Fix the cause of the disclosure.
6. Ensure that the new key does not also reach the repository or Logs.

#### 9.5. Protecting Session Tokens

Session Tokens and Refresh Tokens might provide access to the user account.

They should not be published in public Logs, reports visible to others, or the code repository.

---

## 10. Preventing Secret Disclosure in Logs and Error Messages

Sometimes an application does not directly print the password, but records confidential information in an error message or Log.

For example, this method is insecure:

```python
logger.info("Using API key: %s", api_key)
```

Because the actual key value is recorded in the Log.

A more appropriate method:

```python
logger.info("API key has been configured")
```

In this case, only the configuration status is recorded, and the Secret value is not disclosed.

### Items That Should Not Be Logged Without Reason

- Password
- API Key
- Access Token
- Refresh Token
- Private Key
- Sensitive authentication information
- Unnecessary personal information

In addition to the Log content, we must also consider its storage location, access level, and retention period.

---

## 11. Managing Secrets in GitHub Projects

For Python projects published on GitHub, this checklist is useful.

### Before Committing

- [ ] No password or API Key is placed in the code.
- [ ] The `.env` file is not accidentally tracked.
- [ ] Configuration files containing Secrets have been checked.
- [ ] The settings sample contains only example values.
- [ ] Logs and error messages do not disclose confidential information.

### After Committing

- [ ] Check the repository status.
- [ ] Make sure local confidential files have not been published.
- [ ] If a Secret has been disclosed, revoke or replace it.
- [ ] If necessary, check the Git history and published versions.

### If the Repository Is Public

A public repository does not mean all settings must be public.

The application code can usually be public, but the actual Secret values must remain separate from the code.

---

## 12. How This Lesson Relates to Our Python Projects

In the projects `01-port_scanner` and `02-dns_lookup`, we might not currently need an API Key or password.

However, these principles become important in developing future versions and new tools.

For example, if we build a tool in the future that communicates with an external security service, we must:

- Keep the API Key separate from the code.
- Receive the necessary settings from the environment.
- Prevent the key from being logged.
- If possible, restrict the key to the minimum necessary permissions.
- Properly manage the program's behavior when the key is missing.
- Have appropriate settings for the development and operational environments.

If our tool only needs a non-confidential configuration value, there is no need to treat it as a Secret without reason. Correctly identifying the type of data also matters.

---

## 13. Common Mistakes

### First Mistake: Placing an API Key Inside the Code

The key might be published with the code or remain in Git history.

### Second Mistake: Thinking `.gitignore` Deletes Previous Files

This file only affects Git's tracking of files and does not delete the previous history.

### Third Mistake: Deleting a Disclosed Secret Without Replacing It

If the key has already been published, it must be revoked or replaced; deleting the file alone is not enough.

### Fourth Mistake: Storing Passwords in Plain Text

If the database is disclosed, the passwords are directly available to the attacker.

### Fifth Mistake: Using a Simple SHA-256 for Storing Passwords

For this task, specialized password key-derivation algorithms must be used.

### Sixth Mistake: Printing a Secret in Logs

Even if the code repository is secure, Logs can also become a path for information disclosure.

### Seventh Mistake: Giving Excessive Permissions to an API Key

If the key is compromised, excessive permissions can increase the damage.

---

## 14. Summary

In this lesson, we learned:

- Secrets include passwords, API Keys, Tokens, and private keys.
- Confidential information should not be placed in source code or public Logs.
- Environment variables and the `.env` file can be useful for managing settings in the development environment.
- Files containing Secrets must remain outside the Git repository.
- `.gitignore` does not delete previous Git history.
- User passwords must be stored with a specialized algorithm and proper settings.
- Tokens and API Keys must have the minimum necessary permissions.
- If a Secret is disclosed, it must be revoked or replaced, and the cause of the disclosure fixed.
- Confidential information should not be recorded in Logs or error messages without reason.

### Exercise 1: Reviewing a Code Snippet

Review the following code:

```python
import requests

API_KEY = "example-secret-value"

response = requests.get(
    "https://api.example.com/data",
    headers={"Authorization": f"Bearer {API_KEY}"},
    timeout=10,
)

print(response.text)
```

Answer these questions:

1. Why can placing the key in the code be dangerous?
2. How can the key be received from an environment variable?
3. Is printing the full response always appropriate? What information might be in the response?
4. Why should we use a Timeout for an HTTP request?

Note: The domain `example.com` in this example is only a sample, and this code alone does not implement a real service.

### Exercise 2: Designing Project Files

For a Python project, explain which of the following should be in Git:

- `.env`
- `.env.example`
- `.gitignore`
- The Python file that uses the environment variable
- A Log file containing sensitive information

Write your reasoning for each item.

### Exercise 3: Responding to a Key Disclosure

Suppose the project's API Key was accidentally published in a public GitHub repository.

Write a step-by-step response plan that includes:

- Revoking or replacing the key
- Checking for suspicious activities
- Correcting the code and settings
- Checking the repository history
- Preventing recurrence

