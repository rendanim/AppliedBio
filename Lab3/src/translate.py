#!/usr/bin/env python3

from Bio import SeqIO
import sys

dna_file=sys.argv[1]


def translate():
    seq_file = list(SeqIO.parse(dna_file,'fasta'))

    for i in range(len(seq_file)):
        print('>',end='')
        print(seq_file[i].id)
    
        trans=seq_file[i].seq.translate()
        print(trans)

def main():
    translate()

if __name__=='__main__':
    main()