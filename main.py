
from functions import arp, check_conn
from macchanger import change_mac_windows, change_mac_linux, check_mac_linux, check_mac_windows


givenip = input("IP RANGE. | Leave empty for auto-detection >>> ")

devices = arp(givenip)

print("\nN° \t IP \t\t MAC \t\t\t VENDOR\n")
for key in devices:
    print(f"{key} \t {devices.get(key)[0]} \t {devices.get(key)[1]} \t {devices.get(key)[2]}")

choice = int(input("\nChoose a device to spoof. >>> "))
mac = devices.get(choice)[1]
os = input(f"\nSpoofing {mac}\nWhat Operating system are you using?\n 1 Windows\n 2 Linux \n>>> ")
if os == "2":
    interface = input("Please specify your network interface >>> ")
    try:
        change_mac_linux(mac, interface)
    except:
        print("Failed.")
if os == "1":
    try:
        change_mac_windows(mac)
    except:
        print("Failed.")

choice = input("Would you like to verify if the changes were applied successfully? y/n >>> ")
if choice.lower() == "y":
    if os == "2":
        try:
            print(f"Your current MAC is {check_mac_linux(interface)}. You selected {mac} earlier.")
        except:
            print("Failed to check MAC")
    
    if os == "1":
        try:
            check_mac_windows()
        except:
            print("Failed to check MAC")
print("\nPLEASE NOTE IT CAN TAKE UP TO A MINUTE FOR YOUR DEVICE TO RECONNECT AFTER CHANGING ITS MAC ADDRESS!\n")
choice = input("Would you like to test the Internet connection? y/n >>> ")

if choice.lower() == "y":
    attempts = int(input("How many attempts should be made? >>> "))
    check_conn(attempts)