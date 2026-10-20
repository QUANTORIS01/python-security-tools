[🇮🇷 فارسی](/02-dns_lookup/docs/fa/03-cybersecurity-fundamentals/16-secure-development-and-security-assessment-workflow.md)

# Lesson 16: Secure Development and Security Assessment Workflow

## Secure Development & Security Assessment Workflow

## 1. Introduction

So far, we have become familiar with the basic concepts of cybersecurity, networking, vulnerabilities, cryptography, managing confidential information, Logging, and security monitoring.

Now we must turn these concepts into a practical method for developing Python tools.

Suppose we want to build a tool like DNS Lookup or Port Scanner. Simply running the program and getting the correct output is not enough. We must examine:

- Does it properly handle invalid inputs?
- Does it behave predictably when errors occur?
- Does it disclose sensitive information?
- Are its dependencies secure and up to date?
- Do the tests verify the expected behavior?
- Can we explain its performance and limitations?

These questions are part of secure software development.

---

## 2. What Is Secure Development?

**Secure Development** means considering security as one of the software's requirements throughout all stages of development.

Security should not be examined only at the end of the project.

For example, if during the tool's design we decide to catch all Exceptions regardless of their type and display only a general message, problems might arise in troubleshooting or error management.

If from the beginning we design specific behavior for expected and unexpected errors, the result will usually be more predictable and easier to maintain.

### General Secure Development Stages

1. **Design:** specify the goal, requirements, and limitations
2. **Implementation:** write code following security principles
3. **Testing:** examine normal behavior, errors, and invalid inputs
4. **Dependency Review:** examine libraries and dependencies
5. **Security Assessment:** examine possible risks and weaknesses
6. **Remediation:** fix identified problems
7. **Retesting:** re-examine after remediation
8. **Maintenance:** continuous maintenance and updates

These stages are not always completely linear. During testing or maintenance, we might return to the design or implementation stage.

---

## 3. Input Validation

User input must be examined before use.

For example, the DNS Lookup tool might receive a domain name and record type from the user.

In this case, we must specify:

- Is the input empty?
- Is the requested record type supported?
- Is the input compatible with the constraints defined for the application?
- If the input is invalid, how does the application respond?

For example, if the tool only supports specific records, its behavior for an unknown record type must be clear.

An important point is that input validation is not the same as ensuring the validity of the result. Even a valid domain name might not exist or the DNS server might not be able to respond to it.

**Key principle:** Check the input, but do not assume that input validation guarantees the operation's success.

---

## 4. Error and Exception Management

A secure application must handle errors in a predictable way.

For example, a network tool might encounter these conditions:

- Invalid input
- Timeout
- Empty response
- Resolver error
- Network access problem
- Unexpected error in code

These conditions do not necessarily have the same meaning.

### Appropriate Error Management Principles

- Handle expected errors as specifically as possible.
- The error message for the user should be clear and appropriate.
- Necessary technical details for troubleshooting should be logged at the appropriate destination.
- Confidential information should not be in messages or Logs.
- Unexpected errors should not be silently ignored.
- The program's behavior when an operation fails should be clear.

For example, displaying the message "No response was received for this request" might be appropriate for the user; but in the internal report, if needed, the more precise error type can be logged.

Of course, the user message must be consistent with reality. A Timeout does not necessarily mean that the domain does not exist.

---

## 5. Managing Python Dependencies

Many Python projects depend on external libraries.

These libraries might have vulnerabilities or receive security fixes in new versions.

Therefore, examining dependencies is part of the project's secure maintenance.

### 5.1. Virtual Environment

To isolate the project's dependencies, a virtual environment can be used:

```bash
python -m venv .venv
```

Activation on Linux and macOS:

```bash
source .venv/bin/activate
```

Activation on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

A virtual environment helps with separate dependency management, but does not by itself resolve their vulnerabilities.

### 5.2. Viewing Dependencies

You can view installed packages with this command:

```bash
python -m pip list
```

To examine the compatibility of some dependencies, you can also use:

```bash
python -m pip check
```

This command examines declared incompatibilities among installed dependencies; but **it is not a security vulnerability identification tool**.

### 5.3. Examining Known Vulnerabilities

A tool such as `pip-audit` can examine Python dependencies for known vulnerabilities.

After installing it in the appropriate environment, it can be run:

```bash
python -m pip_audit
```

The presence of a warning does not mean that the vulnerability is necessarily exploitable in the project's conditions. Also, the absence of a warning does not guarantee that the project is completely secure.

When examining the results, items such as the vulnerable version, the fixed version, the extent of use of the vulnerable part, and the possibility of upgrading should be considered.

---

## 6. Software Testing from a Security Perspective

Testing is not just for ensuring correct operation in normal conditions; the program's behavior in unusual conditions must also be examined.

### 6.1. Testing the Success Path

We examine that the operation reaches the expected result with valid input.

### 6.2. Testing Invalid Input

We examine that invalid input does not cause uncontrolled behavior or an inappropriate message.

### 6.3. Testing Operational Errors

We examine that the program can handle conditions such as Timeout or dependency errors in the expected manner.

### 6.4. Testing Boundaries

Empty, very large, or out-of-range values can create different behaviors.

### 6.5. Testing for Information Non-Disclosure

We examine that error messages, Logs, and program output do not contain passwords, Tokens, or unnecessary sensitive information.

### 6.6. Reproducible Testing

A good test should be as reproducible as possible.

For example, if a test depends on the real network, it might produce a different result due to network conditions. To test the internal logic of the program, if appropriate, Mock can be used to control the behavior of an external dependency.

Of course, Mock does not completely replace integrated testing with the real service; each has a different purpose.

---

## 7. Security Scanning Is Not the Same as a Security Assessment

Security tools can gather important information, but their outputs must be interpreted.

For example:

- Port Scanner can examine the access status of specific ports.
- DNS Lookup can receive information related to DNS records.
- A dependency examination tool can report some known vulnerabilities.

None of these tools alone determines the complete security of a system.

### Why?

Because each tool has a specific scope.

Port Scanner alone does not prove that a service is vulnerable. An open port might be necessary for the system's normal operation.

DNS Lookup, too, cannot by itself draw conclusions about the complete security of a domain or server from observing a single record.

Similarly, the dependency examination tool might report problems that are not exploitable in the project's specific conditions; or might not detect weaknesses outside its examination scope.

**The tool's output is the starting point of the examination; not the final verdict on the system's security.**

---

## 8. A Simple Security Assessment Workflow

To examine a tool or system, the following workflow can be used.

### Stage One: Define the Scope

Specify what you are examining and what authorization you have to perform the examination.

For example, in a local project, the scope might be the application itself and its dependencies.

In a network assessment, the authorized scope and operational limitations must be clear.

### Stage Two: Identify Assets

Specify what needs protection:

- Source code
- Confidential information
- Dependencies
- Configuration files
- Network communications
- User data

### Stage Three: Identify Risks

Ask what might go wrong.

For example:

- Invalid input might cause an uncontrolled failure.
- An error might disclose internal information.
- A dependency might have a vulnerability.
- Confidential information might enter Git or Logs.
- The program might send excessive requests without appropriate restriction.

### Stage Four: Perform Examinations

Based on the project's scope, use appropriate methods:

- Automated tests
- Code review
- Dependency examination
- Settings examination
- Log examination
- Controlled testing of the program's behavior

### Stage Five: Prioritize Findings

Examine each problem based on severity, probability of occurrence, possible impact, and exploitation conditions.

Not all problems have the same importance. For example, disclosing a valid Token might be more important than an inappropriate error message.

### Stage Six: Remediate and Retest

After fixing the problem, examine again that:

- The main problem has been removed.
- The fix has not created a new error.
- The related test still passes.
- The program's expected behavior has been preserved.

### Stage Seven: Documentation

Record the result:

- What was examined?
- What problem was found?
- What evidence existed?
- What action was taken?
- What limitations remain?

Accurate documentation makes the assessment traceable and repeatable.

---

## 9. A Secure Development Checklist for Python Tools

Before completing a tool, examine these items:

### Inputs and Outputs

- [ ] Inputs are validated.
- [ ] Invalid input has predictable behavior.
- [ ] Error messages are clear and do not disclose sensitive information.

### Error Management

- [ ] Expected errors are handled.
- [ ] Unexpected errors are not silently ignored.
- [ ] The program's behavior when an operation fails is clear.

### Confidential Information

- [ ] Passwords, Tokens, and private keys are not in the code.
- [ ] Confidential information does not accidentally enter Logs.
- [ ] Sensitive files have not accidentally entered the Git repository.

### Dependencies

- [ ] The project's dependencies are identified.
- [ ] Appropriate examinations have been performed on them.
- [ ] There is a plan for updating dependencies.

### Testing

- [ ] The success path has been tested.
- [ ] Invalid input has been tested.
- [ ] Important errors have been tested.
- [ ] Tests are as reproducible as possible.

### Documentation

- [ ] The tool's purpose and limitations are specified.
- [ ] The execution method is explained.
- [ ] Security and operational limitations are stated.

This checklist does not guarantee that the software is completely secure; but it helps identify many common problems.

---

## 10. How This Lesson Relates to Our Projects

Our goal is not just learning security terminology. We are going to use these concepts to better understand Python tools.

In the Port Scanner project, the security examination can focus on:

- Managing Timeout and network errors
- Scan limitations
- Correct interpretation of port state
- Restricting the examination scope to authorized targets
- Testing the tool's behavior in different conditions

In the DNS Lookup project, the related topics are:

- Input validation
- Sending DNS requests and processing responses
- Handling Resolver errors
- The difference between an empty response and an operational error
- Appropriate logging of events
- Testing the program logic and dependency on DNS

In future projects, depending on the type of tool, other topics such as HTTP security, web data validation, Log analysis, or session management will become more important.

**We do not need to fully learn all security topics before starting each project. It is better to examine the concepts related to each tool more deeply while building and analyzing that tool.**

---

## 11. Final Exercise

For a Python tool of your choice, perform an initial assessment.

Answer the following questions:

1. What is the tool's purpose and where is its authorized use scope?
2. What inputs does it receive?
3. What errors might occur?
4. What information should not be recorded in the output or Log?
5. What dependencies does it have and how can they be examined?
6. Which tests are needed to examine unusual behavior?
7. What are the three most important possible risks?
8. If a problem is found, how do you verify its remediation?

The answers do not need to be complicated. The goal is to consider security as part of the software engineering process when building tools.

---

## 12. Chapter Summary

In this chapter, we became familiar with important principles:

- Understanding threats, vulnerabilities, and risks
- Understanding the attack surface and identification principles
- Understanding security controls and defense in depth
- Familiarity with authentication and authorization
- Understanding the basic concepts of cryptography and managing confidential information
- Understanding the principles of network security
- Familiarity with common network attacks
- Understanding vulnerability management
- Understanding Logging and security monitoring
- Familiarity with secure development, testing, and security assessment

Now the goal is not to continue all these topics separately and theoretically. In the following stages, we will examine each concept more deeply when we actually need it to understand a tool or make a technical decision.

# End of Chapter Three: Cybersecurity Fundamentals

## Next Chapter: DNS Lookup Project Code Analysis

In the next chapter, instead of building a new tool or continuing theorizing, we will go to our own DNS Lookup project.

We will proceed with the analysis step by step:

1. Examining the actual project structure and the responsibilities of the existing files
2. Following the program's execution path from the CLI to receiving the result
3. Examining how the DNS library is used
4. Analyzing response processing and record types
5. Examining Exception management and the program's behavior on errors
6. Examining Logging and where it is used
7. Analyzing tests, Mocks, and coverage of important behaviors
8. Examining the architecture, limitations, and opportunities for improvement

In this chapter, the basis of the analysis will be **the actual project code**; not files or modules that might only exist in a suggested design.
