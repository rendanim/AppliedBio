#!/usr/bin/env python3

from Bio import SeqIO
import sys
import re

prot_file = sys.argv[1]
prot_file = list(SeqIO.parse(prot_file,'fasta'))
def kleek():
  
    pattern = re.compile('KL([EI]{2,})+K{1}')
    j = 0
    for i in range(len(prot_file)):
        
        m=pattern.search(str(prot_file[i].seq))
        if m:
            print('>',end='')
            print(prot_file[i].id,end='\t')
            print('This sequence contains KLEEK')
            print(prot_file[i].seq)
            j += 1
        else:
            print('>',end='')
            print(prot_file[i].id,end='\t')
            print('There is no KLEEK-like motif in this sequence')
            #print(prot_file[i].seq)
       
    print(j)
            

def main():
    kleek()

if __name__=='__main__':
    main()