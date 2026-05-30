# SSH Brute Force Attack

A simple Python script to perform an SSH password brute-force attack using a wordlist. This repository is intended for educational and authorized testing purposes only.

## ⚠️ Important
Only use this tool against systems you own or have explicit permission to test. Unauthorized access to systems is illegal and unethical.

## Features
- Attempts SSH login with a fixed target IP and username
- Reads candidate passwords from `wordlist.txt`
- Uses `paramiko` for SSH connections
- Stops once a valid password is found

## Requirements
- Python 3.8+
- `paramiko`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/theDreamer911/ssh-brute-force-attack.git
   cd ssh-brute-force-attack
   ```
2. Install dependencies:
   ```bash
   python3 -m pip install paramiko
   ```

## Usage
1. Update `attack.py` with the correct target IP and username:
   ```python
   target = "192.168.56.2"
   username = "admin"
   ```
2. Provide your password list in `wordlist.txt`, one password per line.
3. Run the script:
   ```bash
   python3 attack.py
   ```

## Example output
```text
[+] Trying: password123
[FAILED]
[+] Trying: admin
[SUCCESS] Password found: admin
```

## Notes
- The script waits 3 seconds between attempts to reduce load on the target.
- It only supports one username and one target IP at a time.
- Customize `attack.py` if you want to add support for multiple usernames or better error handling.

## Disclaimer
This project is for learning purposes only. The author is not responsible for misuse.

