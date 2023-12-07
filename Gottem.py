from os import system
import subprocess
import keyboard
import time

system("start chrome")
keyboard.press_and_release("ctrl + l")
keyboard.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
keyboard.press_and_release("enter")
time.sleep(2)
keyboard.press_and_release("f")

command_output = subprocess.check_output("netsh wlan show interfaces")
networks = []
ssid, password = "", ""

for i, c in enumerate(str(command_output).split(r"\n")):
    if "SSID" in c and "BSSID" not in c:
        ssid = str(c[c.index(":") + 2:]).replace(r"\r", "")

response = input(f"Oh, so you're connected to {ssid}? (y/n): ")

print(f"It doesn't really matter what you just typed, I know you're connected to {ssid}.")

command_output = subprocess.check_output(f"netsh wlan show profile {ssid} key=clear")

for i, c in enumerate(str(command_output).split(r"\n")):
    if "Key" in c:
        password = c[c.index(":")+2:].replace(r"\r", "")

if "feea" not in password:
    system("netsh wlan disconnect")
print(f"\nAlso, your wifi password is {password}, since now you need to reconnect. Ya dun got hacked...")

leave = input("\n\nPress Enter to close...")
