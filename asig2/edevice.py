'''
Christopher L. Ayala-Griffin
Asignación 2: Threads and Scheduling
CCOM4017_0U1: Sistemas Operativos

'''

import threading, time, random, socket, sys
from threading import Thread

N =  5 # Maximum messages

sleep_ = range(1,4)  # range of sleeps times

job_time = range(1,6) # range of job time

if len(sys.argv)<3:
    print("Faltan uno o más de los tres parametros requeridos")
    sys.exit()
else:
    port = int(sys.argv[2])
    host = sys.argv[1]

# create client socket
try:
    client_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print("Failed to create socket")

client_address = (host, port)

class DevicesThread(Thread):

	# The constructor assign the internal id to the new thread.
    def __init__ (self, t_number):
		# This variable is used to assign an internal id to the thread.
        self.t_number = t_number
        Thread.__init__(self)
	# Define inside what the thread is to do.
    def run(self):
        start = int(self.t_number * N/2)
        end = int((self.t_number + 1) * N/2)
        
        if self.t_number == 1:
            end = N
            
        i = start
        while(i < end):
            send_message(self)
            i += 1

def send_message(self):
    work_t = random.choice(job_time) # get random job time
    message = "%s:%s"%(self.t_number, work_t)
    msg = message
    # Send data
    print('sending {}'.format(msg))

    try:
        client_socket.sendto(msg.encode(), (host, port))
        # Receive response
        print('waiting to receive')
        data, address = client_socket.recvfrom(1024)

    except socket.error:
        print("Error")
        sys.exit()
            
def main():
    # start threads
    idealThreads = 2
    thread = [0] * idealThreads

    for i in range(idealThreads):
        thread[i] = DevicesThread(i)
        thread[i].start()

	# Make the original thread wait for the created threads.
    for i in range(idealThreads):
        thread[i].join()
        
    print('closing socket')
    empty = "done"
    client_socket.sendto(empty.encode(), (host, port))
    client_socket.close()

	# Display buffer content
    print("I'm done.")

if __name__ == "__main__":
    main()
