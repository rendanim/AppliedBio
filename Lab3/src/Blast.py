#!/usr/bin/env python3
from Bio import SeqIO
import sys
from Bio.Blast import NCBIWWW

prot_file = sys.argv[1]
fasta_string = open(prot_file).read()
#print(fasta_string)
result_handle = NCBIWWW.qblast("blastp", "pdb", fasta_string)
print(result_handle.read())
result_handle.close()