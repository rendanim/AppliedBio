#!/usr/bin/env python3
from Bio import SeqIO
import sys
from Bio.Blast import NCBIXML
import re
from operator import itemgetter

threshold = 1e20
pattern=sys.argv[1]
b_file = sys.argv[2]
result_handle = open(b_file)
blast_records = NCBIXML.parse(result_handle)
#blast_records= list(blast_records)

#print(len(blast_records))
#print(blast_records[0].alignments)
output=list()
for record in blast_records:
        for alignment in record.alignments:
            # hsp = high scoring pair
            for hsp in alignment.hsps:
                if (hsp.expect < threshold and re.search(pattern, alignment.title)):
                    #print(record.query,end='\t')
                    assession_sub = alignment.title.split('lcl|')[1].split(' ')[0]
                    #print(assession_sub,end='\t')
                    #print(hsp.score,end='\t')
                    #print(hsp.expect)
                    output.append([record.query, assession_sub,hsp.score,hsp.expect])     


sort_out=sorted(output,key=itemgetter(1, 3))
#print(sort_out)
#sort remove higher e-values
for i in range(len(sort_out)):
    if(i>0 and sort_out[i][1]==sort_out[i-1][1]):
        continue
    else:           
        print(sort_out[i][0],end='\t')
        print(sort_out[i][1],end='\t')
        print(sort_out[i][2],end='\t')
        print(sort_out[i][3])
                    