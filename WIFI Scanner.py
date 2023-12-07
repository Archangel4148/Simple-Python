
import subprocess, os
from os.path import exists
os.system("color A")
valid = False
response = input("Would you like to filter responses? ")
response.casefold()
while response not in "yes" and response not in "no":
    print("Invalid input...")
    response = input("Would you like to filter responses? ")
    response.casefold()

exclude = []

if response in "yes":
    response = input("Would you like to open from a file, or type your own list of exceptions? ")
    response.casefold()
    while response != "file" and response != "list":
        print("Invalid input...")
        response = input("Would you like to open from a file, or type your own list of exceptions? ")
        response.casefold()

if response == "file":
    while not valid:
        print("(Press Enter to Cancel)")
        response = input("What is the name of the file you would like to import? ")
        if response == "":

            response = input("Would you like to continue without filters, or exit the program? ")
            response.casefold()
            while response != "exit" and response != "continue":
                print("Invalid input, please enter either \"exit\" or \"continue\"...")
                response = input("Would you like to continue without filters, or exit the program? ")
                response.casefold()

            if response == "exit":
                print(""
                      "\nClosing Program...")
                quit()
            else:
                break
        elif exists(response):
            valid = True
            with open(response) as f:
                exclude = [str(i).replace("\n", "") for i in f.readlines()]
        else:
            print("This file does not exist...\n")

elif response == "list":
    while response != "":
        response = input("Enter an exclusion, or press Enter to proceed: ")
        if response != "":
            exclude.append(response)

# Collect Raw Network Names
command_output = subprocess.check_output("netsh wlan show profiles")
networks = []
# Parse Raw Info Into Individual Network IDs
for i, c in enumerate(str(command_output).split(r"\n")):
    if "All User Profile" in c:
        networks.append(c[c.index(": ") + 2:c.index("\\")])
passwords = []
# Collect Raw Security Key Info
for i, c in enumerate(networks):
    raw_pass_output = str(subprocess.check_output(f"netsh wlan show profile \"{c}\" key=clear"))
    passwords.append(raw_pass_output[raw_pass_output.index("Key") + 25:raw_pass_output.index("Cost") - 8])
    output = f"\n{str(c)} : {passwords[i]}"
    sensitive = False
# Check for Exclusions in Network IDs
    for exception in exclude:
        if exception.casefold() in c.casefold():
            sensitive = True
            break
    if not sensitive:
        print(output)
    else:
        sensitive = False

# Prevent Instant Close in Terminal
leave_check = input("\n\nPress Enter to close...")

