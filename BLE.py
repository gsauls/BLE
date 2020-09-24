# BLE SCAN PROGRAM

# for sending emails
import smtplib, ssl

# for scanning for BLE devices
from gattlib import DiscoveryService

# scan function
def scan( str, str1 ):
    print("Scanning for {}...\n".format(str1))
    service = DiscoveryService()
    devices = service.discover(8)

    for address, name in devices.items():
        if address == str:
            print("Beacon found - device: {}\n".format(str1))  
            return True

    return False

# email function
def email( str ):
    port = 465 #For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "#########"
    receiver_email = "#########"
    password = "#########"
    message = """\

    Subject: URGENT

    {} has been taken.""".format(str)

    #Creat a secure SSl context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


# setting each device to false at first, if it is found in scan, will be turned to true
AllDev = True
dev1 = False
dev2 = False
dev3 = False
dev4 = False


# setting a counter for each device
count1 = 0
count2 = 0
count3 = 0
count4 = 0


# setting each device to their address Ex: "0C:F3:EE:0D:79:5B"
beacon1 = "XX:XX:XX:XX:XX:XX"  
beacon2 = "XX:XX:XX:XX:XX:XX" 
beacon3 = "XX:XX:XX:XX:XX:XX"
beacon4 = "XX:XX:XX:XX:XX:XX"


# naming each device, Ex: device1 = "Oculus Rift"
device1 = ""
device2 = ""
device3 = ""
device4 = ""


# main file
while AllDev == True:

    # device 1 block

    dev1 = scan(beacon1, device1)
    if dev1 == True:
        print("Found\n")
        count1 = 0
    if dev1 == False:
        print("Not Found\n")
        count1 += 1
    if count1 == 3:
        print("Sending Alert\n")
        email(device1)


    # device 2 block

    dev2 = scan(beacon2, device2)
    if dev2 == True:
        print("Found\n")
        count2 = 0
    if dev2 == False:
        print("Not Found\n")
        count2 += 1
    if count2 == 3:
        print("Sending Alert\n")
        email(device2)


    # device 3 block

    dev3 = scan(beacon3, device3)
    if dev3 == True:
        print("Found\n")
        count3 = 0
    if dev3 == False:
       print("Not Found\n")
       count3 += 1
    if count3 == 3:
        print("Sending Alert\n")
        email(device3)


    # device 4 block

    dev4 = scan(beacon4, device4)
    if dev4 == True:
        print("Found\n")
        count4 = 0
    if dev4 == False:
        print("Not Found\n")
        count4 += 1
    if count4 == 3:
        print("Sending Alert\n")
        email(device4)