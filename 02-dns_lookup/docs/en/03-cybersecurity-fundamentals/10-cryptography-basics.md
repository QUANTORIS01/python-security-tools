[🇮🇷 فارسی](/02-dns_lookup/docs/fa/03-cybersecurity-fundamentals/10-cryptography-basics.md)

# Lesson 10: Cryptography Basics

## 1. What Is Cryptography?

**Cryptography** is a branch of science that provides methods for protecting information and communications.

Cryptography can help us:

- Keep information confidential.
- Detect unauthorized changes to data.
- Verify the identity of a sender or service.
- Confirm the authenticity and integrity of messages.

For example, when we connect to a website using HTTPS, cryptographic mechanisms are used to protect the communication.

But cryptography is not limited to HTTPS. This concept is used in information storage, digital signatures, key management, and many security systems.

### Basic Terms

| Term | Meaning |
|---|---|
| Plaintext | Readable data before encryption |
| Ciphertext | Encrypted output |
| Encryption | Converting data into an encrypted form |
| Decryption | Restoring encrypted data to its original form |
| Key | The key used in cryptographic operations |
| Cipher | A cryptographic algorithm |
| Hash | The output of a hash function |
| Digital Signature | A digital signature for verifying authenticity and integrity |

Important note: **Encryption, Encoding, and Hashing are three different concepts.** We will examine their differences more precisely below.

---

## 2. What Is Encoding?

**Encoding** is a method for representing data in a specific format.

The main goal of Encoding is usually not confidentiality, but converting data into a format suitable for transmission, storage, or processing.

For example, Base64 converts binary data into a text form that is easier to transmit in text-based systems.

Suppose we have the following string:

`Hello`

Its Base64 representation is:

`SGVsbG8=`

This conversion is not considered encryption; because anyone who knows the Base64 format can restore the data to its original form.

### Uses of Encoding

- Transmitting binary data in text form
- Displaying data in standard formats
- Compatibility between different systems
- Converting text to a specific byte representation

### A Security Note

If we only convert confidential information with Base64, that information is not secured.

For example, placing a password in Base64 does not provide any cryptographic protection.

**Rule:** Encoding is for representing data, not for keeping it confidential.

---

## 3. What Is Encryption?

**Encryption** is a process that, using a cryptographic algorithm and key, converts readable data into data that cannot be directly used without appropriate access to the key and decryption mechanism.

The main goal of Encryption is to protect information confidentiality.

The general process can be shown like this:

`Plaintext + Key → Encryption → Ciphertext`

To restore the data:

`Ciphertext + Key → Decryption → Plaintext`

For example, suppose we have a file containing sensitive information. We can encrypt it with an appropriate cryptographic algorithm so that someone who gains access to the file cannot read its content without the necessary key.

Of course, the security of this method depends on the algorithm, the way it is used, key management, and other implementation details.

### Encryption Alone Does Not Solve All Problems

If an attacker can also obtain the encryption key, they might be able to decrypt the information.

Also, Encryption alone does not guarantee that the data has not changed. For this purpose, we must use an appropriate tampering-detection mechanism.

---

## 4. Symmetric Encryption

In symmetric encryption, a shared key is usually used for both encryption and decryption.

General process:

1. The sender and receiver have access to the appropriate key.
2. The sender encrypts the data with the key.
3. The encrypted data is transmitted or stored.
4. The receiver decrypts it with the necessary key.

### Example: AES

**AES (Advanced Encryption Standard)** is one of the well-known symmetric encryption algorithms.

Uses of symmetric encryption include:

- Encrypting files
- Protecting stored data
- Encrypting communication data
- Protecting large amounts of information

### Main Advantage

Symmetric encryption is usually efficient for encrypting large amounts of data.

### Main Challenge: Key Management

The sender and receiver must have a secure way to obtain or share the key.

If the key is transmitted over an insecure path or stored in an inappropriate place, information security might be compromised.

### Encryption Modes and Data Authenticity

In the practical use of AES, choosing the appropriate mode matters greatly.

For encrypting new data, using an **Authenticated Encryption** method such as AES-GCM is usually recommended; because it provides both confidentiality and tamper detection.

In AES-GCM, correct use of the Nonce and preventing inappropriate repetition of it with a given key is very important.

Merely using the name AES does not guarantee that an implementation is secure.

---

## 5. Asymmetric Cryptography

In asymmetric cryptography, a related key pair is used:

- **Public Key**
- **Private Key**

The public key can be made available to others, but the private key must remain confidential.

In public-key cryptography applications, data encrypted for the recipient is usually decryptable only with the corresponding private key.

This explanation is a conceptual model; real protocols often use hybrid methods.

### Common Uses

- Secure key exchange
- Digital signatures
- Verifying service identities
- Public Key Infrastructure (PKI)
- Establishing secure communications

### Example: HTTPS

In HTTPS communications, digital certificates and cryptographic mechanisms are used to authenticate the service and establish a secure connection.

In modern protocols such as TLS, asymmetric cryptography is usually not used directly to encrypt all communication data; rather, key agreement and authentication mechanisms are used alongside symmetric encryption.

### The Difference Between Public and Private Keys

| Feature | Public Key | Private Key |
|---|---|---|
| Confidentiality | Can usually be published | Must remain confidential |
| Use | Depending on the algorithm, e.g. encryption or signature verification | Depending on the algorithm, e.g. decryption or signature creation |
| Its disclosure | Usually not considered a security secret by itself | Might compromise system security |

Note: In digital signatures, the private key is used to create the signature, and the corresponding public key is used to verify it. This process is not the same as encrypting data for confidentiality.

---

## 6. What Is Hashing?

**Hashing** is a process that converts data of arbitrary size into an output of a fixed size.

The function that performs this is called a **Hash Function**.

Conceptually:

`Input → Hash Function → Hash Digest`

For example, we can use a Hash function to compute a summary of a file's content.

If the file changes, the Hash output usually changes too. This property can be useful for verifying data integrity.

### Important Properties of a Cryptographic Hash Function

A suitable cryptographic hash function must have important security properties, including:

- Finding an input that has a specific Hash is computationally difficult.
- Finding a second input with the same Hash as a given input is difficult.
- Finding two different inputs with the same output is difficult.

These properties relate to concepts such as preimage resistance, second preimage resistance, and collision resistance, respectively.

### Common Algorithms

- SHA-256
- SHA-384
- SHA-512

MD5 and SHA-1, due to their known weaknesses in collision resistance, are not suitable choices for new security applications that require this property.

### Is Hash the Same as Encryption?

No.

Encryption is designed to encrypt data and usually can restore it with the appropriate key.

But Hashing is usually a one-way process and is not intended to directly recover the original input from the Hash.

| Feature | Encryption | Hashing |
|---|---|---|
| Main goal | Usually confidentiality | Summarizing and supporting integrity verification |
| Key | Usually uses a key | A regular Hash function does not require a key |
| Data recovery | Might be possible with the appropriate mechanism and key | For a regular Hash, direct recovery is not the intended goal |
| Output | Encrypted data | Digest or summary |

---

## 7. Why Is Hashing a Password Different from Hashing a File?

This difference is very important from a security perspective.

For verifying file changes, a function like SHA-256 can be useful.

But for storing user passwords, a general fast hash like SHA-256 alone is not suitable.

The reason is that an attacker can quickly test many possible passwords and compare their Hashes with the stolen values.

For storing passwords, we must use key-derivation methods designed for passwords, such as:

- Argon2id
- scrypt
- bcrypt
- PBKDF2

These methods are designed to make bulk testing of guesses more expensive.

### What Is Salt?

**Salt** is a value used uniquely for each stored password.

Salt helps ensure that identical passwords do not necessarily have identical stored outputs, and makes the reuse of precomputed tables harder.

Salt does not need to be confidential like a password, but must be generated and stored according to the algorithm's design.

In practice, a suitable password management library usually also manages the generation and storage of Salt.

**Rule:** Do not store passwords in plain text, and do not use a general fast hash alone to store them.

---

## 8. What Is HMAC?

A regular Hash alone cannot prove that a message was produced by a trusted individual or system.

Suppose an attacker can change both a file and the Hash stored next to it. In this case, a simple Hash comparison might not reveal the change.

**HMAC (Hash-based Message Authentication Code)** uses a Hash function and a shared key to enable verification of message authenticity and detection of tampering.

Conceptually:

`Message + Secret Key → HMAC`

A receiver who has the valid shared key can compute the expected value and compare it with the received value.

HMAC can help with:

- Verifying message integrity
- Confirming that the message was produced with the shared key
- Detecting unauthorized changes to data

However, HMAC alone does not provide confidentiality; for confidentiality, an appropriate encryption mechanism must be used.

Also, since both parties have the shared key, HMAC alone does not provide public and distinguishable identity proof like a digital signature.

---

## 9. Digital Signature

A digital signature is a cryptographic mechanism for verifying the authenticity and integrity of data.

In the common digital signature model:

1. The sender creates a signature with their private key.
2. The message and signature reach the receiver.
3. The receiver verifies the signature with the corresponding public key.

If the verification is valid, we can conclude that the signature was created with the corresponding private key, and that the verified data matches the signed data; of course, this conclusion depends on the security of the keys, the algorithm, and the implementation.

### Uses of Digital Signatures

- Software signing
- Verifying the authenticity of digital documents
- Verifying the integrity of software packages
- Message signing
- Digital certificates and public key infrastructure

### How Is a Signature Different from Encryption?

Digital signatures and encryption are designed for different purposes.

- Encryption is primarily used for confidentiality.
- A Digital Signature is used for verifying authenticity and integrity.

A digital signature does not by itself make a message's content confidential. If the message must also be confidential, an appropriate confidentiality protection mechanism must be used.

---

## 10. The Difference Between HMAC, Hashing, Encryption, Encoding, and Digital Signature

The following table summarizes the most important differences.

| Method | Main goal | Ability to recover original data | Key |
|---|---|---|---|
| Encoding | Representing or transmitting data | Usually yes | Usually none |
| Encryption | Confidentiality | With appropriate mechanism and key | Yes |
| Hashing | Producing a data summary and supporting integrity verification | Direct recovery is not the intended goal | Regular Hash does not require a key |
| HMAC | Message authenticity and integrity with a shared key | Does not encrypt data | Has a shared key |
| Digital Signature | Verifying authenticity and integrity | Does not encrypt data | Private and public keys |

These methods are sometimes used together in one system.

For example, a system might encrypt data, use HMAC on a message, or produce a digital signature for a software package. Choosing the right method depends on the security goal.

---

## 11. Working with Hash in Python

The Python standard library provides the `hashlib` module for computing common Hashes.

Example:

```python
import hashlib

message = b"Hello, security!"

digest = hashlib.sha256(message).hexdigest()

print(digest)
```

In this example:

- `hashlib` is the standard Hash computation module.
- `message` is of type `bytes`.
- `sha256()` creates a Hash object.
- `hexdigest()` converts the output into a string of hexadecimal digits.

### Why Do We Use `bytes`?

Hash functions operate on byte data.

If our data is a text string, we must convert it to bytes:

```python
text = "Hello, security!"
data = text.encode("utf-8")
```

Now we can pass `data` to the Hash function.

### Computing the Hash of a File

For large files, it is better to read the content in chunks, rather than placing the entire file in memory at once.

```python
import hashlib


def sha256_file(file_path: str) -> str:
    digest = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            digest.update(chunk)

    return digest.hexdigest()
```

In this function:

- The file is opened in binary mode.
- The content is read in chunks of 8192 bytes.
- Each chunk is added to the Hash object.
- Finally, the final Hash is returned.

This method uses less memory for large files.

### A Security Note

Computing a Hash alone does not guarantee a file's authenticity.

For example, if a file's Hash is received from a trusted source, it can be compared with the computed Hash.

But if an attacker can change both the file and the reference Hash, this comparison alone is not enough. In such cases, we might need a digital signature or another authenticity-verification mechanism.

---

## 12. How Cryptography Relates to Our Python Projects

The concepts of this lesson are widely used in our future security projects.

### Port Scanner

In the Port Scanner tool, we might in the future produce reports whose integrity needs to be verified.

Computing the report's Hash can help detect changes to the file relative to a reference value.

Of course, if we need to verify the report's authenticity, we must examine how the reference Hash is protected.

### DNS Lookup

In DNS Lookup, receiving a DNS record does not by itself mean verifying the authenticity or confidentiality of all related information.

DNS security depends on the protocol, settings, and the threat in question.

For example, DNSSEC can help verify the authenticity and integrity of DNS data, but does not by itself provide confidentiality of DNS queries.

This example shows that we must specify which security property we need, and then choose the appropriate control.

### Future Projects

The concepts of this lesson will be used in the following projects:

- Verifying file integrity
- Producing and verifying file Hashes
- Verifying digital signatures
- Working with encrypted data
- Securely managing passwords
- Examining communication security

---

## 13. Common Mistakes

### First Mistake: Thinking Base64 Is Encryption

Base64 is an Encoding method and is not designed to protect confidentiality.

### Second Mistake: Thinking a Hash Can Be Decrypted Like Encrypted Data

A regular Hash is not designed for direct input recovery.

### Third Mistake: Using a Simple SHA-256 for Storing Passwords

For storing passwords, specialized key-derivation methods such as Argon2id or scrypt must be used.

### Fourth Mistake: Thinking a Hash Alone Proves Authenticity

To verify authenticity, we must consider the trustworthiness of the reference value and the mechanism for producing or verifying it. HMAC and digital signatures cover this need in specific scenarios.

### Fifth Mistake: Thinking Encryption Provides All Security Properties

Encryption is important for confidentiality, but integrity, authenticity, key management, and access control must also be considered.

### Sixth Mistake: Thinking the Private Key Can Be Made Public

The private key must remain confidential. Its disclosure might compromise the security of mechanisms that depend on it.

---

## 14. Summary

In this lesson, we learned:

- Cryptography is a set of methods for protecting information and communications.
- Encoding is used for converting data format and does not provide confidentiality.
- Encryption is used for protecting data confidentiality.
- Symmetric encryption uses a shared key.
- Asymmetric encryption relies on a public and private key pair.
- Hashing produces a summary of data and can be used for verifying integrity.
- Storing passwords requires specialized methods such as Argon2id, scrypt, bcrypt, or PBKDF2.
- HMAC is used for verifying authenticity and integrity with a shared key.
- A digital signature enables verification of data authenticity and integrity.
- In Python, `hashlib` can be used to compute the Hash of data and files.

### Exercise

**First Exercise: Choosing the Right Method**

For each scenario, determine which method is more appropriate and why:

1. Converting binary data to a text format for transmission
2. Protecting the confidentiality of a file
3. Checking whether a file's content has changed compared to the reference version
4. Securely storing user passwords
5. Verifying the authenticity and integrity of a message using a shared key
6. Verifying the signature of a software package

**Second Exercise: Python**

Write a function named `sha256_text()` that receives a text string and returns its SHA-256 Hash.

Conditions:

- The function must convert the string to UTF-8.
- The output must be in Hex form.
- Use `hashlib` to compute the Hash.

**Third Exercise: Security Analysis**

Suppose a file and its SHA-256 value have been published on a website.

Explain:

- How do you compute and compare the file's Hash?
- Why does this comparison not necessarily prove the file's authenticity?
- How can a digital signature help verify authenticity?

