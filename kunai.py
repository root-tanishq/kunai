#!/usr/bin/python3
import socket
import sys
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
art = f"""{bcolors.WARNING}
   __ __               _ 
  / //_/_ _____  ___ _(_)
 / ,< / // / _ \/ _ `/ / 
/_/|_|\_,_/_//_/\_,_/_/  
            -Boy From Future                         
"""
print(art)
try:
    port = int(sys.argv[1])
    print(f"{bcolors.HEADER}Creating socket")
    host = 'localhost'
    file = open(f'{sys.argv[2]}', 'r')
    webserver = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    webserver.bind((host , port ))
    print(f'{bcolors.OKGREEN}Socket created')
    webserver.listen(5)
    while True:
        clientsocket , address = webserver.accept()
        print(f'{bcolors.OKBLUE}Established connection with {address}')
        message = f'HTTP/1.1 200 OK\r\n\r\n {str(file.read())} \r\n'
        clientsocket.send(message.encode())
        clientsocket.close()
except:
    help_output = f"""{bcolors.FAIL}
-------------USAGE-------------
python3 kunai.py [PORT] [FILE LOCATION]

PORT            = port you want to use for webserver
FILE LOCATION   = location to index.html
-------------------------------
"""
    print(help_output)