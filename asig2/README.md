# **README**


### **Introduction**

In this project the student will simulate a Shortest Job First scheduling algorithm for a distributed system that consists of embedded devices and a central compute server. The student will assume that we have multiple embedded devices that generate computational problems that are too heavy to be performed in their hardware, either because the device's battery will drain, they do not have enough memory, nor computational resources to perform them in a timely manner. We will simulate a central server (can be a cluster) that will receive requests for computing time from the embedded devices, will put the jobs in a queue of processes, and then will “execute” them.


### **Objectives**

    ● Practice threads implementations
    ● Practice inter process communication using sockets (UDP) and a shared buffer
    ● Identify critical regions
    ● Implementation of mutual exclusion and semaphores

### **Programming Language**
        
    *Python3*
    
### **Requiered modules and libraries:**

    ●threading
    ●time
    ●random
    ●socket
    ●sys
    ● Thread

### **Files and Programs**
    ● edevice.py
    ● scheduler.py
    
## **Example how to run programs:**

    How to run the embedded devices:
        *#python edevice.py <server address> <server port>*
    
    How to run the server:
        *#python scheduler.py <server port>*
### Referencias:

*https://www.binarytides.com/programming-udp-sockets-in-python/*
*https://pymotw.com/3/threading/*
*https://docs.python.org/3/library/socket.html*

