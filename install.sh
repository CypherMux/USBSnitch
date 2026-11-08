#!/bin/bash

if [ "$EUID" -ne 0 ]; then
  echo "Please run as root (sudo ./install.sh)"
    exit 1
fi

echo "[*] Installing USBSnitch..."

# Install the dependencies
if command -v pacman &> /dev/null; then
  pacman -S --needed --noconfirm python-pyudev libnotify
elif command -v apt &> /dev/null; then
  apt update && apt install -y python3-pyudev libnotify-bin
else
  echo "[-] Warning: Unsupported package manager. Please install python-pyudev and libnotify manually."
fi

# Copy the Python script
cp usb-snitch.py /usr/local/bin/usb-snitch.py
chmod +x /usr/local/bin/usb-snitch.py

# Copy systemd service
cp usb-snitch.service /etc/systemd/system/usb-snitch.service

# Reload systemd
systemctl daemon-reload

echo "[+] Installation complete!"
echo "Enable the service to start on boot via:"
echo "  sudo systemctl enable --now usb-snitch"
