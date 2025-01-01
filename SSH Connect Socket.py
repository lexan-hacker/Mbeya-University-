# SSH connect socket whatsoever 

import socket

s = socket.socket()

try :

    s.connect(("192.168.1.101" , 22))
    

    answer = s.recv(1024)

    print(answer)

    s.close

except OSError :
    print( " The Computer has problem resolving the host mentioned ")
