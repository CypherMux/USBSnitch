# usb-snitch
A real time notification visualizer for the USBGuard software.


## Why I Made This

I use USBGuard to block unauthorized hardware from connecting to my machine. However, checking the status manually by running `sudo usbguard list-devices` every time I happen to plug something in is extremely tedious.

`usb snitch` solves this by running silently in the background as a `systemd` daemon. It listens to kernel `udev` events, checks the hardware's authorization state, and instantly pops up a desktop notification. By doing that you know exactly what was plugged in and whether its data transfer capabilities were outright blocked or fully authorized without ever touching a terminal.

## Features

*  **Silent Systemd Daemon:** Runs quietly in the background and starts on boot.

*  **Instant Desktop Notifications:** Uses the desktop notifications feature natively on your system to notify you the second when a device connects.

*  **Data Transfer Status:** Explicitly tells you if the device is `BLOCKED` *(the data is successfully cut off by USBGuard)* or if the device is `AUTHORIZED` *(data is allowed via USBGuard)*.

*  **Device Fingerprinting:** Identifies the type of device *(Storage,Keyboard,etc)* so you know what kind of device the thing you just plugged in truly is. Extremely useful for USBs that are actually BadUSBs as they will show up as HIDs instead of the storage device they usually are.

## How It Works

`usb snitch` is a lightweight Bash script that uses `udevadm monitor` to listen for USB "add" events. When a device is inserted, it reads the device's `sysfs` attributes directly from the kernel:

**1.** It grabs the Vendor ID, product ID, and Manufacturer.

**2.** It reads the `authorized` flag *(which is set by USBGuard or the kernel)*. `0` will mean blocked, `1` means authorized.

**3.** It checks the `bInterfaceClass` to see if the device presents itself as mass storage.

**4.** It finally sends the data to `notify-send` so the alert appears as a notification on your desktop.

