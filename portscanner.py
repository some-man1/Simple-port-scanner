import socket
import threading
import os
from sys import argv,exit
from banner import banner

try:
    target_ip = argv[1]
except:
    print("Usage : python3 main.py <ip or domain>")
    exit()

   
def clear():  
    os.system("cls")
    os.system("clear")
 
        
shape = '\033[34m' + "[" +  '\033[91m' + "+" + '\033[34m' + "]"



def scan_port(ip, port):
    """The function who scan
    ip ---> The target who will get scan
    port ---> The ports
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect((ip, port))
        print(str(shape) + "\033[32m" + f" Port {port} is open")
        sock.close()
    except:
        print(str(shape) + '\033[91m' + f" Port {port} is closed")

def main():
    """This is the function will make every thing work"""
    clear()
    banner()
    for port in range(1, 65553):
            scan_port(target_ip, port)


scan_thread = threading.Thread(target=main)
scan_thread.start()


try:
    # Keep the main thread running
    while scan_thread.is_alive():
        scan_thread.join(timeout=0.1)  
except KeyboardInterrupt:  
    print(f"\n\n{shape} Thanks for using :)")
