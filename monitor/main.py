"""
@author: Kartik Saini
@author: Harshit Soora
@author: Vivek Vardhan Adepu
@author: Shivang Gupta
@author: Deepak Imandi

"""

from monitor.monitor_gossip import heartbeat_protocol
import socket
import pickle
import sys
sys.path.insert('../utils/')
from transfer import _send_msg, _recv_msg
from object_pg import DataObject, PlacementGroup

def main():
    init_hashtable
    init_network_topology
    recv_write_acks_thread
    recv_req_client_thread
    recv_osd_status_thread
    #HEADERSIZE = 10

    # s = socket.socket()
    # print ("Socket successfully created")

    # # reserve a port on your computer in our
    # # case it is 12345 but it can be anything
    # port = 1234

    # # Next bind to the port
    # # we have not typed any ip in the ip field
    # # instead we have inputted an empty string
    # # this makes the server listen to requests
    # # coming from other computers on the network
    # s.bind(('', port))
    # print ("socket binded to %s" %(port))

    # # put the socket into listening mode
    # s.listen(5)
    # print ("socket is listening")

    # # a forever loop until we interrupt it or
    # # an error occurs
    # while True:

    #     # Establish connection with client.
    #     c, addr = s.accept()
    #     print ('Got connection from', addr )

    #     # send a thank you message to the client.
    #     msg = _recv_msg(c, 1024)

    #     print(msg)

    #     res = {"osd_ip":[["127.0.0.1", 12346], ["127.0.0.1", 8090]]}

    #     _send_msg(c, res)

    #     c.close()

    # s.close()
    # # Close the connection with the client
    # #c.close()


if __name__ == '__main__':
	main()