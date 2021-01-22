# BLE

  I used a Raspberry Pi for this project with Raspian OS. The Pi itself already has the ability to scan for BLE devices from the
command line but I used the PyBlueZ library to be able to make a program out of it. The program itself is currently set to 4
devices, but you can add as many as you want. All you need to know is the MAC address for the BLE device. The program also sends
and email alert when one of the devices is out of range. My particular use was for the Pi to be set up in a room, constantly 
scanning for BLE tags that were put on certain devices. When one of the devices was taken out of the room (out of range) the Pi 
would then send an email alert out saying which device was gone. So if you want to use that feature just create a junk email to use
as the sender and provide the password for it in the code where it is requested and then send to any email that you want to notify.
Overall this worked as a great custom asset tracking system using a Raspberry Pi. 

  The PyBlueZ library is a bit tricky to work with. It supposedly works on Windows and MacOS as well, with the right dependencies
 installed. I have yet to get it to work on either. Even for Linux it took a bit of debugging to get the right dependencies. You can
 find those that are needed under the PyBlueZ github I believe. Here is a link to that:
 
 https://github.com/pybluez/pybluez
 
  They provide a few examples of what their library is capable of. The code is fairly simple to understand. The hardest part is
 getting the correct and updated dependencies for the OS you are using. At the bottom of their page you will find this link:
 
 https://github.com/pybluez/pybluez/blob/master/docs/install.rst
 
  It provides installation instructions and which dependencies are needed for each.
  
  My personal demo video:
  
  https://youtu.be/M5RWFQiVFgA
