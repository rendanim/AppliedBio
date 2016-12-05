#!/usr/bin/env python3
import matplotlib.pyplot as plt
import sys
from Bio.Blast import NCBIXML
from matplotlib.backends.backend_pdf import PdfPages
import argparse






def count_scores(b_file,outputfile):
    
    result_handle = open(b_file)
    blast_records = NCBIXML.parse(result_handle)



    output=list()
    for record in blast_records:
            for alignment in record.alignments:
                # hsp = high scoring pair
                for hsp in alignment.hsps:
                    output.append(hsp.score)

    makepdf(output,outputfile)

def makepdf(output,outputfile):
    ofile = PdfPages(outputfile)
    plt.figure()
    plt.hist(output)
    plt.xlabel('Score')
    plt.ylabel('Frequency')
    plt.title('Histogram of Scores')
    ofile.savefig()
    ofile.close()


def main():
    parser = argparse.ArgumentParser(description='Saves an PDF file for Scores from the BLAST scores')
    parser.add_argument('xmlfile', help='XML input file.')
    parser.add_argument('outfile', help="Name.")
    args = parser.parse_args()
    count_scores(args.xmlfile,args.outfile)

    

if __name__=='__main__':
    main()