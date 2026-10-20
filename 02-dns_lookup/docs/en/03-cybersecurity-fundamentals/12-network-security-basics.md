[🇮🇷 فارسی](/02-dns_lookup/docs/fa/03-cybersecurity-fundamentals/12-network-security-basics.md)

# Lesson 12: Network Security Basics

## 1. Introduction

**Network Security** is a set of policies, settings, tools, and methods used to protect the network, connected devices, and data in transit.

The goal of network security is to:

- Limit unauthorized access.
- Prevent unnecessary services from being accessible.
- Detect suspicious communications.
- Detect attacks and unusual behaviors.
- Limit the impact of an incident if it occurs.

For example, suppose you have a web server and a database. The web server must be accessible from the Internet, but the database usually does not need to be directly accessible from the Internet.

Network security helps ensure that this difference in access level is properly enforced.

---

## 2. Basic Principles of Network Security

### 2.1. Least Privilege

Each user, device, or service should have access only to the resources needed to perform its task.

For example:

- Internet users can connect to the HTTPS port of the web server.
- Only the application server is allowed to connect to the database port.
- Administrative access to the server must be restricted to specific individuals and systems.

### 2.2. Attack Surface Reduction

Every active service and every unnecessary communication path can increase the attack surface.

To reduce the attack surface:

- Disable unnecessary services.
- Block unnecessary ports.
- Keep software up to date.
- Restrict administrative access.
- Periodically review network settings.

**Note:** An open port by itself does not mean a vulnerability exists. Its importance depends on the service behind the port, its settings, the software version, and the level of access.

### 2.3. Not Assuming Default Trust

We should not give full trust to a device simply because it is inside the organization's network.

In modern security designs, access is evaluated based on identity, permission, device state, and specific policies. This approach relates to the concept of **Zero Trust**.

---

## 3. What Is a Firewall?

A **Firewall** is a hardware or software tool that examines network traffic based on a set of rules and determines whether to allow or deny its passage.

Depending on its type and capabilities, a firewall can examine items such as:

- Source and destination IP address
- Source and destination port
- Protocol, such as TCP or UDP
- Connection state
- In more advanced firewalls, application or application-layer information

### 3.1. How Does a Firewall Work?

Suppose a server has three services:

| Port | Service | Sample Policy |
|---|---|---|
| 22/TCP | SSH | Only from authorized administrative IPs |
| 80/TCP | HTTP | Accessible if public access is needed |
| 443/TCP | HTTPS | Publicly accessible |
| 3306/TCP | MySQL | Only from the application server |

In this example, Internet users can connect to the web service, but should not have direct access to the database.

These rules are samples; the actual policy must be compatible with the architecture and needs of the specific environment.

### 3.2. Types of Firewalls by Location

**Host-based Firewall**

Runs on a specific system and controls incoming or outgoing traffic of that system.

Example: the operating system firewall of a Linux server.

**Network-based Firewall**

Placed in the communication path between networks or different network segments and controls passing traffic.

Example: a firewall that separates the internal network from the Internet.

These two types can be used simultaneously; the presence of one does not necessarily eliminate the need for the other.

### 3.3. Stateless and Stateful Firewalls

**Stateless Firewall**

Examines each network packet based on defined rules, without necessarily maintaining the state of previous communications.

**Stateful Firewall**

Also tracks the state of connections and can determine whether a packet belongs to a previously established connection.

This capability is useful in deciding about traffic related to a connection.

### 3.4. The Default Deny Principle

In the **Default Deny** policy, traffic is denied by default, unless a specific rule allows its passage.

This approach is usually more restrictive and secure than a policy that allows everything and only blocks a few items.

Of course, rules must be designed carefully so that necessary services are not unintentionally made unavailable.

### 3.5. Firewall Limitations

A firewall alone does not provide complete security. For example:

- Authorized traffic might pass through a vulnerable application.
- An authorized user might disclose sensitive information.
- Misconfigurations might create unwanted access.
- An attack might be carried out through a communication that is allowed by the network policy.

That is why the firewall must be used alongside other controls.

---

## 4. What Is an IDS? (Intrusion Detection System)

**IDS** stands for *Intrusion Detection System*.

This system examines traffic or system activities to identify signs of attack, suspicious behavior, or violations of security policies.

An IDS might generate alerts based on:

- Known attack patterns
- Unusual traffic
- Repeated connection attempts
- Behaviors that are inconsistent with the security policy

### 4.1. Types of IDS

**NIDS — Network-based IDS**

Examines network traffic at specific points.

For example, it can be used to detect suspicious patterns in the traffic of a network segment.

**HIDS — Host-based IDS**

Examines the activities of a specific host; for example, system events, file changes, or unusual behaviors on a server.

### 4.2. What Is the IDS Output?

An IDS usually produces an alert or event so that the security officer can review it.

For example:

> A large number of failed connection attempts from one source in a short time has been observed.

This alert does not necessarily prove that the attack was successful. The observed behavior might have other causes as well.

Therefore, alerts must be reviewed and compared with other information.

---

## 5. What Is an IPS? (Intrusion Prevention System)

**IPS** stands for *Intrusion Prevention System*.

In addition to examining traffic, an IPS can take preventive action based on its rules and capabilities.

For example, it might:

- Reject suspicious packets.
- Block a connection.
- Stop traffic that conflicts with a specific security rule.

### 5.1. The Difference Between IDS and IPS

| Feature | IDS | IPS |
|---|---|---|
| Main goal | Detecting suspicious activity | Detecting and preventing specific identified activity |
| Common output | Alert or event | Alert and preventive action |
| Common deployment | Receiving a copy of traffic or examining host activity | Often in the traffic path |
| Automatic blocking capability | Usually not its main goal | One of its main capabilities |
| Risk of misconfiguration | False or excessive alerts | In addition to false alerts, the possibility of blocking authorized traffic |

This difference is a common pattern, not an absolute rule for all products. Some tools combine detection and prevention capabilities.

### 5.2. False Positive and False Negative

**False Positive**

The system detects an activity as suspicious, while that activity is actually harmless.

**False Negative**

A malicious activity occurs, but the system does not detect it.

Both cases matter. Excessive false positives can cause security team fatigue or blocking of healthy communications; false negatives can also lead to malicious activity passing through.

---

## 6. The Difference Between IDS, Firewall, and IPS

These three concepts do not answer the same question:

- **Firewall:** What traffic is allowed to pass based on the network policy?
- **IDS:** Is there a sign of suspicious activity?
- **IPS:** Should the detected traffic be stopped according to the prevention policy?

### A Practical Example

Suppose a web server is publicly available.

1. The firewall allows HTTPS traffic to reach the server.
2. The IDS examines the traffic and, upon observing a suspicious pattern, issues an alert.
3. The IPS, if properly configured and with a valid detection, might block specific traffic.
4. The event-logging system keeps the necessary information for later review.

These tools complement each other. None alone detects or stops all attacks.

---

## 7. Network Segmentation

**Network Segmentation** means dividing the network into segments whose communication is controlled.

For example, an organization might divide its network into:

- User network
- Server network
- Database network
- Management network
- Guest network

The goal is not to completely separate all segments from each other; the goal is to allow only the necessary communications.

### 7.1. Why Is Segmentation Important?

If a device in the user network is infected, appropriate segmentation can make it harder for the attacker to move toward servers or databases.

This relates to the topic of **limiting Lateral Movement**.

### 7.2. What Is a DMZ?

**DMZ** is a part of the network used to place some services exposed to the Internet; such as a public web server.

In a sample design:

- Internet users have access to the web server in the DMZ.
- The web server has access only to specific and necessary services in the internal network.
- Direct Internet access to the database is blocked.

The DMZ is not a substitute for all security controls; its communication rules must be properly defined and reviewed.

---

## 8. Communication Encryption and VPN

### 8.1. TLS

**TLS** is a protocol for protecting communications that can provide confidentiality and integrity of transmitted data and verify the identity of the other party through certificates.

For example, HTTPS uses TLS to protect the communication between the browser and the web server.

However, communication encryption alone does not guarantee that the target application is secure or that the data the user sends is harmless.

### 8.2. VPN

**VPN** creates a protected network connection; for example, an employee might connect to the organization's network from a remote location via VPN.

A VPN can protect communication along the transit path, but:

- It is not a substitute for strong authentication.
- It should not create unlimited access to the entire network.
- It requires secure settings, updates, and access control.

After the VPN is established, the user should also be given only the necessary accesses.

---

## 9. Common Network Security Risks

Some common problems include:

### 9.1. Unnecessary Ports and Services

A service accessible from the Internet might be the target of scanning, abuse, or login attempts.

Defensive measures:

- Disable unnecessary services.
- Restrict access to administrative services.
- Periodically review active services.

### 9.2. Firewall Misconfiguration

An overly permissive rule might create unnecessary access.

Measures:

- Document the rules.
- Remove unused rules.
- Design accesses with the Default Deny principle.
- Test and review changes.

### 9.3. Outdated or Vulnerable Services

Even if network access is restricted, outdated software can still pose a risk.

Measures:

- Check software versions.
- Install security patches.
- Separate sensitive services from unnecessary networks.

### 9.4. Spoofing and Address Impersonation Attacks

In some attacks, the attacker tries to forge information such as the IP address or the identity of a source.

We should not trust a communication based only on the source address. In security design, appropriate authentication, network controls, and valid verification methods must be used.

### 9.5. Inadequate Monitoring

If events are not logged or reviewed, detecting an incident and understanding what happened becomes harder.

Measures:

- Log important events.
- Keep system clocks synchronized.
- Define meaningful alerts.
- Have a clear policy for storing and reviewing reports.

---

## 10. How These Concepts Relate to Your Python Projects

In the `python-security-tools` repository, the two previous tools can be part of network security examination.

### 10.1. Port Scanner

The Port Scanner tool helps examine the access status of target ports.

For example, it can answer the question:

> Is a specific port on the examined host accessible from the scan execution location?

But this tool alone cannot prove that:

- The service behind the port is vulnerable.
- There is no firewall.
- The target system has been infected.
- An attack has been successful.

The scan result depends on the scan execution location, firewall rules, network path, and the host's state.

### 10.2. DNS Lookup

The DNS Lookup tool examines information that can be received through DNS queries; such as A, AAAA, MX, NS, or TXT records.

This information can be useful for understanding the infrastructure and reviewing configuration, but DNS Lookup is not a network intrusion detection tool and does not by itself determine the security state of the firewall or the vulnerability of services.

### 10.3. Combining Results

In an authorized assessment, the following process can be considered:

1. Identify the DNS records related to the domain under examination.
2. Identify the assets and the authorized assessment scope.
3. Examine the access status of the necessary ports.
4. Compare the results with the expected services.
5. Have the firewall rules and network settings examined by the authorized officer.
6. If IDS/IPS systems exist, examine the related alerts.
7. Document the findings and prioritize them for correction.

**Important:** Observing an open port does not prove the existence of a vulnerability or a successful attack. The result must be examined with other evidence.

---

## 11. Practical Exercises

Perform all the following exercises only on your personal system, a laboratory environment, or a target you are authorized to examine.

### Exercise 1: Observing Network Connections on Your System

On Windows:

```powershell
netstat -ano
```

On Linux:

```bash
ss -tuln
```

Check:

- What connections or ports are displayed?
- Which addresses are local?
- Can you identify the relationship between a port and its corresponding service?

Remember that these commands do not produce identical output and do not by themselves provide a complete view of the system's security state.

### Exercise 2: Examining Local Services

Run a known service in the laboratory environment and check whether it is accessible from your system.

Then stop it and compare the result.

The goal of this exercise is to understand the difference between a service being active and it being accessible from a specific source.

### Exercise 3: Reviewing the Firewall Policy

On your personal system, view the firewall rules using the operating system's management tool.

Answer these questions:

1. What traffic is allowed?
2. Is administrative access restricted?
3. Is there any unnecessary or overly permissive rule?
4. Before changing any rule, how do you ensure that a necessary service will not be disrupted?

Do not delete or change rules without understanding their purpose.

### Exercise 4: Designing a Simple Network

For a hypothetical application, consider the following components:

- Public web server
- Application server
- Database
- Management system

Design a table that specifies which component should be allowed to connect to which.

Then explain why each communication is necessary and which communications should be blocked.

### Exercise 5: Comparing IDS and IPS

For each scenario, determine which capability is needed:

1. Logging an alert when suspicious traffic is observed
2. Automatically blocking traffic that matches a valid prevention rule
3. Reviewing reports after an incident
4. Preventing direct Internet access to the database

Note that the fourth item is usually solved with firewall policy and network segmentation design; IDS alone is not a substitute for this control.

---

## 12. Summary

In this lesson, we learned:

- Network security is used for controlling access and protecting communications and services.
- A firewall controls traffic based on specific rules.
- IDS detects suspicious activity and usually produces alerts.
- IPS can also block specific traffic.
- Network segmentation and DMZ help limit communications and reduce the scope of incident impact.
- TLS protects communications and VPN enables a protected network connection.
- Port Scanner examines the access status of ports, not that it alone proves a vulnerability or a successful attack.
- DNS Lookup examines DNS information and is not a substitute for monitoring or intrusion detection tools.

The important principle is that **network security comes from a combination of access control, proper configuration, monitoring, updates, and continuous review.**
