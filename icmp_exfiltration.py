#!/usr/bin/env python3
from scapy.all import *
from colorama import Fore
import signal
import subprocess
import sys
import time


def ctrl_c(signum, frame):
    print(f"\n{Fore.BLUE + '┃'}  {Fore.GREEN + '['}{Fore.BLUE + '*'}{Fore.GREEN + ''}]"
          f"{Fore.BLUE + '  Exiting the program...'}")
    time.sleep(1)
    exit(1)


signal.signal(signal.SIGINT, ctrl_c)


# Colours
def get_colours(text, color):
    if color == "blue":
        blue_color = Fore.BLUE + text
        print(blue_color)
    elif color == "red":
        red_color = Fore.RED + text
        print(red_color)


def data_parser(packet_info):
    if packet_info.haslayer(ICMP):
        if packet_info[ICMP].type == 8:
            byte_data = packet_info['ICMP'].load[-4:].decode('utf-8')
            print(byte_data, flush=True, end='')


if len(sys.argv) != 2:
    print(f"\n{Fore.BLUE + '┃'}  {Fore.GREEN + '['}{Fore.RED + '!'}{Fore.GREEN + ''}]"
          f"{Fore.YELLOW + f' Usage {sys.argv[0]} <Interface-Name>'}")
else:
    try:
        print(f"\n{Fore.BLUE + '┃'}  {Fore.GREEN + '['}{Fore.BLUE + '*'}{Fore.GREEN + ''}]"
              f"{Fore.BLUE + '  Listening for any incoming connections...'}")
        print(Fore.WHITE)  # To avoid leaving the terminal with colors.
        sniff(iface=f'{sys.argv[1]}', prn=data_parser)
    except PermissionError:
        print(f"\n{Fore.BLUE + '┃'}  {Fore.GREEN + '['}{Fore.RED + '!'}{Fore.GREEN + ''}]"
              f"{Fore.RED + ' Run this script with administrator privileges.'}")
        print(Fore.WHITE)
    except OSError:
        print(f"\n{Fore.BLUE + '┃'}  {Fore.GREEN + '['}{Fore.RED + '!'}{Fore.GREEN + ''}]"
              f"{Fore.RED + '  No such interface found'}")
        print(Fore.WHITE)
