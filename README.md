                                                    USBSnitch





<img width="1028" height="1028" alt="concept3" src="https://github.com/user-attachments/assets/f612ed36-2098-4e22-ab59-6edbcf613ef6" />



                              A real time notification visualizer for the USBGuard software.


## Why I Made This

I use USBGuard to block unauthorized hardware from connecting to my machine. However, checking the status manually by running `sudo usbguard list-devices` every time I happen to plug something in is extremely tedious.

`USBSnitch` solves this by running silently in the background as a `systemd` daemon. It listens to kernel `udev` events, checks the hardware's authorization state, and instantly pops up a desktop notification. By doing that you know exactly what was plugged in and whether its data transfer capabilities were outright blocked or fully authorized without ever touching a terminal.

## Features

*  **Silent Systemd Daemon:** Runs quietly in the background and starts on boot.

*  **Instant Desktop Notifications:** Uses the desktop notifications feature natively on your system to notify you the second when a device connects.

*  **Data Transfer Status:** Explicitly tells you if the device is `BLOCKED` *(the data is successfully cut off by USBGuard)* or if the device is `AUTHORIZED` *(data is allowed via USBGuard)*.

*  **Device Fingerprinting:** Identifies the type of device *(Storage,Keyboard,etc)* so you know what kind of device the thing you just plugged in truly is. Extremely useful for USBs that are actually BadUSBs as they will show up as HIDs instead of the storage device they usually are.

## How It Works

`USBSnitch` is a lightweight Bash script that uses `udevadm monitor` to listen for USB "add" events. When a device is inserted, it reads the device's `sysfs` attributes directly from the kernel:

**1.** It grabs the Vendor ID, product ID, and Manufacturer.

**2.** It reads the `authorized` flag *(which is set by USBGuard or the kernel)*. `0` will mean blocked, `1` means authorized.

**3.** It checks the `bInterfaceClass` to see if the device presents itself as mass storage.

**4.** It finally sends the data to `notify-send` so the alert appears as a notification on your desktop.

## Dependencies

Because this tool is relies fully on Python and desktop notifications to operate, you will need to install the following packages in order for it to function correctly:

*  **Arch**: `sudo pacman -S python-pyudev libnotify`

*  **Debian/Ubuntu:** `sudo apt install python3-yudev libnotify-bin`

## Installation & Usage

**1. Clone the repository:**

```git clone https://github.com/CypherMux/USBSnitch.git && cd USBSnitch```

**2. Run the installer *(this will install all dependencies necessary, copy the script, and set up the systemd service)*:

```chmod +x install.sh && sudo ./install.sh```

**3. Enable and start the background service:**

```sudo systemctl enable --now usb-snitch.service```

**4. Plug in a USB device. A desktop notification will now appear whenever you plug in any device.

## How To Manage The Service

Because this tool runs as a system daemon, you can control it just like any other systemd service:

*  **Stop Monitoring:**

```sudo systemctl stop usb-snitch.service```

*  **Start Monitoring:**

```sudo systemctl start usb-snitch.service```

*  **Check the system logs:**

```journalctl -u usb-snitch.service -f```

## Disclaimer

*This tool is a visualizer for existing USB security policies you may have on your system *(such as USBGuard)*. It does not block devices itself as it only reports what the kernel and your security policies are already doing. Use responsibly on systems you own.*

