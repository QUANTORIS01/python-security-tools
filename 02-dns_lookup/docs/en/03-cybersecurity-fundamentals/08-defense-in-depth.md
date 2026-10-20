[🇮🇷 فارسی](/02-dns_lookup/docs/fa/03-cybersecurity-fundamentals/08-defense-in-depth.md)

# Lesson 8: Defense in Depth

## 1. What Is Defense in Depth?

**Defense in Depth** is a security approach in which, instead of relying on a single security control, we use multiple independent or complementary defensive layers.

The goal is that if an attacker bypasses one layer, the other layers can still:

- Prevent unauthorized access.
- Detect suspicious activity.
- Limit the spread of an attack.
- Protect important information.
- Make system recovery possible.

For example, suppose we have an Internet-facing server. If we rely only on a Firewall, a single configuration mistake in it might eliminate a significant part of the protection.

But if, in addition to the Firewall, we use strong authentication, software updates, access restrictions, event logging, and backups, the failure of one control does not necessarily mean the failure of the entire defense system.

**Key principle: security should not depend on the success of a single control.**

---

## 2. Why Do We Need Multiple Security Layers?

No security control is perfect. Every control may have its own limitations, configuration errors, or specific weaknesses.

The important reasons for using defense in depth include:

### 2.1. The Possibility of a Control Failing

A Firewall might be misconfigured or a rule might create excessive access.

In such conditions, other controls such as strong authentication and user access restrictions can still prevent some unauthorized access.

### 2.2. The Existence of Unknown Vulnerabilities

Sometimes a software has a vulnerability that has not yet been identified or fixed.

Software updates are very important, but controls such as restricting network access, reducing a service's privilege level, and monitoring can also limit the impact of an attack.

### 2.3. Reducing the Impact of an Attack

Sometimes fully preventing an attacker from entering is not feasible. In these conditions, we must prevent the attacker from accessing other parts of the system and sensitive data.

For example, if a user account is compromised, the limited permissions of that account can reduce the extent of the damage.

### 2.4. Increasing the Likelihood of Detecting an Attack

An attack might bypass a preventive control, but the attacker's behavior might be visible in Logs or monitoring systems.

In this case, a detective control can help discover the incident and begin the response process.

---

## 3. The Main Layers of Security Defense

Defense in depth does not have a single fixed architecture. The appropriate layers depend on the type of system, the threats, and the level of risk.

However, we can examine several common layers.

### 3.1. The Policy and Process Layer

This layer specifies how security should be managed.

Examples:

- Access control policy
- Security patch management process
- Incident response plan
- Security awareness training
- Backup preparation and testing process

Without clear processes, even appropriate technical tools might not be used correctly.

### 3.2. The Physical Layer

The goal of this layer is to protect equipment and the physical environment.

Examples:

- Server room locks
- Access cards
- CCTV cameras
- Protecting network equipment
- Controlling access to the backup storage location

If an attacker can access equipment directly, they might bypass some software controls or compromise information.

### 3.3. The Network Layer

This layer controls and examines network communications.

Examples:

- Firewall
- Network Segmentation
- Restricting accessible ports
- VPN for specific accesses
- IDS/IPS
- Network traffic monitoring

The goal is to reduce unnecessary communications, restrict access paths, and detect suspicious activities.

### 3.4. The Operating System and Host Layer

This layer protects servers and endpoint systems.

Examples:

- Installing security patches
- Disabling unnecessary services
- Setting file permissions
- Using host-protection tools
- Logging system events
- Running services with minimum necessary privileges

### 3.5. The Application Layer

This layer relates to the security of software and services running on the system.

Examples:

- Input validation
- Preventing SQL injection
- Secure session management
- Checking access permissions on the server side
- Secure secret management
- Updating software dependencies

Network security alone does not guarantee that the application running on that network is secure.

### 3.6. The Identity and Access Layer

This layer specifies who is allowed to use which resource and at what level of access.

Examples:

- Multi-Factor Authentication (MFA)
- Role-Based Access Control (RBAC)
- Least Privilege principle
- Removing or disabling unnecessary accounts
- Periodic review of permissions

### 3.7. The Data Layer

This layer directly protects information.

Examples:

- Encrypting sensitive data
- Controlling read and write permissions
- Preparing backups
- Examining data integrity
- Securely deleting information that is no longer needed
- Restricting access to encryption keys

Even if one of the other layers fails, appropriate data controls can prevent the disclosure or destruction of part of the information.

### 3.8. The Monitoring and Response Layer

This layer is important for detecting incidents and reacting to them.

Examples:

- Collecting and analyzing Logs
- Security alert system
- Examining unusual behaviors
- Incident response process
- Preserving incident-related evidence
- Restoring the system after fixing the problem

Security is not just preventing attacks; the ability to detect and manage incidents is also part of it.

---

## 4. A Practical Example: Protecting a Web Server

Suppose an organization has a web server that must be accessible from the Internet.

This server might include:

- Operating System
- Web Server
- Web Application
- Database
- User Information

If we want to protect this server, we can design multiple defensive layers.

| Layer | Sample Control | Goal |
|---|---|---|
| Network | Firewall | Restricting unnecessary traffic |
| Network | Network Segmentation | Limiting communication between parts |
| Operating System | Installing patches | Reducing the risk of known vulnerabilities |
| Application | Input validation | Reducing the risk of malicious inputs |
| Identity | MFA for administrative accounts | Making account exploitation harder |
| Access | Least Privilege | Limiting damage from unauthorized access |
| Data | Encrypting sensitive information | Protecting data confidentiality |
| Monitoring | Logging and reviewing Logs | Detecting suspicious behavior |
| Recovery | Tested backup | Enabling information recovery after an incident |

These layers are not substitutes for each other; they work together to cover different risks.

For example, data encryption does not necessarily prevent the misuse of an authorized account. On the other hand, MFA alone does not protect data against accidental deletion or hardware failure.

Therefore, we must choose controls according to different threats.

---

## 5. The Principle of Least Privilege and Its Relation to Defense in Depth

One of the important principles in designing security layers is **Least Privilege**.

This principle says that every user, program, or service should have only the minimum access needed to perform its task.

### Example

Suppose a web application should only read information from a database.

If the database account of this application also has permission to delete tables or create administrative accounts, exploiting the application might cause more damage.

But if the application's account has only the permission to read the required information, part of the potential impact of an attack is limited.

The Least Privilege principle can be applied at several levels:

- User accounts
- Administrative accounts
- Operating system services
- Applications and processes
- File access
- Network access
- API access

This principle does not make an attack impossible, but it can reduce the extent of the damage.

---

## 6. How Defense in Depth Relates to Our Python Projects

In the projects `01-port_scanner` and `02-dns_lookup`, we have built tools that support part of the security examination process.

### 6.1. The Role of the Port Scanner

The Port Scanner can help examine the network access surface.

For example, after configuring a Firewall, we can re-examine the port state on a system we are authorized to examine.

This helps answer questions such as:

- Is the target port still accessible?
- Is any unexpected port observed?
- Does the result match the network policy?

But port scanning alone cannot verify the security of the entire network. This tool provides a limited view of the port state from the scan execution location.

### 6.2. The Role of DNS Lookup

DNS Lookup helps us examine the DNS information of a domain.

For example, in a domain under our own management, we can examine:

- What information do the DNS records publish?
- Do the important records exist?
- Does the observed information match the expected settings?
- Does any record need to be corrected or removed?

However, DNS Lookup does not examine all security layers and cannot guarantee the security of a domain or server on its own.

### 6.3. How to Use These Tools in a Defense-in-Depth Process?

A simple procedure could be:

1. **Understanding Assets:** Identify which domains, servers, and services are under our management.

2. **Examining the State:** Use tools such as DNS Lookup and Port Scanner to gather the necessary information.

3. **Assessing Risk:** Compare the results with the actual needs of the system and security policies.

4. **Applying the Appropriate Control:** If necessary, correct the Firewall settings, disable unnecessary services, or restrict access.

5. **Re-Examining:** Test again to see whether the intended changes have been applied.

6. **Continuous Monitoring:** In addition to periodic reviews, examine Logs and security alerts.

This procedure shows that examination tools are part of a larger security process; they are not substitutes for all security controls.

---

## 7. How Does Defense in Depth Differ from Using Many Tools?

Using a large number of security tools does not necessarily mean effective defense in depth.

For example, an organization might have several scanning tools installed, but:

- Unnecessary accesses might still be active.
- Security patches might not be installed.
- Logs might not be reviewed.
- Backups might not be restorable.
- Incident response responsibilities might not be defined.

In this case, the number of tools is large, but security coverage might still be incomplete.

Effective defense in depth requires:

- Understanding assets and threats
- Choosing controls appropriate to the risk
- Covering different weaknesses
- Coordination among controls
- Continuous monitoring and testing
- Reviewing and fixing identified problems

**Important principle:** the quality, coverage, and coordination of controls are more important than the number of installed tools.

---

## 8. Limitations of Defense in Depth

Defense in depth reduces risk, but does not eliminate it completely.

### Greater Complexity

Each layer may require configuration, maintenance, and monitoring.

### Misconfiguration

If several controls are configured incorrectly, they might all be ineffective against a specific scenario.

### Shared Dependency

Sometimes several apparently different layers depend on the same administrative account, service, or infrastructure. If that part is compromised, several layers might be affected simultaneously.

### Cost and Resources

Implementing each control requires cost and human resources. Therefore, the choice of controls should be based on the importance of the assets and the level of risk.

### False Confidence

Having several controls should not cause the organization to abandon testing, assessment, and continuous improvement.

---

## 9. Summary

In this lesson, we learned:

- Defense in Depth means using multiple complementary defensive layers.
- The failure of one control should not automatically cause the failure of the entire security system.
- Defensive layers can include network, operating system, application, identity, data, physical security, and monitoring.
- The Least Privilege principle helps limit the extent of the damage.
- Port Scanner and DNS Lookup can be useful in examining the state and assessing some risks, but they are not substitutes for preventive controls and other defensive layers.
- Effective defense in depth requires proper selection of controls, appropriate configuration, monitoring, and continuous assessment.

### Exercise

**First Exercise: Designing Defensive Layers**

Suppose we have a web server that also has a database.

Choose at least five security controls and explain for each:

- Which layer does it belong to?
- What asset or what does it protect?
- What type of risk is it useful against?
- What limitation does it have?

**Second Exercise: Analyzing an Incident**

Suppose an attacker has gained access to a user account.

Explain how the following controls can help reduce the damage:

- MFA
- Least Privilege
- Logging and reviewing Logs
- Network Segmentation
- Backup

Note that MFA might have been bypassed in this scenario, or the account might have been compromised through another path; therefore, you should also examine the role of other controls.

**Third Exercise: Our Own Projects**

Imagine the Port Scanner shows an unexpected port on an authorized test server.

Design a multi-stage defensive process that includes examination, risk assessment, choosing a control, applying a change, and verifying the result.
