# 🖱️ Anti-Lock Script – Multi-platform Mouse Jiggler

[![Build Multi-Platform](https://github.com/yourusername/anti-lock/actions/workflows/build-multiplatform.yml/badge.svg)](https://github.com/yourusername/anti-lock/actions/workflows/build-multiplatform.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

This Python utility prevents your screen from locking by simulating a small mouse movement every 60 seconds.  
It's available for **Windows**, **macOS (Apple Silicon)**, and **Linux (.deb / .rpm)** via GitHub Releases.

---

## 💖 Sponsor this project

If you find this project useful, consider supporting it 🙏

[![Buy Me A Coffee](https://img.shields.io/badge/-Buy%20me%20a%20coffee-ffdd00?logo=buymeacoffee&logoColor=black&style=flat)](https://www.buymeacoffee.com/amarnaud2)
[![Ko-fi](https://img.shields.io/badge/-Support%20me%20on%20Ko--fi-29abe0?logo=ko-fi&logoColor=white&style=flat)](https://ko-fi.com/amarnaud2)
[![PayPal](https://img.shields.io/badge/-Donate%20via%20PayPal-00457C?logo=paypal&logoColor=white&style=flat)](https://paypal.me/arnaud2m)

## 📦 Supported Platforms

| Platform | Format         | Built with           |
|----------|----------------|----------------------|
| Windows  | `.exe`         | PyInstaller          |
| macOS    | `.app` / `.dmg`| py2app               |
| Linux    | `.deb` / `.rpm`| PyInstaller + FPM    |

## 🚀 How It Works

Every 60 seconds, the script moves the mouse by 1 pixel and back, preventing screen lock due to inactivity.

## 🔧 How to Use

Download the appropriate binary from the [Releases](https://github.com/yourusername/anti-lock/releases) section, then run it:

- **Windows**: Double-click `anti_lock.exe`
- **macOS**: Unzip and launch the `.app`. May require `System Preferences > Security > Allow Anyway`.
- **Linux**: Install with `sudo dpkg -i` or `sudo rpm -i`

## 💻 Manual Usage (Python Script)

You can also run the Python script directly:

```bash
pip install pyautogui
python anti_lock.py

To stop the script, press Ctrl+C.
``` 

## 🛠️ Build Locally

### Windows (via GitHub Actions or manually)

```bash
pip install pyinstaller
pyinstaller --onefile --windowed anti_lock.py
```

### macOS (Apple Silicon)

```bash
pip install py2app
python setup.py py2app
```

### Linux (Debian/Redhat)

```bash
sudo apt install ruby ruby-dev build-essential rpm
sudo gem install fpm
pip install pyinstaller
pyinstaller --onefile anti_lock.py
fpm -s dir -t deb -n anti_lock -v 1.0.0 -C pkg
fpm -s dir -t rpm -n anti_lock -v 1.0.0 -C pkg
```

### 🤖 CI/CD with GitHub Actions

This repository includes a GitHub Actions workflow that:

- Builds the script for all major platforms.
- Publishes artifacts to GitHub Releases when a tag like v1.0.0 is pushed.

## 🧪 Local Development Setup (macOS M1 compatible)

### 1. Clone this repository

```bash
git clone https://github.com/yourusername/anti-lock.git
cd anti-lock
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the script

```bash
python anti_lock.py
```

### 6. Deactivate the virtual environment

```bash
deactivate
```

---

## ☕ Support

If you’d like to say thanks or help keep this project going:

- 💛 [Buy Me a Coffee](https://www.buymeacoffee.com/amarnaud2)
- 💙 [Ko-fi](https://ko-fi.com/amarnaud2)
- 💳 [PayPal](https://paypal.me/arnaud2m)

Every contribution helps — thank you!

## 📜 License

MIT License – free to use, modify and distribute.


