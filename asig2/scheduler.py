'''
Christopher L. Ayala-Griffin
Asignación 2: Threads and Scheduling
CCOM4017_0U1: Sistemas Operativos

'''

import threading, time, random, socket, sys
from threading import Thread

# global variables
id = 0
cpu_time = 0
n = 10
mybuffer = []
index = 0
count_id = [-1]*n
count_time = [0]*n
no_of_processes = [0]
full = threading.Semaphore(0)
empty = threading.Semaphore(n)
mutex = threading.Lock()


if len(sys.argv)<2:
    print("Faltan uno o más de los parametros requeridos")
    sys.exit()
else:
    port = int(sys.argv[1])

class ProducerThread(Thread):
    # The constructor assign the internal id to the new thread.
    def __init__ (self, t_number):
        # This variable is used to assign an internal id to the thread.
        self.t_number = t_number
        self.running = True
        Thread.__init__(self)

    def run(self):
        producer_thread(self)   # Hacer ProducerThread

class ConsumerThread(Thread):
    # The constructor assign the internal id to the new thread.
    def __init__ (self, t_number):
        # This variable is used to assign an internal id to the thread.
        self.t_number = t_number
        self.running = True
        Thread.__init__(self)

    def run(self):
            consumer_thread(self)   # Hacer ConsumerThread

def create_socket():
# Create a UDP socket
    global s
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
        print("Failed to create socket.")
        sys.exit()

        # Bind the socket to the port
    try:
        s.bind(('',port))
    except socket.error:
        print("Bind failed.")
        sys.exit()
    print("Socket bind complete")

def run_socket():
    global data
    global address
    # Receive data from client
    data, address = s.recvfrom(1024)
    if data:
        data = data.decode()
        if data == "done":
            data = 0
            print("Closing socket")
            s.close()
            
    else:
        print("No data received")
        print("Closing socket")
        s.close()

def producer_thread(self):
    #define producer funcion
    while self.running:
        item = produce_item(self)
        empty.acquire()
        mutex.acquire()
        insert_item(self, item)
        mutex.release()
        full.release()

def consumer_thread(self):
    #define consumer function
    while self.running:
        full.acquire()
        mutex.acquire()
        item = remove_item()
        mutex.release()
        empty.release()
        consume_item(self, item)

def produce_item(self):
    # producer thread to run socket
    run_socket()
    if data == 0:
        self.running = False
    else:
        return data

def insert_item(self, item):
    data = 0
    if not self.running:
        print("No data to insert. Endind producer.")
    elif mybuffer:
        first_element = mybuffer[0].split(':')
        item_split = item.split(':')
        # sort by smallest time first
        if first_element[1] > item_split[1]:
            mybuffer.insert(0, item)
        else:
            mybuffer.append(item)
    else:
        mybuffer.append(item)
        
def remove_item():
    item = mybuffer.pop()
    return item
    
def consume_item(self, item):
    id, cpu_time = process_item(item)
    reply = "Device {} with CPU time {} processed.".format(id, cpu_time)
    # Send back processed data to client
    s.sendto(reply.encode(), address)
    time.sleep(cpu_time)
    # when jobs are done and buffer empty print results and end consumer loop
    if not mybuffer:
        num_p = no_of_processes[0]
        for i in range(num_p):
            print("Device {} consumed {} seconds of CPU time.".format(count_id[i], count_time[i]))
        self.running = False

def process_item(item):
    item = item.split(":")
    id = int(item[0])
    cpu_time = int(item[1])
    # set a count for devices and their respective time.
    for i in range(n):
        if (id == count_id[i]):
            count_time[id] = count_time[id] + cpu_time
            return (id, cpu_time)
    no_of_processes[0] = no_of_processes[0] + 1
    count_id[id] = id
    count_time[id] = count_time[id] + cpu_time
    return (id, cpu_time)
    
def main():
    # define main, and create socket
    create_socket()
    # to create and start threads
    prodT = ProducerThread(1)
    consT = ConsumerThread(2)
    prodT.start()
    consT.start()
    # wait for each thread to finish  before killing processes
    prodT.join()
    consT.join()

    print("Jobs are done!")

if __name__ == "__main__":
    main()

