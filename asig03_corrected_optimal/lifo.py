'''
Christopher L. Ayala-Griffin
801-12-0585
Asignación 3: Memory Management
CCOM4017_0U1: Sistemas Operativos

'''

import sys, os.path

def usage():
    print ("Usage:\n\tpython %s <Number of physical memory pages> <access sequence file>\n\t" % (sys.argv[0],))
    sys.exit(0)
    
def file_read(fname):
    content_array = []
    with open(fname, "r") as f:
        for line in f:
            line=line.split()
            largo=len(line)
            print(line)
            for i in range(largo):
                if line[i] != '\n':
                    content_array.append(line[i])
    a=split_data(content_array)
    print(a)
    return a
        
def split_data(content):
    largo=len(content)
    a=[]
    for i in range(largo):
        item = content[i]
        item = item.split(":")
        a.append(item[1])
    return a
    
def lifo(vmp, num_pmp):
    largo = len(vmp)
    pmp = [-1]*num_pmp
    page_faults = 0
    count_index = 0
    for i in range(largo):
        flag = 0
        for j in range(num_pmp):
            if(pmp[j]==vmp[i]): # verifica si esta
                flag=1
                break
        if (flag==0 and (pmp[count_index]==-1)): #si no esta, fault; las primeras entradas siempre son fault
            pmp[count_index]=vmp[i]
            if count_index < num_pmp-1:
                count_index+=1
            page_faults+=1
        elif (flag==0 and (i >= num_pmp)):
            pmp[num_pmp-1]=vmp[i]
            page_faults+=1
    
    print("\nTotal page faults:", page_faults)

if __name__=="__main__":

    if len(sys.argv) == 3:
        num_pmp = int(sys.argv[1])
        file_ = sys.argv[2]
    else:
        usage()
    vmp_list=file_read(file_)
    lifo(vmp_list, num_pmp)
