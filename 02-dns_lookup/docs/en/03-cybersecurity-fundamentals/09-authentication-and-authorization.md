[🇮🇷 فارسی](/02-dns_lookup/docs/fa/03-cybersecurity-fundamentals/09-authentication-and-authorization.md)

# Lesson 9: Authentication and Authorization

## 1. Introduction

In any secure system, we must be able to answer two fundamental questions:

1. **Who are you?**
2. **What are you allowed to do?**

These two questions relate to two different concepts:

- **Authentication:** verifying the identity of a user or system
- **Authorization:** determining which resources and operations an authenticated user or system is allowed to access

These two concepts are related, but not the same.

### A Simple Example

Suppose you enter an office building.

- Showing an ID card to verify your identity is similar to Authentication.
- Checking whether you are allowed to enter the server room is similar to Authorization.

Your identity might be verified, but you may not be allowed to enter the server room.

The same principle applies in computer systems.

---

## 2. Authentication

**Authentication** is the process by which a system verifies that a user, device, or service really has the identity it claims.

For example, the user enters the username `alice`. The system must have a way to verify that the request really comes from the owner of that account.

### Common Authentication Methods

#### 2.1. Something You Know

Information that the user knows.

Examples:

- Password
- PIN
- Answer to a security challenge, in systems that are properly designed

Passwords are a common authentication method, but using weak or reused passwords can create security risks.

#### 2.2. Something You Have

A device or factor that the user possesses.

Examples:

- A hardware security key
- An app that generates one-time codes
- A device registered to receive or approve authentication requests

Of course, merely having a device or receiving an SMS does not mean complete security; security depends on the implementation and the existing threats.

#### 2.3. Something You Are

Biological characteristics of the individual.

Examples:

- Fingerprint
- Face recognition
- Some other biometric methods

These methods also have limitations. For example, recognition may be incorrect, and biometric data cannot be changed as easily as a password.

### Multi-Factor Authentication (MFA)

**Multi-Factor Authentication (MFA)** uses two or more authentication factors from different categories.

For example, combining a password with a security key can be stronger than a single factor.

An important point is that using two different passwords alone is not considered MFA; both belong to the same category: something we know.

---

## 3. Authorization

After the identity is determined, the system must decide which operations that identity is allowed to perform.

This decision-making is called **Authorization**.

For example, in a file management system:

- The first user can view files.
- The second user can view and edit files.
- The system administrator can manage users.

All three users might be successfully authenticated, but have different permissions.

### Resources and Actions

Authorization usually specifies which operations an identity can perform on a resource.

**Resources:**

- Files
- Folders
- Database records
- APIs
- Servers
- System settings

**Actions:**

- Read
- Create
- Update
- Delete
- Execute
- Manage Users

For example, a user might be allowed to view a report but not allowed to delete it.

---

## 4. The Difference Between Authentication and Authorization

| Feature | Authentication | Authorization |
|---|---|---|
| Main question | Who are you? | What are you allowed to do? |
| Goal | Verifying identity | Checking access permission |
| Typical execution time | Before deciding about access | When determining or checking access |
| Example | Verifying a password | Checking permission to delete a file |
| Possible failure | Identity is not verified | Identity is known, but the operation is not allowed |

In many systems, authentication is performed first, and then permissions are checked.

However, the details depend on the system design. Some resources are public and do not require authentication; others may enforce specific policies to limit requests before authentication.

### Example

Suppose the user `alice` logs into an application.

1. Her username and authentication credential are checked.
2. The system verifies her identity.
3. The user sends a request to delete a report.
4. The application checks whether `alice` has permission to delete that report.

If the fourth step fails, the user should not be able to delete the report, even if their authentication was completely successful.

---

## 5. The Principle of Least Privilege

**Least Privilege** is one of the important principles of access control.

According to this principle, each user, program, or service should have only the minimum permissions needed to perform its task.

### Example

Suppose an application only needs to read user information from a database.

If the database account used by the application also has permission to delete tables, modify the database structure, and create new users, a vulnerability in the application could cause more damage.

But if this account only has permission to read the required information, the scope of some attacks is limited.

### Uses of Least Privilege

- Using a regular account for daily tasks
- Limiting the number of Administrator accounts
- Setting precise permissions for files
- Restricting program access to databases
- Restricting API permissions
- Removing unnecessary permissions
- Periodically reviewing user access

The Least Privilege principle alone does not prevent all attacks, but it can reduce the impact of many errors and abuses.

---

## 6. Common Access Control Models

Systems use different models to decide about permissions.

### 6.1. Role-Based Access Control (RBAC)

**Role-Based Access Control** determines access based on the user's role.

For example:

| Role | View report | Edit report | Manage users |
|---|---|---|---|
| Viewer | Yes | No | No |
| Editor | Yes | Yes | No |
| Admin | Yes | Yes | Yes |

Instead of assigning permissions individually to each user, permissions are assigned to roles and users receive the appropriate role.

This approach can simplify access management in organizations with many users and resources.

Of course, if a user receives excessive roles, they might gain unnecessary access.

### 6.2. Attribute-Based Access Control (ABAC)

**Attribute-Based Access Control** makes access decisions based on various attributes.

These attributes might include:

- User identity
- User role
- Resource type
- Request time
- Device location or state
- Information sensitivity
- Environmental conditions

For example, a system might allow access to a sensitive document only when the user is authorized and the request is made from an approved device.

ABAC is flexible for complex policies, but its proper design and review are also very important.

### 6.3. Access Control List (ACL)

**Access Control List** defines a set of permissions for a specific resource.

For example, a file might have the following policy:

- `alice`: read and write
- `bob`: read only
- `charlie`: no access

ACLs are used in operating systems, file systems, and some network systems.

### General Difference

- **RBAC:** decision based on role
- **ABAC:** decision based on attributes and conditions
- **ACL:** list of permissions associated with a resource

These models are not necessarily competitors; a system can use a combination of them.

---

## 7. Access Control in Web Applications and APIs

In web applications, there must be a clear distinction between authentication and authorization.

Suppose an API provides user information.

A request might contain a valid Token. This Token can be used to determine identity or identity-related information, but its validity does not mean the user is allowed to view information about all users.

The application must also check permission to access the requested resource.

### A Sample Security Flaw

Suppose a user with ID `101` has logged in and sends the following request:

`GET /api/users/202`

If the application only checks that the user is logged in and then returns information about user ID `202` without checking permission, information about another user might be disclosed.

This type of problem can be an example of **Broken Access Control** and, in the case of access to objects belonging to other users, it relates to the concept of **IDOR (Insecure Direct Object Reference)**.

### Methods for Reducing Risk

- Checking permission on the server side
- Checking access to each resource, not just the initial login
- Restricting access to sensitive information
- Using specific authorization policies
- Testing access with multiple user accounts
- Logging sensitive events
- Avoiding trusting an identifier the user sends in the request

**Important note:** hiding a button or page in the user interface is not a substitute for checking permission on the server side.

---

## 8. Passwords and Secure Storage of Authentication Information

If an application stores user passwords, it should not keep them in plain text.

In standard systems, passwords should be stored using an appropriate key-derivation algorithm designed for passwords, along with a unique Salt; such as:

- Argon2id
- scrypt
- bcrypt
- PBKDF2

Choosing and configuring the appropriate algorithm matters. Using a general fast hash like SHA-256 alone is not a suitable method for storing passwords.

Also:

- Passwords should not be logged.
- Sensitive information should not be placed inside source code.
- Tokens and access keys must be carefully protected.
- Sensitive communications should use a secure channel.
- The account recovery process must also be reviewed from a security perspective.

Secure authentication is not limited to choosing a login method; managing the lifecycle of authentication information also matters.

---

## 9. How These Concepts Relate to Our Python Tools

The projects `01-port_scanner` and `02-dns_lookup` are network assessment tools. They are not necessarily a complete authentication or authorization system.

However, these concepts matter in how we develop and use our tools.

### 9.1. Permission to Perform Operations

Suppose that in the future, our scanning tool could be used by multiple users in an organizational environment.

We must specify:

- Who is allowed to run scans?
- Who is allowed to change settings?
- Who can view the results?
- Who is allowed to delete reports?

Authentication can determine the user's identity, and authorization determines which operations they are allowed to perform.

### 9.2. Restricting Access

If the tool is designed for only one specific task, it should not need system administrative access without reason.

Running the tool with the minimum necessary privileges can reduce the risk of errors from program bugs or unexpected inputs.

### 9.3. Responsible Use of Tools

Network scanning should be performed within the scope of systems we are authorized to examine.

Authentication in one system does not by itself create permission to scan all hosts on the network. Operational authorization must be determined based on policies and actual authority.

---

## 10. Common Mistakes

### First Mistake: Treating Authentication and Authorization as the Same

Verifying a user's identity does not mean all of their operations are authorized.

### Second Mistake: Fully Trusting a Successful Login

After a user logs in, every sensitive request must be checked according to authorization policies.

### Third Mistake: Checking Permission Only in the User Interface

An attacker might send API requests directly. Access checks must be performed on the server side.

### Fourth Mistake: Giving Administrative Access to All Users

Excessive access increases the likelihood and extent of damage from errors or abuse.

### Fifth Mistake: Assuming a Valid Token Means Access to All Resources

A valid Token might indicate identity or some user attributes; but the application must also check permission to access the resource and operation in question according to its policy.

---

## 11. Summary

In this lesson, we learned:

- Authentication is for verifying identity.
- Authorization is for determining access permission.
- Successful authentication does not mean all operations are authorized.
- MFA uses multiple different authentication factors.
- The Least Privilege principle restricts access to the minimum necessary.
- RBAC, ABAC, and ACL are methods for managing access.
- Web applications and APIs must check access permission to resources on the server side.
- Secure storage of passwords and Tokens is an important part of authentication security.

### Exercise

**First Exercise: Identifying the Concept**

For each item, determine whether it relates to Authentication, Authorization, or both:

1. Verifying a user's password
2. Checking permission to delete a file
3. Using a security key to log in
4. Checking whether a user is allowed to view a financial report
5. Restricting a user to viewing only their own information

**Second Exercise: Analyzing an API**

Suppose an API returns user information by their ID.

The user is authenticated, but can include other users' IDs in the request.

Explain:

- What is the security problem?
- Why is Authentication alone not enough?
- What permission should the application check?
- How can this problem be examined with automated tests?

**Third Exercise: Least Privilege**

Suppose a Python application only needs to read records from a database.

Explain why granting permission to delete tables to this application's account is dangerous, and how its access can be restricted.
