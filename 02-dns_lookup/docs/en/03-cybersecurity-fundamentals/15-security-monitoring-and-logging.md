[🇮🇷 فارسی](/02-dns_lookup/docs/fa/03-cybersecurity-fundamentals/15-security-monitoring-and-logging.md)

# Lesson 15: Security Monitoring and Logging

## Security Monitoring & Logging

## 1. Introduction

Suppose our Python tool sends a DNS request but does not receive a response. Or a request encounters an error. If the tool only displays the result, we might not have enough information to understand the cause of the problem.

Now imagine that a security tool logs hundreds of unexpected errors instead of one error. Without proper information, distinguishing whether the problem is from the network, settings, user input, or the program itself becomes difficult.

This is where two important concepts come in:

- **Logging:** recording information about the program's execution and its events.
- **Security Monitoring:** examining events to identify unusual behaviors or security threats.

The goal of this lesson is to learn the principles of logging events in Python and to understand their role in security tools.

---

## 2. The Difference Between Event, Log, and Alert

These three concepts are related, but not identical.

### Log

A Log is a record of an event that the program has logged.

For example:

```text
2026-10-09 10:30:00 INFO DNS lookup completed for example.com
```

This report shows that a DNS operation has completed successfully.

### Event

An Event is something that matters to the system and can be logged or examined.

Examples:

- Executing a DNS request
- Receiving a response from the server
- Failure to establish a connection
- Failed user login
- Change to security settings

Not every Event is necessarily dangerous. For example, a failed DNS request might be due to an ordinary network problem.

### Alert

An Alert is created when an event or combination of events requires attention.

For example:

- Logging a DNS error alone might just be a Log.
- Repeating many errors in a short time might be an Event worth examining.
- Exceeding a specific threshold of errors can create an Alert.

**Note:** Logging alone does not mean detecting or preventing an attack. Creating an alert usually requires detection rules, event analysis, or monitoring systems.

---

## 3. Why Does Logging Matter in Security?

Proper logging of events has several important uses.

### 3.1. Troubleshooting

When the program errors, a Log can help us understand:

- Which operation was in progress?
- When did the error occur?
- What type of error occurred?
- Is the problem reproducible?

### 3.2. Security Incident Investigation

If suspicious behavior is observed, the recorded reports might help examine the following:

- What happened?
- When did it happen?
- Which part of the system was involved?
- Are there other related events?

Of course, a Log only provides the information that was actually recorded. If the program did not log an important event, we might not be able to reconstruct it from the reports.

### 3.3. Detecting Unusual Behavior

Examining a collection of Logs might reveal patterns; for example:

- A large number of authentication errors
- A sudden increase in network errors
- Highly repeated requests
- Repeated attempts to access unauthorized resources
- Unexpected changes in settings

A single event is not always a sign of attack. Proper detection usually depends on context, the number of events, and the system's conditions.

---

## 4. What Information Should Be Logged?

A useful Log should have enough information to understand the event, without disclosing sensitive data.

Common information includes:

| Field | Use |
|---|---|
| Timestamp | The time the event occurred or was recorded |
| Log Level | The importance or severity of the message |
| Logger Name | The name of the reporting component |
| Event Message | Description of the event |
| Context | Information needed to understand the event |
| Correlation ID | An identifier for linking the reports of one operation |

For example:

```text
2026-10-09 10:30:00 WARNING dns_lookup Timeout during DNS query
```

In this example, the time, the report level, and the description of the event are specified.

### Accurate Timestamping

In systems with multiple machines or services, synchronized clocks matter greatly. Without it, the order of events might be misinterpreted.

In distributed systems, using a standard time such as UTC can make comparing reports easier.

### Recording Appropriate Context

For a DNS Lookup tool, depending on the need and the sensitivity of the information, the Context might include:

- The type of DNS operation
- The requested record type
- The duration of the request
- The overall result of the operation
- The type of error that occurred

The information should be enough to make troubleshooting easy, not to log every piece of data without reason.

---

## 5. Logging Levels in Python

The Python standard `logging` library has several main levels.

| Level | Use |
|---|---|
| `DEBUG` | Detailed information for development and troubleshooting |
| `INFO` | Informing about normal operations |
| `WARNING` | An unexpected condition that does not necessarily stop the program's execution |
| `ERROR` | An error that has prevented an operation from completing |
| `CRITICAL` | A very serious error that might threaten the entire program's operation |

For example, if a DNS request is successful, we might use `INFO`. If the operation fails due to a Timeout, depending on the program's expected behavior, `WARNING` or `ERROR` might be appropriate.

**The choice of report level should be based on the actual meaning of the event, not just the name of an Exception.**

An expected network error does not necessarily mean a total program failure.

---

## 6. Introduction to `logging` in Python

The `logging` library is available as standard in Python and usually does not need to be installed separately.

### 6.1. A Simple Example

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

logger = logging.getLogger(__name__)

logger.debug("Detailed diagnostic information")
logger.info("DNS lookup completed")
logger.warning("DNS query timed out")
logger.error("DNS lookup failed")
```

In this example:

- `basicConfig()` specifies the basic logging settings.
- `level=logging.INFO` displays messages at INFO level and more important levels.
- `format` determines the report format.
- `getLogger(__name__)` receives a Logger named after the current module.

Since the logging level is set to `INFO`, the `DEBUG` message is not displayed in normal output.

### 6.2. Why Do We Use `getLogger(__name__)`?

In a project with multiple modules, each module should preferably have its own Logger:

```python
import logging

logger = logging.getLogger(__name__)
```

This helps specify which module each message came from.

In multi-module projects, the main logging configuration is usually performed at the program's entry point, such as the CLI; reusable modules only log the necessary messages.

This separation prevents repeated logging configuration in different modules.

---

## 7. Logging Exceptions Properly

Suppose an operation's execution encounters an error. Logging the error type can be useful for troubleshooting.

```python
import logging

logger = logging.getLogger(__name__)

try:
    result = perform_operation()
except RuntimeError:
    logger.exception("Operation failed")
```

In this example, `logger.exception()` logs the message along with the Exception information and Traceback.

This method should usually be used inside an `except` block.

The Traceback can be very useful for finding the error location, but it might also reveal internal program information. Therefore, we must control the destination and access to the reports.

### Should We Catch All Errors?

No.

Catching overly general Exceptions and continuing the program's execution without proper error handling can hide problems.

It is better to:

1. Identify expected errors.
2. Handle them at the appropriate level.
3. Log useful information.
4. Handle unexpected errors in a way that does not hide their root cause.

---

## 8. What Information Should Not Be Logged?

One of the most important security principles of Logging is that reports should not become a place for sensitive information leakage.

### Information That Should Usually Not Be Logged

- Password
- API Key
- Access Token and Refresh Token
- Private Key
- Authentication information
- Sensitive content of requests or responses
- Unnecessary personal information

For example, this is dangerous:

```python
logger.info("User credentials: %s", credentials)
```

If `credentials` contains a password or Token, sensitive information enters the reports.

It is better to log only the result of the operation:

```python
logger.info("Authentication attempt completed")
```

Of course, this message alone might not be enough for troubleshooting; additional information must be selected based on the actual need, the privacy policy, and the access level.

### An Important Principle

**Not all information needed to run the application is necessarily needed to be logged.**

It is also better to examine or sanitize control characters and untrusted values before logging user input data. Otherwise, a tampered input might change the appearance of the reports or inject fake messages into them.

---

## 9. The Difference Between Logging and `print()`

In small programs, using `print()` to display the result is sufficient.

But Logging offers more capabilities:

- Different message levels
- Logging the Logger name
- Automatic timestamping
- Ability to send reports to a file or other destinations
- Ability to set the report level without changing all messages
- Easier integration with monitoring systems

For example, in a CLI tool, the result the user needs to see can be displayed through the program's normal output, but the technical details of the operation's execution can be logged with Logging.

These two uses are not the same:

- **Output:** information the user needs to use the tool.
- **Log:** information useful for troubleshooting, examination, and system monitoring.

We should not transfer all internal program messages to the user's output without reason.

---

## 10. From Log to Security Monitoring

Having a Log is useful, but Monitoring requires examining and analyzing these reports.

Consider a simple process:

1. The program logs important events.
2. The reports are stored in a specific destination.
3. Related events are examined.
4. Detection rules or thresholds are executed.
5. If necessary, an alert is created.
6. The responsible individual examines the event.

In large systems, reports might be sent to a central system to enable searching and analysis across multiple services.

### Storing and Protecting Reports

Logs must also be protected.

Pay attention to these items:

- Restrict access to the reports.
- Specify their retention period.
- Prevent disk filling.
- Consider Log file rotation or Log Rotation.
- If necessary, transfer the reports to a separate destination.
- Make unauthorized modification or deletion of reports detectable as much as possible.

Unlimited retention of reports is not always the right decision; it might create costs or retain sensitive information longer than necessary.

---

## 11. How Logging Relates to the DNS Lookup Project

In the Logging tool, DNS Lookup can make understanding the program's behavior easier.

For example, consider the following categories of events:

| Event | Useful information to log |
|---|---|
| Starting a request | The operation type and the requested record |
| Receiving a response | The overall result and the operation duration |
| Timeout | The operation type and the error type |
| Invalid domain | An explanation of the input error, without disclosing unnecessary information |
| Unexpected error | An appropriate message and Exception information at a secure destination |

Of course, not all of these should necessarily be logged at the same level. The choice of appropriate level depends on the program's actual behavior.

### A DNS Error Is Not Always a Security Event

Suppose a DNS request reaches a Timeout. This can be caused by:

- A network communication problem
- The Resolver not responding
- Restrictions of the execution environment
- Incorrect settings
- A temporary service disruption

Therefore, we should not treat every Timeout as a security attack.

In contrast, an unusual increase in the number of errors or requests might be worth examining.

**A Log alone does not determine the definitive cause of an event; it must be interpreted in the appropriate context.**

### Logging in Security Tools

In security tools, reports must answer two questions:

1. What happened in the tool?
2. What information is needed to understand the cause of that event?

But we should not log all data received from the network or all user inputs without reason.

---

## 12. A Few Common Mistakes

### First Mistake: Logging All Information

Logging all inputs and outputs might disclose sensitive information.

**Solution:** Log only the necessary information that is appropriate to the purpose of the report.

### Second Mistake: Not Logging Errors

If an operation fails and no information is logged, troubleshooting becomes difficult.

**Solution:** Handle and log important errors at the appropriate place.

### Third Mistake: Treating All Errors the Same

An expected Timeout is not the same as an unexpected programming error.

**Solution:** Consider the error type and its impact on the operation when choosing the report level.

### Fourth Mistake: Configuring Logging in All Modules

This can cause duplicate configurations or inappropriate behavior in multi-module programs.

**Solution:** Receive the Logger in each module and usually perform the main configuration at the program's entry point.

### Fifth Mistake: Fully Trusting Logs

Some events might not have been recorded, or the reports might be incomplete or even tampered with.

**Solution:** Consider Logs as one source of evidence, not as complete and definitive truth.

---

## 13. Practical Exercises

### Exercise 1: Appropriate Logging Level

For each item, determine which level is more appropriate and why:

1. A DNS operation has completed successfully.
2. A DNS request has reached a Timeout.
3. The program was unable to complete an important operation due to an unexpected error.
4. The developer needs more internal details for troubleshooting.

The answers might vary depending on the impact of the event and the program's expected behavior; the reason for the choice matters more than memorizing the names of the levels.

### Exercise 2: Identifying Sensitive Information

Review this message:

```python
logger.info(
    "Request failed: token=%s password=%s",
    token,
    password,
)
```

Answer the following questions:

- What is wrong with it?
- Why is removing the password alone not enough?
- What information could be logged instead?

### Exercise 3: Designing a Log for DNS Lookup

For a DNS operation, determine:

- When should a Log be recorded?
- What information should be in it?
- What information should not be logged?
- Which errors are expected?
- What event might be worth security examination?

### Exercise 4: Reviewing a Logger

Review the following code:

```python
import logging

logger = logging.getLogger(__name__)


def run_operation() -> None:
    try:
        perform_operation()
    except RuntimeError:
        logger.exception("Operation failed")
        raise
```

Answer the following questions:

- Why is `getLogger(__name__)` used?
- What information does `logger.exception()` log?
- Why do we re-raise the error after logging it with `raise`?
- In what conditions might re-logging the same Exception at a higher layer cause unnecessary report duplication?

---

## 14. Summary

In this lesson, we learned:

- Logging means recording the program's events.
- Monitoring means examining events to understand the system's state and identify unusual behaviors.
- An Alert is a warning that is usually created based on an event or a set of conditions.
- The Python standard `logging` library is the main tool for recording reports in Python.
- Choosing the logging level should match the actual importance of the event.
- Logging sensitive information can cause information leakage.
- Reports are useful for troubleshooting and security examination, but they alone do not prove the definitive cause of an event.
- In DNS Lookup tools, a distinction must be made between ordinary operational errors and truly suspicious behaviors.

### Next Step

In the sixteenth and final lesson of this chapter, we will examine the principles of secure development and the security assessment workflow; then we will enter the code analysis chapter of the DNS Lookup project to examine the concepts in the actual implementation.
