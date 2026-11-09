---
name: Bug report
about: Create a report to help us improve the project
title: '"[BUG]"'
labels: bug
assignees: CypherMux

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1.  Plug in device `...` (e.g Logitech Mouse, Sandisk USB Drive)

2.  See error in `journalctl -u usb-snitch.service -f`

3. Notification fails to appear / Notification shows incorrect data.

**Expected behavior**
A clear and concise description of what you expected to happen. (e.g "I expected a desktop notification saying the device is BLOCKED").

**Environment  (please complete the following information):**

-  OS:  [e.g Arch Linux, Ubuntu, Kali Linux, etc..]

-  Desktop Environment / Window Manager:  [e.g GNOME, KDE Plasma, Hyprland, i3, etc..]

-  Display Server:  [e.g Wayland, X11, etc..]

-  Python Version: [e.g  3.11]  (Run `python3 --version`)

-  Are you running the script manually or via systemd? [e.g  Manual with sudo, systemd daemon]

**Logs  (Crucial for debugging the problem)**

Please paste the output of the service logs here:

```journalctl -u usb-snitch.service -n 50 --no-pager```

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Additional context**
Add any other context about the problem here. Did you modify the `send_notification` function for your username/UID? If so which method are you using (e.g `sudo`, `-u`, `su -c`, `systemd-run`)?
