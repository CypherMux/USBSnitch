# Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x  | :white_check_mark: |
| < 1.0  | :x:                |


## Reporting a Vulnerability

Because **USBSnitch** runs as a system level daemon (`root`) and interfaces directly with the kernel `udev` events, security vulnerabilities in this code are taken extremely seriously.

**Please do not report security vulnerabilities through public Github issues.**

If you believe you have found a security vulnerability in USBSnitch, please report it privately.

Please include the following details in your report:

*  The type of issue (e.g command injection, privilege escalation, symlink attacks, etc..).

*  Full path of source files related to the issue.

*  Step-by-step instructions to reproduce the issue.

*  PoC or exploit code (if applicable).

*  Impact of the issue, including how an attacker may be able to exploit it.

## What to Expect

*  **Acknowledgement:** I will acknowledge the receiving of your vulnerability report within 48 hours of submission.

*  **Investigation:** I will investigate the issue and keep you updated on the progress.

*  **Fixes & Disclosure:** If the vulnerability is confirmed, I will develop a patch and coordinate the public disclosure timeline with you.

## Security Design Choices

*  **No Shell Execution;** USBSnitch uses Python's `subprocess.run` with list arguments (rather than `shell=True`) to prevent command injection attacks when passing devices names to `notify-send`.

*  **Read-Only Hardware Access:** The script only reads from `/sys/bus/usb/devices/` to check authorization status. It does not write to kernel files or block devices directly *(that is USBGuard's job)*.

*  **Root Privileges:** The script requires `root` to read kernel hardware events. It is designed to run as a locked-down systemd service.

## Thank You!

Thank you for helping to keep USBSnitch and the open-source community safe!
