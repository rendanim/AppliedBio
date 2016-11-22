#!/usr/bin/env python3
import sys

files=sys.argv[1:]
nfiles=len(files)

def readfiles(files,nfiles):
    '''Reads files and sends lines to gc_counter
    Arguments: files - list of files
               nfiles -number of files'''
    for i in range(nfiles):
        print('Reading---'+files[i])
        f=open(files[i], 'r')
        #print(f.readline())
        
        fc=0
        gc=0
        for line in f:
            if(line[0]!='>'): 
                '''Donot count the sequence name'''
                lcc,gcc = gc_count(line)
                fc=fc+lcc
                gc=gc+gcc
        ratio=gc/fc
        print(ratio)
        #print(gc)
        #print(fc) 

def gc_count(line):
    '''Count GC in each line sent by readfiles'''
    gc=0
    lc=0
    for l in line:
        if(l=='G'or l=='C'): 
            '''check G OR C'''
            gc+=1
        lc+=1
        '''Return count for the line'''
    return lc,gc

def main():
    '''Read the files first'''
    readfiles(files,nfiles)

if __name__ == "__main__":
    main()
           