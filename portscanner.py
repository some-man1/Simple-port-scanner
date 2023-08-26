import socket
import threading
import os, sys

target_ip = sys.argv[1]

def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

stop_event = threading.Event()

if not is_valid_ip(target_ip):
    print("\033[91m" + "Usage: python portscanner.py " + '\033[34m' "<target_ip>")
    sys.exit(1)


def banner():
    print("\033[32m" + """

                                                                                                                              
                                                                                                                              
                                 ___                                                                                          
,-.----.                       ,--.'|_                                                                                        
\    /  \    ,---.    __  ,-.  |  | :,'                                                  ,---,      ,---,             __  ,-. 
|   :    |  '   ,'\ ,' ,'/ /|  :  : ' :           .--.--.                            ,-+-. /  | ,-+-. /  |          ,' ,'/ /| 
|   | .\ : /   /   |'  | |' |.;__,'  /           /  /    '     ,---.     ,--.--.    ,--.'|'   |,--.'|'   |   ,---.  '  | |' | 
.   : |: |.   ; ,. :|  |   ,'|  |   |           |  :  /`./    /     \   /       \  |   |  ,"' |   |  ,"' |  /     \ |  |   ,' 
|   |  \ :'   | |: :'  :  /  :__,'| :           |  :  ;_     /    / '  .--.  .-. | |   | /  | |   | /  | | /    /  |'  :  /   
|   : .  |'   | .; :|  | '     '  : |__          \  \    `. .    ' /    \__\/: . . |   | |  | |   | |  | |.    ' / ||  | '    
:     |`-'|   :    |;  : |     |  | '.'|          `----.   \'   ; :__   ," .--.; | |   | |  |/|   | |  |/ '   ;   /|;  : |    
:   : :    \   \  / |  , ;     ;  :    ;         /  /`--'  /'   | '.'| /  /  ,.  | |   | |--' |   | |--'  '   |  / ||  , ;    
|   | :     `----'   ---'      |  ,   /         '--'.     / |   :    :;  :   .'   \|   |/     |   |/      |   :    | ---'     
`---'.|                         ---`-'            `--'---'   \   \  / |  ,     .-./'---'      '---'        \   \  /           
  `---`                                                       `----'   `--`---'                             `----'            
                                                                                                                              

""")

    print('\033[91m' + "My website : " + "\033[32m" + "https://rdkgt7us.000webhostapp.com/")
    print('\033[91m' + "My instgram : " + "\033[32m" + "r_d515\n")

   
def clear():  
    os.system("cls")
    os.system("clear")
 
        
shape = '\033[34m' + "[" +  '\033[91m' + "+" + '\033[34m' + "]"



def scan_port(ip, port):
    """The function who scan
    ip // The target who will get scan
    port // The ports
    """
    try:
        if not stop_event.is_set():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect((ip, port))
            print(str(shape) + "\033[32m" + f" Port {port} is open")
            sock.close()
        else:
            print("\033[32m" + "\nStopping the scan...")
    except:
        print(str(shape) + '\033[91m' + f" Port {port} is closed")

def main():
    """This is the function who make config to the scan function"""
    clear()
    banner()
    try:
        for port in range(1, 65553):
            if stop_event.is_set():
                break  
            scan_port(target_ip, port)
    except KeyboardInterrupt:
        stop_event.set()  
        pass


scan_thread = threading.Thread(target=main)
scan_thread.start()


try:
    # Keep the main thread running
    while scan_thread.is_alive():
        scan_thread.join(timeout=1)
except KeyboardInterrupt:
    stop_event.set()  
    print(f"\n {shape} Thans for using :)")
