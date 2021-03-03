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
            for i in range(largo):
                if line[i] != '\n':
                    content_array.append(line[i])
    a=split_data(content_array)
    return a
        
def split_data(content):
    largo=len(content)
    a=[]
    for i in range(largo):
        item = content[i]
        item = item.split(":")
        a.append(item[1])
    return a
    
def optimal(vmp, num_pmp):
    pmp =[]
    fault = 0
    largo = len(vmp)
    valor_mas_lejano = [-1 for i in range(num_pmp)]
    for i in range(largo):   # recorre largo de virtual memory pages
        flag = 0
        if vmp[i] not in pmp:
            if len(pmp)<num_pmp:    # si es fault y todavia hay espacios vacios
                pmp.append(vmp[i])
            else:
                for x in range(len(pmp)):
                    if pmp[x] not in vmp[i+1:]: # busca por algun valor que no volvera a ser utilizado en el futuro, si encuetra uno que no se volvera a usar, sustituye en esa posicion
                        flag = 0
                        pmp[x] = vmp[i]
                        break
                    else:
                        flag = 1
                        valor_mas_lejano[x] = vmp[i+1:].index(pmp[x]) # busca ocurrencia de valor de pmp[x] en virtual memory page
                if flag == 1:
                    pmp[valor_mas_lejano.index(max(valor_mas_lejano))] = vmp[i] # asigna el valor en virtual memory al valor maximo en valor mas lejano (al valor más lejano en vmp)

            fault += 1
    print("\nTotal Page Faults: %d"%(fault))
    
if __name__=="__main__":

    if len(sys.argv) == 3:
        num_pmp = int(sys.argv[1])
        file_ = sys.argv[2]
    else:
        usage()
    vmp_list=file_read(file_)
    optimal(vmp_list, num_pmp)
