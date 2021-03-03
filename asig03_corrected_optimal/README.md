
# **README**

### Incluye Optimal Page Replacement Algorithm V.2


### **Introducción**

Estos programas de page replacement algorithm (PRA) son simulaciones que tienen como fin demostrar el funcionamiento del manejo de memoria de los Sistemas Operativos.
Los algoritmos implementados son:
    ● Last In First Out
    ● Optimal Replacement Algorithm
    ● WSClock Page Replacement Algorithm (WSCRA)


### **Objetivos**

    ● Estudiar la implementación de los tres algoritmos de reemplazamiento a implementar.
    ● Familiarizarse con el manejo de memoria.
    ● Implementación de modelos de simulación.
    ● Implementación de buenas técnicas de programación.

### **Programming Language**

    *Python3*


### **Programas**

    ● lifo.py
    ● optimal.py
    ● wsclock.py

### **Algunas especificaciones**
    ● Espacio en memoria fisica es N = 10.
    ● El programa lee un archivo de texto y extrae los valores numericos a ser reemplazados en página de memoria física.
    ● El programa tiene un contador para page faults cada vez que no encuentré una página de memoria virtual en memoria física y al terminar se imprimirá la cantidad de page faults para los diferentes algoritmos

## **Como correr los programas:**

    Para correr lifo PRA:
        *#python lifo.py <Número de páginas en memoria ficical> <archivo.txt>*

    Para correr optimal PRA:
        *#python optimal.py <Número de páginas en memoria ficical> <archivo.txt>*
        
    Para correr WS Clock PRA:
        *#python wsclock.py<Número de páginas en memoria ficical> <tau> <archivo.txt>*

### Algoritmo de LIFO y Optimal

    El algoritmo de lifo esta implementado de manera que la última dirección entrada a memoria fisica, es la primera en ser reemplazada.
    
    Para el algoritmo de optimal se reemplazará el valor que más lejano se accesará en memoria.
    
### ***Working Set Clock Replacement Algorithm***

    Este algoritmo tiene un reloj para llevar cuenta del último tiempo en que fue accesada cada página en memoria. Cada vez que se acceda una página se actualizará con el tiempo del reloj en ese momento de ser accesado. También tendrá un valor de tau que se utilizará para saber si la página esta en el working set, sino se reemplaza.

    
### Referencias:

* https://www.w3schools.com/python/ref_string_index.asp *
*https://www.geeksforgeeks.org/page-replacement-algorithms-in-operating-systems/*
*https://www.youtube.com/watch?v=C26qsPwf-Js&feature=youtu.be*
*https://www.youtube.com/watch?v=pJ6qrCB8pDw&list=PLIY8eNdw5tW-BxRY0yK3fYTYVqytw8qhp*
*Modern-Operating-System-Tanenbaum 3rd ed*
*Python Programming: An Introduction to Computer Science by Franklin Beedle and Associates (2016---John-M.-Zelle) 3rd ed*
