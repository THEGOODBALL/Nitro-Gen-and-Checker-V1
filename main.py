from pystyle import *
import os
import random
import string
import time
import requests
from colorama import init
from pystyle import Colorate, Colors, Center, Col
import sys

# Initialize colorama for Windows support
init(autoreset=True)

# Define the banner
banner = """
┳┓•       ┏┓      ┓┏┏━
┃┃┓╋┏┓┏┓  ┃┓┏┓┏┓  ┃┃┗┓
┛┗┗┗┛ ┗┛  ┗┛┗ ┛┗  ┗┛┗┛
"""

# Apply color and centering
colored_banner = Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter(banner))

# Display the banner
print(colored_banner)

time.sleep(0.1)
print("Subscribe to THEGOODBALLYT\n")
time.sleep(0.1)

# Function to get the number of codes
def get_number_of_codes():
    try:
        num = int(input('Input How Many Codes to Generate and Check: '))
        if num <= 0:
            print("Please enter a positive number.")
            restart_script()
        else:
            return num
    except ValueError:
        print("Invalid input! Restarting the script...")
        restart_script()

# Function to restart the script
def restart_script():
    python = sys.executable
    os.execl(python, python, *sys.argv)

# Ask for the number of codes
num = get_number_of_codes()

# Generate codes
with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Your nitro codes are being generated, be patient if you entered a high number!")

    start = time.time()

    for _ in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k=16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

# Check codes
valid_codes = []

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip().split('/')[-1]  # Extract code part only
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Valid | {nitro} ")
            valid_codes.append(f"https://discord.gift/{nitro}")
        else:
            print(f" Invalid | https://discord.gift/{nitro} ")

# Save valid codes
with open("Valid Codes.txt", "w", encoding='utf-8') as file:
    for code in valid_codes:
        file.write(f"{code}\n")

print("https://www.youtube.com/@THEGOODBALLYT |  PLEASE SUB AND LIKE!  \n")

time.sleep(0.2)

input("\nYou have generated codes. Press Enter to close this. You'll find generated codes in 'Valid Codes.txt'. If the file is empty, generate more codes for a better chance. Bad luck :( ")
