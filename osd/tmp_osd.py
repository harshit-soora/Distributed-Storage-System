"""
@author: Kartik Saini

"""

import socket
import pickle
from transfer import _send_msg, _recv_msg
HEADERSIZE = 10

# def _send_msg(socket, msg):
#     msg = pickle.dumps(msg)
#     # msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
#     print(msg)
#     socket.send(msg)
    
# def _recv_msg(socket, size):
#     full_msg = ''
#     new_msg = True
#     msg = socket.recv(1024)
    
#     r_msg = pickle.loads(msg)
        
#     print(r_msg)
    
#     return r_msg
     
s = socket.socket()         
print ("Socket successfully created")
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12346              
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
  
# put the socket into listening mode 
s.listen(5)     
print ("socket is listening")            
  
# a forever loop until we interrupt it or 
# an error occurs 
while True: 
  
    # Establish connection with client. 
    c, addr = s.accept()     
    print ('Got connection from', addr )
      
    # send a thank you message to the client. 
    msg = _recv_msg(c, 1024)
    
    print(msg)
    
    if(msg["type"] == "WRITE"):
    	pg = msg["PG"]
    	file = open("./data/"+pg.pg_id, 'wb')

    	pg_b = pickle.dumps(pg)
    	file.write(pg_b)

    	# pickle.dump(pg, file)
    	file.close()

    	_send_msg(c, [pg.pg_id, "SUCCESS"])

    elif msg["type"] == "READ":
    	pg_id = msg["PG_id"]
    	file = open("./data/"+pg_id, 'rb')

    	pg_b = file.read()
    	pg = pickle.loads(pg_b)

    	file.close()
    	# print(pg)
    	msg = {"pg_id": pg.pg_id, "res":"SUCCESS", "PG":pg}

    	_send_msg(c, msg)

    c.close()
    
    print("RECV")
    print(msg)

s.close()
# Close the connection with the client 
#c.close()
