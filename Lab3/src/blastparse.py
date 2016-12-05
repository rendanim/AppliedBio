#!/usr/bin/env python3
from Bio import SeqIO
import sys
from Bio.Blast import NCBIXML
import re

threshold = 1e20
pattern=sys.argv[1]
b_file = sys.argv[2]
result_handle = open(b_file)
blast_records = NCBIXML.parse(result_handle)
#blast_records= list(blast_records)

#print(len(blast_records))
#print(blast_records[0].alignments)

for record in blast_records:
        for alignment in record.alignments:
            # hsp = high scoring pair
            for hsp in alignment.hsps:
                print(hsp.expect)
                