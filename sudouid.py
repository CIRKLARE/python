import os

if not 'SUDO_UID' in os.environ.keys():
    print("Try running this program with sudo.")
    exit()

print("you used SUDO to run this code")