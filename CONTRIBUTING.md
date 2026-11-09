# Contributing to USBSnitch

First off, thank you for considering contributing to `USBSnitch`! It is people like you that make the open-source community such an amazing place to learn, create, and inspire.

## How to Report a Bug

If you find a bug ,*(like a notification failing to send, or a certain device type being misidentified for example)*, please open an issue on GitHub.

Before opening an issue, please check if it has already been reported. When you create an issue, please include the following:

*  **Your Linux Distribution** *(e.g Arch Linux, Ubuntu, Debian, etc..)*

*  **Your desktop environment** *(e.g GNOME, KDE, Hyprland, etc..)*

*  **The exact error message you had received from `journalctl -u usb-snitch.service -f`.**

*  **What device you had plugged in when the error occured.**

## How to Suggest an Enhancement

If you have an idea for a new feature *(like adding support for additional USB devices for example)*, open an issue with the tag `[Feature Request]`. Describe exactly what you want the tool to do and why it would be an useful addition to USBSnitch.

## How to Submit a Pull Request

* **1.** **Fork** the repository and create a branch from `main`.

* **2.** If you have added code that should be tested before implementing, add tests to the fork *(if applicable)*.

* **3.** Ensure your script passes the Python syntax check by using the command: `python3 -m py_compile usb-snitch.py`.

* **4.** Update the `README.md` with details of said changes to the interface *(e.g if you were to add a new configuration variable to the script you can notify it here)*.

* **5.** Issue your pull request!

* ## Coding Style

* To keep the overall codebase clean and readable, please follow these guidelines:

* *  **Python 3 Only:** This tool relies on Python 3 and the `pyudev` library.
 
  *  **Indentation:** Please use **4 spaces** for indentation. Do not use tab characters *(Python will throw a `TabError` at you)*.
 
  *  **The `send_notification` Function:** This function is **HIGHLY** sensitive to Linux permissions. If you modify it whatsoever ensure you are not breaking the `sudo -u` or `su` privilege dropping logic required to talk to the user's D-Bus session.
 
  *  **Documentation:** If you add a new feature, add a comment explaining *why* it is there.
 
  ## License

  *By contributing to this project, you agree that your contributions will be licensed under its MIT license.*
