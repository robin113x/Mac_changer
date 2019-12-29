#!/usr/bin/env python
print(" ")
print(" ")
print("MMMMM          MMMMM           AAAA         CCCCCCCCCC           ")
print("MMM  MM      MM  MMM         AAA  AAA       CCC                  ")
print("MMM    MM  MM    MMM        AAA    AAA      CCC                  ")
print("MMM      MM      MMM       AAA@@@@@@AAA     CCC      H A N G E R.")
print("MMM              MMM      AAA        AAA    CCC                  ")
print("MMM              MMM     AAA          AAA   CCC                  ")
print("MMM              MMM    AAA            AAA  CCCCCCCCCC           ")


print("                                                         -Robin  ")
print(" ")


import subprocess
import optparse

def get_argument():
    parse = optparse.OptionParser()  # taking input from user
    parse.add_option("-i", "--interface", dest="interface", help="Interface 'wlan0/eth0' to change it's mac address")
    parse.add_option("-m", "--mac", dest="new_mac", help="New  mac address")
    (option, argument) = parse.parse_args()
    if not option.interface:
        parse.error("[-]Please entre the specific interface or --help for more info")
    if not option.new_mac:
        parse.error("[-]please entre the new MAC or --help for more info")
    return option

def change_mac(interface,new_mac):

  print("################# R O B I N ####################")
  print("change MAC ADDRESS of " + interface + " to " + new_mac)
  print("################# R O B I N ####################")
  subprocess.call(["ifconfig", interface, "down"])
  subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
  subprocess.call(["ifconfig", interface, "up"])
  subprocess.call(["ifconfig", interface])


option = get_argument()
change_mac(option.interface, option.new_mac)   #calling function







