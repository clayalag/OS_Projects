###############################################################################
#
# Filename: mds_db.py
# Author: Jose R. Ortiz and ... Christopher L. Ayala-Griffin
#
# Description:
# 	List client for the DFS
#


import socket
import sys

from Packet import *

def usage():
	print ("Usage: python %s <server>:<port, default=8000>" % sys.argv[0])
	sys.exit(0)

def client(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip,port))
    p = Packet()
    p.BuildListPacket()
    msg = p.getEncodedPacket()
    sock.sendall(msg.encode())
    msg = sock.recv(1024).decode()
    p.DecodePacket(msg)
    print(msg)
    sock.close()  #   cierra coneccion
	# Contacts the metadata server and ask for list of files.

if __name__ == "__main__":

	if len(sys.argv) < 2:
		usage()

	ip = None
	port = None 
	server = sys.argv[1].split(":")
	if len(server) == 1:
		ip = server[0]
		port = 8000
	elif len(server == 2):
		ip = server[0]
		port = server[1]

	if not ip:
		usage()

	client(ip, port)
