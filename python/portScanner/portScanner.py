#!/bin/python

import sys
import socket
from datetime import datetime

# obbietivo

if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1]) # tradure in una direzione IPV4
else:
        print("La sintassi e sbagliata. Ci vogliono pui argumenti \n s-> python3 portScanner.py <ip>")

print("*"*50)
print(f"Scassionando Obbietivo: {target}")
print("Tempo " + str(datetime.now()))
print("*"*50)


try:
        for port in range(50,85):
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((target,port))
                if(result == 0):
                        print(f"{port} e aperto")
                s.close()
except KeyboardInterrupt:
        print("L' operazione e stata cancellata. Uscendo dal programa")
        sys.exit()
except socket.gaierror:
        print("Non e stato possibile di risolvere il Hostname")
        sys.exit()
except socket.error:
        print("Il servitore non risponde")
        sys.exit()

