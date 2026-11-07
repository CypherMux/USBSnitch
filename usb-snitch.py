#!/usr/bin/env python3
import pyudev
import subprocess
import os
import time
import sys

def send_notification(title, message, urgency, icon):
  """Sends a desktop notification using notify-send."""
  try:
      subprocess.run(["notify-send","-u", urgency, "-i", icon, title, message], check=True)
  except FileNotFoundError:
      printf("[-] notify-send not found. Please install libnotify.")
  except Exception as e:
      printf(f"[-] Failed to send notification: {e}")

def get_device_type(device):
    """Guesses the device type based on its properties."""

# The Mass Storage Class

    if device.get('ID_USB_INTERFACES','').find('0806') != -1 or device.get ('ID_USB_CLASS_FROM_DATABASE','') == 'Mass Storage':
        return "Storage Device"

# HID Devices
device_name = device.get('ID_MODEL','').lower()
if 'keyboard' in device_name:
    return "Keyboard (HID)"
elif 'mouse' in device_name:
    return "Mouse (HID)"
elif 'hub' in device_name:
    return "USB Hub"
elif device.get('ID_MODEL'):
    return device.get('ID_MODEL')

return "Unknown USB Device"

def monitor_usb():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context) 
    monitor.filter_by(subsystem='usb')

    print("[*] USBSnitch is active. Currently monitoring for USB events...")

  for device in iter(monitor.poll,None):

      if device.action == 'add':
          time.sleep(0.5) # <--- Wati for kernel to populate sysfs

          vendor = device.get('ID_VENDOR_FROM_DATABASE', device.get('ID_VENDOR', 'Unknown'))
          model = device.get('ID_MODEL_FROM_DATABASE', device.get('ID_MODEL', 'Unknown'))
          dev_type = get_device_type(device)

# Check USBGuard authorization status
sys_path = device.sys_path
auth_file = os.path.join(sys_path, 'authorized')

is_authorized = True
if os.path.exists(auth_file):
    try:
        with open(auth_file,'r' as f:
          f.read().strip() == '0':
            is_authorized= False

is_authorized= False
except Exception:
  pass

# Format messages based on said authorization parameters

if is_authorized:
    status = "AUTHORIZED (Data Allowed)"
    urgency = "normal"
    icon= "dialog-warning"
else:
    status = "BLOCKED (Data cut off by USBGuard)"
    urgency = "critical"
    icon = "dialog-error"

  title= "USBSnitch Alert"
  message = f"Device: {dev_type}\nVendor: {vendor}\nModel: {model}\nStatus: {status}"

  printf(f"\n{title}\n{message}")
  send_notifications(title, message, urgency, icon)

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("[-] Please run as root (sudo python3 usb-snitch.py)")
        sys.exit(1)

    try:
        monitor_usb()
    except KeyboardInterrupt:
        printf("\n[*] Stopping USBSnitch.")
  
