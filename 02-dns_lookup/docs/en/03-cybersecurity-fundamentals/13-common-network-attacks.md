[🇮🇷 فارسی](/02-dns_lookup/docs/fa/03-cybersecurity-fundamentals/13-common-network-attacks.md)

# Lesson 13: Common Network Attacks

## 1. Introduction

Networks are designed to enable communication between systems, users, and services; but these very communications might be abused.

A **Network Attack** is a deliberate attempt to disrupt communications, gain unauthorized access to resources, steal information, or abuse network services.

Network attacks have different goals:

- Identifying the target's services and infrastructure
- Unauthorized access to accounts or systems
- Eavesdropping or tampering with communications
- Making services unavailable
- Moving from a compromised system to other parts of the network

For security analysis, it is necessary to distinguish between three topics:

- **Attack Technique:** the method or technique used by the attacker.
- **Indicator:** a sign that might indicate suspicious activity.
- **Mitigation:** an action or control that reduces the likelihood or impact of an attack.

Observing an indicator alone does not always prove that an attack has occurred. The evidence and environment conditions must also be examined.

---

## 2. Port Scanning

### 2.1. What Is Port Scanning?

In port scanning, the status of a host's ports is examined to determine which ports are accessible or might have services listening on them.

Port scanning might be part of an attacker's reconnaissance activity; but it also has completely legal and defensive uses, such as reviewing the access surface of an organization's server services.

### 2.2. Why Does an Attacker Scan Ports?

An attacker might want to find out:

- What services are accessible?
- Which services are accessible from the Internet?
- Is an unnecessary administrative service exposed to access?
- Which systems are more important for further examination?

Port scanning by itself does not mean intrusion.

### 2.3. Common Port States

| State | Meaning |
|---|---|
| Open | A connection to the port is possible, and a program is usually listening on it. |
| Closed | The host responds, but no active service is accessible on that port. |
| Filtered | Network filtering or lack of sufficient response prevents determining the definitive state. |

The precise interpretation of these states depends on the scanning method, the protocol, and the host's behavior.

### 2.4. Possible Indicators of Scanning

- A large number of connections to different ports in a short time
- Attempts to access various ports on a host
- Attempts to connect to multiple hosts from one source
- An unusual increase in failed connections

These indicators might also have harmless causes; for example, monitoring tools or authorized organizational scans.

### 2.5. Defensive Measures

- Keep only necessary services active.
- Restrict access to administrative ports.
- Review firewall rules.
- Log and review connection attempts in proportion to the environment's needs.
- Periodically perform authorized scans of the organization's assets.

### Connection to the Python Project

The `Port Scanner` tool we have built can be used to examine specific ports in an authorized environment.

But you must remember:

**An open port, by itself, does not prove a vulnerability.**

For a security assessment, the service, version, settings, business need, and security patch status must also be examined.

---

## 3. Brute Force Attack

### 3.1. What Is Brute Force?

In a **Brute Force** attack, the attacker tries to obtain a password or confidential value by testing a large number of possible combinations.

This attempt might be made against items such as:

- An application login account
- A remote access service
- An administrative panel
- Keys or confidential values that have a limited search space

The success of the attack depends on factors such as password length and complexity, system restrictions, and the ability to repeat attempts.

### 3.2. The Difference Between Brute Force and Dictionary Attack

**Brute Force**

Examines possible combinations broadly.

**Dictionary Attack**

Uses a list of passwords or likely values; for example, common passwords or combinations that are more likely to be used.

In practice, password guessing methods can be a combination of these two approaches.

### 3.3. What Is Password Spraying?

In **Password Spraying**, one or a few common passwords are tested on many accounts, instead of focusing many attempts on one account.

This method might be used to bypass restrictions that detect a large number of failed attempts for one account.

### 3.4. Possible Indicators

- An increase in failed logins
- Attempts to log into multiple accounts from one source
- Unusual logins at different times or locations
- An increase in login attempts to administrative services
- A successful login after a series of suspicious attempts

None of these indicators alone is definitive proof of an attack.

### 3.5. Defensive Measures

- Using strong and unique passwords
- Enabling MFA
- Limiting the rate of login attempts
- Using increasing delays or account lockout policies, considering the risk of account lockout abuse
- Monitoring and alerting on unusual behaviors
- Restricting administrative access through the network
- Using secure password management and storage methods

To prevent attackers from locking users' accounts, the login restriction policy must be designed carefully.

---

## 4. DoS and DDoS Attacks

### 4.1. What Is DoS?

**Denial of Service (DoS)** is an attack whose goal is to reduce or eliminate the availability of a service.

For example, a service might be unable to respond to real users due to excessive requests or excessive resource consumption.

### 4.2. What Is DDoS?

**Distributed Denial of Service (DDoS)** is a type of denial-of-service attack in which traffic or requests are generated from a large number of distributed systems or sources.

The distributed nature of the attack can make its detection and mitigation harder.

### 4.3. General Types of Attacks

**Volumetric Attacks**

The goal is to saturate communication capacity with a large volume of traffic.

**Protocol-based Attacks**

The goal is to consume network resources or intermediate equipment through specific protocol behaviors.

**Application-layer Attacks**

In this case, requests are sent to an application service whose processing can consume a lot of resources.

These attacks are not necessarily accompanied by a very large volume of traffic; even a smaller number of expensive requests might cause a problem.

### 4.4. Possible Indicators

- A sudden increase in incoming traffic
- An increase in service response latency
- An increase in Timeout errors
- High CPU or memory usage
- An unusual increase in the number of requests
- A reduction in availability for real users

An increase in traffic is not always a sign of attack; events such as a real increase in users can also have this effect.

### 4.5. Defensive Measures

- Using DDoS protection services
- Rate limiting requests in proportion to the type of service
- Using a CDN or traffic distribution systems, if appropriate
- Monitoring traffic and system resources
- Designing appropriate capacity and redundancy
- Defining an incident response plan
- Coordinating with the Internet service provider or hosting service in major incidents

A regular firewall alone is not enough to counter all types of DDoS.

---

## 5. Man-in-the-Middle (MitM) Attacks

### 5.1. What Is MitM?

In a **Man-in-the-Middle** attack, the attacker tries to place themselves in the path of two parties' communication or control the communication in a way that allows them to observe or change data.

For example, in an insecure scenario, the user might think they are communicating directly with a service, while the attacker is in the communication path.

The success of such an attack depends on network conditions, the authentication method, and communication protection.

### 5.2. Possible Risks

- Disclosure of sensitive information
- Credential theft
- Tampering with transmitted data
- Redirecting the user to an unexpected destination
- Forging or abusing trust between two parties

### 5.3. Defensive Measures

- Correct use of HTTPS and TLS
- Verifying digital certificates
- Avoiding ignoring certificate warnings
- Using a valid VPN in appropriate scenarios
- Using MFA
- Protecting wireless networks
- Updating the operating system and software

**Note:** The presence of HTTPS reduces the likelihood of eavesdropping and communication tampering, but does not guarantee the security of the entire application. For example, a vulnerability in the application itself or the theft of the user's session can still pose a risk.

---

## 6. Spoofing (Address and Identity Forgery)

### 6.1. What Is Spoofing?

**Spoofing** refers to forging identity information or source specifications so that communication or data appears trustworthy.

This concept has different types, and each type requires different defensive controls.

### 6.2. IP Spoofing

In **IP Spoofing**, the source IP address in packets is forged.

This can be used in some attacks to hide the true source or to abuse address-based trust.

However, IP address forgery alone does not mean the attacker can also receive the communication responses or establish a normal two-way connection.

### 6.3. DNS Spoofing

In attacks related to **DNS Spoofing**, an attempt is made to provide an incorrect or misleading DNS response to a system or user.

The possible consequence is redirecting the user to the wrong address.

The attack methods can vary and might relate to configuration weaknesses, the Resolver's state, or the communication path.

### 6.4. Email Spoofing

In **Email Spoofing**, the sender information of an email is forged in a way that the message appears to come from another source.

Organizations can reduce some abuses related to sender domain forgery by properly configuring mechanisms such as SPF, DKIM, and DMARC.

These mechanisms do not eliminate all types of phishing or identity forgery.

### 6.5. General Defensive Measures

- Use valid authentication.
- Do not trust source information alone.
- Configure DNS Resolvers and network settings properly.
- Use appropriate anti-spoofing controls at the network boundary.
- Protect sensitive communications with secure protocols.
- Perform validation at the application layer as well.

---

## 7. DNS Amplification Attack

### 7.1. General Concept

**DNS Amplification** is one type of DDoS attack that abuses the difference between the request size and the response size in certain conditions.

In an abuse scenario, requests are forged with the victim's IP address, and larger responses are directed toward the victim.

This attack usually depends on abusable DNS infrastructure and the ability to forge the source address.

### 7.2. Why Is This Attack Dangerous?

If the responses are much larger than the requests, the volume of traffic sent to the victim can increase and put pressure on its communication resources.

### 7.3. Defensive Measures

- Preventing the organization's Resolver from becoming an open and abusable service for the public
- Restricting access to internal Resolvers
- Using address anti-spoofing controls in the network
- Monitoring unusual DNS traffic patterns
- Cooperating with the network provider to mitigate the attack's impact

### Connection to DNS Lookup

The `DNS Lookup` tool is used for querying and examining DNS records.

This tool alone cannot prove that a DNS Server is vulnerable to DNS Amplification or is participating in an attack.

Such an assessment requires examining the server configuration, access policy, and traffic evidence.

---

## 8. Lateral Movement

### 8.1. Concept

After initial access to a system, the attacker might try to use that system to access other systems on the network.

This process is called **Lateral Movement**.

For example, if a user account has excessive access, compromising one device might open a path to more sensitive resources.

### 8.2. Factors That Increase Risk

- Shared passwords between systems
- Excessive administrative access
- Flat network without proper segmentation
- Administrative services accessible from unnecessary segments
- Inadequate monitoring
- Insecurely stored credentials

### 8.3. Defensive Measures

- Network segmentation
- Applying the Least Privilege principle
- Using separate administrative accounts
- Protecting credentials and sessions
- Restricting administrative access
- Logging and reviewing login and access events
- Updating and hardening systems

The goal is that if one system is compromised, the possibility of the incident spreading to other segments is reduced.

---

## 9. Phishing and Social Engineering

Not all attacks start through a technical network flaw. Sometimes the attacker tries to deceive the user into giving them access or sensitive information themselves.

### 9.1. What Is Phishing?

**Phishing** is a type of social engineering in which the attacker uses a deceptive message, email, or page to persuade the user to disclose information or perform an unwanted action.

Sample targets:

- Password
- Verification code
- Session token
- Payment information
- Confidential file or document

### 9.2. Possible Phishing Indicators

- A domain similar to the main domain but different
- An unexpected request for sensitive information
- Creating a sense of urgency or threat
- An unexpected attachment or link
- A mismatch between the claimed identity and the actual destination

However, the presence of spelling errors or an unprofessional appearance is not a necessary condition for phishing; fake messages can be very convincing.

### 9.3. Defensive Measures

- Examining the destination of links and domains
- Not entering passwords or verification codes on suspicious pages
- Using phishing-resistant MFA, where possible
- Reporting suspicious messages
- Using a password manager
- Training users and implementing approval processes for sensitive requests

---

## 10. Comparing Attacks and Related Defenses

| Attack | Possible goal or effect | Sample defensive controls |
|---|---|---|
| Port Scanning | Identifying accessible services | Access restriction, removing unnecessary services, monitoring |
| Brute Force | Guessing a password or confidential value | MFA, rate limiting, strong passwords, monitoring |
| DoS/DDoS | Reducing service availability | DDoS protection, capacity management, traffic monitoring |
| Man-in-the-Middle | Observing or tampering with communication | Proper TLS, certificate validation, network protection |
| Spoofing | Forging source specifications or identity | Authentication, anti-spoofing controls, validation |
| DNS Amplification | Saturating the victim's communication resources | Secure Resolver, anti-spoofing controls, DNS monitoring |
| Lateral Movement | Expanding access within the network | Segmentation, Least Privilege, monitoring |
| Phishing | Deceiving the user and stealing information | Training, phishing-resistant MFA, reporting |

No single control is sufficient for all scenarios. Effective defense usually requires multiple layers of control and continuous review.

---

## 11. Practical Exercises

Perform the exercises only in a personal environment, a laboratory, or a scope you are authorized to examine.

### Exercise 1: Analyzing a Port Scanner Result

Review the output of an authorized scan and answer the following questions:

1. Which ports were accessible?
2. Which services should be accessible from the scan location?
3. Which ports require further examination?
4. What other evidence is needed to determine whether a vulnerability exists?

The goal is to draw precise conclusions from evidence, not to assume that every open port is a security problem.

### Exercise 2: Analyzing Login Attempts

Suppose a large number of failed logins for several accounts have been recorded in a service's report.

Determine:

- What information is needed for examination?
- Did the attempts come from one source or several?
- Did any successful login occur after the failed attempts?
- What factors might legally produce similar behavior?
- What actions are appropriate for reducing the risk?

### Exercise 3: Designing an Access Policy

For a hypothetical server, consider these services:

- Web server
- SSH for management
- Database

Design an access policy that specifies:

- Which service should be accessible from the Internet?
- Which service should be accessible only from the management network?
- Which service should only accept connections from the application server?

For each rule, write the security rationale.

### Exercise 4: Examining DDoS Risk

For a hypothetical website, define three indicators that might indicate disruption due to unusual traffic.

Then explain how to distinguish between a real increase in users and a possible attack.

### Exercise 5: Building a Defensive Checklist

Write a checklist for protecting a server that covers at least the following items:

- Necessary services and ports
- Firewall rules
- Authentication and administrative access
- Software updates
- Logging events
- Backup and recovery
- Incident response plan

---

## 12. Summary

In this lesson, we became familiar with several common network attack types:

- **Port Scanning:** examining accessible ports and services
- **Brute Force:** attempting to guess a password or confidential value
- **DoS/DDoS:** disrupting service availability
- **Man-in-the-Middle:** attempting to observe or tamper with communication
- **Spoofing:** forging source specifications or identity
- **DNS Amplification:** abusing DNS responses to increase attack traffic
- **Lateral Movement:** expanding access from one system to other systems
- **Phishing:** deceiving the user to disclose information or perform an unwanted action

The most important point is that **identifying an indicator is different from proving an attack occurred**. Proper analysis requires evidence, understanding of the environment, and examination of multiple information sources.

The Python tools we have built can perform part of the examination and identification process; but valid security decisions must be made based on sufficient evidence and an understanding of the tools' limitations.
