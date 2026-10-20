[🇮🇷 فارسی](/02-dns_lookup/docs/fa/03-cybersecurity-fundamentals/07-security-controls.md)

# Lesson 7: Security Controls

## 1. What Is a Security Control?

**Security Control** is any action, policy, process, or tool used to reduce security risks and protect assets.

Security controls help us:

- Prevent attacks from occurring.
- Detect suspicious activities.
- Reduce the impact of security incidents.
- Restore systems and information after an incident.
- Prevent unauthorized access to resources.

For example:

- Using a Firewall to limit network traffic
- Using Multi-Factor Authentication to protect accounts
- Logging events to files for activity review
- Preparing backups for information recovery
- Restricting users' access to sensitive files

These are all examples of security controls.

The important point is that no security control alone can eliminate all risks. The main goal is to reduce the likelihood of an incident and limit its impact.

---

## 2. Categorizing Security Controls by Function

One way to categorize controls is to consider what they do.

### 2.1. Preventive Controls

These controls are designed to prevent a security incident from occurring.

**Examples:**

- Firewall
- Multi-Factor Authentication (MFA)
- Restricting user access
- Disabling unnecessary services
- Enforcing strong password rules
- Validating application inputs

Suppose a server has services that should not be accessible from the Internet. A proper Firewall configuration can restrict unauthorized access to those services.

A preventive control does not necessarily stop an attack in all conditions, but it reduces its likelihood of success.

### 2.2. Detective Controls

These controls are used to identify suspicious activities or security incidents.

**Examples:**

- Logging and reviewing Logs
- Intrusion Detection Systems (IDS)
- Network traffic monitoring
- Alerts about failed login attempts
- Examining unexpected file changes
- Analyzing security events

For example, if a user account has many failed login attempts in a short time, a monitoring system can identify this behavior and issue an alert.

The important difference is that a detective control may not stop the attack; its main task is to detect the activity and provide the information necessary for response.

### 2.3. Corrective Controls

These controls are used after identifying a problem to fix it or limit its impact.

**Examples:**

- Correcting misconfigured Firewall settings
- Installing a security patch
- Removing an unauthorized user account
- Closing an unwanted port
- Cleaning malware from an infected system
- Fixing vulnerable application code

Suppose a security review shows that an unnecessary service is active on the server. Disabling that service can be a corrective action.

### 2.4. Deterrent Controls

The goal of these controls is to discourage individuals from engaging in malicious behavior.

**Examples:**

- Displaying a legal warning at login
- Announcing the presence of security monitoring
- Formal and transparent policies about the use of organizational resources
- Announcing the consequences of violating security policies

A deterrent control does not necessarily block an attack technically; rather, it attempts to reduce the likelihood of it being performed.

### 2.5. Compensating Controls

Sometimes implementing the ideal security control is not feasible. In such cases, an alternative control may be used that reduces part of the risk.

**Example:**

Suppose an old system does not support MFA. Until the system is replaced, network access to it can be restricted, user access can be reduced, and its activities can be monitored more carefully.

These actions may reduce risk, but they are not necessarily equivalent to MFA.

A compensating control must be evaluated against the actual risk; merely having an alternative control does not mean sufficient security.

### 2.6. Recovery Controls

These controls help restore systems and information to an operational state after an incident.

**Examples:**

- Backups
- Disaster Recovery Plan
- Alternative systems for critical services
- Database recovery process
- Periodic recovery exercises

For example, if a ransomware attack encrypts information, a healthy backup can help recover the data.

Of course, having a backup is not enough; we must also ensure that the versions are healthy and that they can actually be restored.

---

## 3. Categorizing Controls by Implementation Type

Another way to categorize security controls is to examine how they are implemented.

This categorization is different from the previous one:

- The previous categorization asked what the control does.
- This categorization asks how the control is implemented.

### 3.1. Administrative Controls

These controls include policies, rules, processes, and management decisions.

**Examples:**

- Access control policy
- Password policy
- Security awareness training for employees
- Background checks in the hiring process, where permitted
- Risk management process
- Incident response plan
- System change review and approval process

For example, an organization can define a policy that allows employees access to sensitive information only when there is a business need.

This policy is an administrative control; the tools that enforce it in the system may be technical controls.

### 3.2. Technical Controls

These controls use technology, software, or hardware to protect systems and information. They are sometimes called **Logical Controls**.

**Examples:**

- Firewall
- Intrusion Detection or Prevention System (IDS/IPS)
- Encryption
- Role-Based Access Control (RBAC)
- Antivirus and Endpoint Protection tools
- Logging security events
- Port scanning and configuration review tools

For example, the organization's policy might allow access to a server only for a specific team. The Firewall or an access control system can technically enforce part of this policy.

### 3.3. Physical Controls

These controls protect equipment, people, and the physical environment.

**Examples:**

- Door locks
- Server room access cards
- CCTV cameras
- Security guards
- Lockable racks or cabinets
- Fire alarm systems
- Temperature and humidity control equipment

For example, even if a server is well secured from a software perspective, unauthorized physical access to it can compromise the system's security.

That is why cybersecurity is not limited to software and networks.

---

## 4. How to Combine These Two Categorizations?

A single control can fall into both categorizations at the same time.

For example:

| Control | By Function | By Implementation |
|---|---|---|
| Firewall | Usually preventive | Technical |
| Logging and log analysis | Usually detective | Technical |
| Backup | Usually recovery | Technical |
| Security training | Can be preventive or deterrent | Administrative |
| Server room lock | Usually preventive | Physical |
| Applying security patch | Corrective | Technical |
| Restricting network access to an old system | May be compensating | Technical |

**Note:** The role of each control depends on how it is designed and used. For example, a Firewall might, in addition to preventing unauthorized traffic, produce Logs; but logging alone does not guarantee that malicious traffic is blocked.

---

## 5. How Security Controls Relate to the CIA Triad

In the second lesson, we became familiar with the three main principles of information security:

- **Confidentiality**
- **Integrity**
- **Availability**

Security controls can protect one or more of these principles.

### Confidentiality

The goal is to prevent information disclosure to unauthorized people.

Related controls:

- Encryption
- Authentication
- Access control
- Restricting file permissions
- Secure management of keys and secrets

### Integrity

The goal is to prevent unauthorized modification of information and to enable detecting invalid changes.

Related controls:

- Hashing to verify data changes
- Controlling write permissions
- Digital signatures
- Change logging
- Reviewing and approving important changes

Note that a hash alone does not guarantee the authenticity of data. If an attacker can change both the file and the stored hash, a simple hash check may not be sufficient. In some applications, a digital signature or HMAC is more appropriate.

### Availability

The goal is the availability of systems and information to authorized users.

Related controls:

- Backup
- Redundancy
- Service monitoring
- Disaster recovery plan
- Updating and maintaining systems
- Appropriate protection against denial-of-service attacks

One control can support multiple goals at the same time. For example, proper access management helps confidentiality and, in some situations, can also protect against unauthorized changes and thus integrity.

---

## 6. How Security Controls Relate to Our Python Projects

In this section, we will see how the tools we have built can play a role in the security process.

### 6.1. Port Scanner

The Port Scanner tool can help examine the accessibility of TCP ports.

Its defensive uses include:

- Identifying open ports on authorized systems
- Examining changes in the network access surface after applying Firewall rules
- Identifying services that are probably not supposed to be accessible
- Helping examine the network attack surface

For example, if a server's security policy says that only specific services should be accessible from the network, authorized scanning can help examine this state.

But we must remember the difference between these two:

- **Port Scanner:** shows us which ports are accessible from the scan location.
- **Firewall:** can be used to control and limit network traffic.

The scanner by itself is not a preventive control that blocks traffic; it is more of an examination and assessment tool.

Also, an open port by itself does not mean a vulnerability exists. The service, version, configuration, and actual need must be examined.

### 6.2. DNS Lookup

The DNS Lookup tool can retrieve information published in DNS; for example, A, AAAA, MX, and NS records.

Its defensive uses include:

- Examining the correctness of DNS records
- Helping troubleshoot domain-name issues
- Examining the DNS configuration of a domain under the organization's management
- Identifying information that has been unintentionally published in DNS
- Helping the asset inventory and documentation process

This tool is not by itself an access control or attack-prevention system; it is a tool for examining and observing information.

However, its results can help the security team decide which settings need to be corrected.

### 6.3. The Difference Between an Assessment Tool and a Security Control

This difference is very important for the rest of our journey.

| Item | Main Role |
|---|---|
| Port Scanner | Examining accessible ports |
| DNS Lookup | Examining DNS information |
| Firewall | Controlling network traffic |
| Authentication System | Verifying user identity |
| Logging System | Recording events |
| Backup System | Helping recover information |

An assessment tool may help identify a weakness, but it usually does not fix the weakness by itself.

**A security process usually includes these stages:**

1. Examining the system's state
2. Identifying the problem or risk
3. Choosing the appropriate control
4. Applying the control
5. Re-examining and assessing its effectiveness

For example, if the Port Scanner shows an unnecessary port, the corresponding service may need to be disabled or the Firewall rules corrected. After that, rescanning can be used to examine the result.

---

## 7. Is Using Multiple Controls Better?

In many cases, yes. Effective security usually requires a combination of controls.

Suppose we have an important server.

We can use the following controls:

- **Administrative control:** defining the access policy and the responsibilities of individuals
- **Preventive control:** restricting network and user access
- **Detective control:** logging and reviewing events
- **Corrective control:** installing patches and correcting insecure settings
- **Recovery control:** maintaining healthy backups
- **Physical control:** restricting access to the server room

This approach helps ensure that if one control fails, other controls still cover part of the risk.

This concept will be examined further in later lessons under the title **Defense in Depth**.

---

## 8. Common Mistakes

### First Mistake: Thinking Installing a Firewall Is Enough for Security

A Firewall is only part of the security solution. Access management, updates, monitoring, backups, and other controls are also important.

### Second Mistake: Equating Detection and Prevention

Detecting an attack does not necessarily mean preventing it. For example, logging a failed login attempt might record the attack, but it does not necessarily prevent further attempts.

### Third Mistake: Thinking Every Control Falls into Only One Category

A control can have multiple roles. For example, an access control system can prevent information disclosure and also log access events.

### Fourth Mistake: Thinking Having a Control Means Risk Is Eliminated

Every control may have limitations or weaknesses. After implementing a control, we must examine whether the risk has actually been reduced to an acceptable level.

### Fifth Mistake: Thinking the Scanning Tool Itself Solves the Problem

Scanning and examination tools usually reveal the state. Fixing the problem requires analysis, decision-making, and applying the appropriate change.

---

## 9. Summary

In this lesson, we learned:

- A security control is used to reduce risk and protect assets.
- By function, controls can be preventive, detective, corrective, deterrent, compensating, or recovery.
- By implementation type, controls can be administrative, technical, or physical.
- These two categorizations are different and should not be confused.
- Security controls can protect confidentiality, integrity, and availability.
- Port Scanner and DNS Lookup are assessment and examination tools and differ from controls like Firewall or access control systems.
- Effective security requires a combination of controls, continuous assessment, and fixing identified problems.

### Exercise

1. For each of the following items, determine its role by function and which category it falls into by implementation:

- Firewall
- Logging failed login attempts
- Backup
- Server room lock
- Security training for employees
- Applying a security patch

2. Suppose the Port Scanner shows an unexpected port on the organization's server. Explain:

- Why an open port alone is not proof of a vulnerability
- What additional information is needed for further examination
- Which controls might be appropriate for reducing the risk
- How the result can be examined after applying changes

3. Write a scenario in which at least three security controls are used to protect a server. Explain what each control protects against and what limitation it has.
