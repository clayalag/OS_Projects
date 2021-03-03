'''
Christopher L. Ayala-Griffin
801-12-0585
Asignación 3: Memory Management
CCOM4017_0U1: Sistemas Operativos

'''
import sys, os.path

class PMP:
    mod_bit = 0 # bit modificado
    page_num = 0
    time_ = 0 # last accessed
    ref_bit = 1

def usage():
    print ("Usage:\n\tpython %s <Number of physical memory pages> <tau> <access sequence file>\n\t" % (sys.argv[0],))
    sys.exit(0)
    
def file_read(fname):
    with open(fname, "r") as f:
        #vmp_list contains the read lines
        vmp_list = f.read()
        vmp_list = vmp_list.split()
    return vmp_list
    
def find_in_list(vmp, r_or_w, pmp):
    for i in range(len(pmp)):
        if vmp.page_num == pmp[i].page_num:
            pmp[i].ref_bit = 1
            if r_or_w == 'W':
                pmp[i].mod_bit = 1
            return True
    return False
    
def clock(vmp_list, num_pmp, tau):
    pmp = []
    page_faults = 0
    puntero = 0
    t_clock = 0
    for line in range(len(vmp_list)):
        vmp = PMP()
        t = vmp_list.pop(0)
        r_or_w, dat = t.split(":")
        vmp.page_num = int(dat)
        found = find_in_list(vmp, r_or_w, pmp)
        if found == False:
            if len(pmp) < num_pmp:
                if r_or_w == 'W':
                    vmp.mod_bit = 1 #modified bit encendido para write
                vmp.time_ = t_clock
                pmp.append(vmp)
                puntero = (puntero + 1) % num_pmp
                t_clock += 1
            else:
                while True:
                    #referenciado y modify bit encendido
                    if pmp[puntero].ref_bit == 1 and pmp[puntero].mod_bit == 1:
                        pmp[puntero].mod_bit = 0
                        pmp[puntero].ref_bit = 0
                        pmp[puntero].time_ = t_clock
                    # reference bit encedido
                    elif pmp[puntero].ref_bit == 1:
                        pmp[puntero].ref_bit = 0
                        pmp[puntero].time_ = t_clock
                    # modify bit encendido
                    elif pmp[puntero].mod_bit == 1:
                        pmp[puntero].mod_bit = 0
                        pmp[puntero].time_ = t_clock
                    # verificar aging; si es mayor que tau se sustituye en ese lugar
                    elif (t_clock - pmp[puntero].time_) > tau:
                        pmp[puntero].page_num = vmp.page_num
                        pmp[puntero].time_ = t_clock
                        t_clock += 1
                        puntero = (puntero + 1) % num_pmp
                        break
                    t_clock += 1
                    puntero = (puntero + 1) % num_pmp
            page_faults += 1
    print("\nTotal page faults :",page_faults)

if __name__=="__main__":

    if len(sys.argv) == 4:
        num_pmp = int(sys.argv[1])
        tau = int(sys.argv[2])
        file_ = sys.argv[3]
    else:
        usage()
    vmp_list = file_read(file_)
    clock(vmp_list, num_pmp, tau)

