#!/usr/bin/env python3
import sys

files=sys.argv[1:]
nfiles=len(files)

def readfiles(files,nfiles):
    '''Reads files and sends lines to gc_counter
    Arguments: files - list of files
               nfiles -number of files'''
    file_counts=list()
    names=list()           
    for i in range(nfiles):
        #print('Reading---'+files[i])
        f=open(files[i], 'r')
        #print(f.readline())
        Base_dict = {'A': 0, 'C': 0, 'G': 0,'T':0 }
        file_counts.append(Base_dict)
        names.append(f.readline().split()[0][1:11])
        for line in f:
            if(line[0]!='>'):
                '''Donot count the sequence name'''
                file_counts[i] = base_count(file_counts[i],line)
        file_counts[i]=normalize(file_counts[i])     
    dist=calc_dist(file_counts)
    print_output(dist,names) 
        #print(fc) 

def base_count(Base_dict,line):
    '''Count GC in each line sent by readfiles'''
    
    for l in line:
        if(l=='A' or l=='C' or l=='G' or l=='T'):
            Base_dict[l] = Base_dict[l]+1
           
    return Base_dict

def normalize(Base_dict):
    sb=0
    for key in Base_dict:
        sb=sb+Base_dict[key]
    for key in Base_dict:
        Base_dict[key]=Base_dict[key]/sb
    return Base_dict       
def calc_dist(file_counts):
    
    dist=list()
    for i in range(len(file_counts)):
        for j in range(len(file_counts)):
            dist.append((0.25*((file_counts[i]['A']-file_counts[j]['A'])**2 + (file_counts[i]['C']-file_counts[j]['C'])**2+ \
            (file_counts[i]['G']-file_counts[j]['G'])**2 + (file_counts[i]['T']-file_counts[j]['T'])**2))**(0.5))
            
    return dist        

def print_output(dist,names):
    n=len(names)
    print(n)
    for i in range(n):
        if(len(names[i])<10):
            names[i]=names[i].ljust(10)
        print(names[i], end='')
        print_row(dist[n*i:(i+1)*n])

def print_row(l):
    for i in range(len(l)):
        n=len(l)
        if(i==(n-1)):
            print('{:0.3f}'.format(l[i]),end='\n')
        else:
            print('{:0.3f}'.format(l[i]),end=' ')


def main():
    '''Read the files first'''
    readfiles(files,nfiles)

if __name__ == "__main__":
    if len(sys.argv[1:]) == 0:
        sys.stderr.write("Error: No files were provided. Provide at least 2 FASTA files. \n")
        sys.exit(-1)
    else:
        files = sys.argv[1:]
        for filename in files:
            if '.fa' not in filename:
                sys.stderr.write(
                    "Error: Non FASTA file detected. Make sure the files have compatible file endings (.fa). \n")
                sys.exit(-1)
            try:
                 f=open(filename, 'r')
            except IOError:
                sys.stderr.write("Error: " + filename + " was not found. \n")
                sys.exit(-1)
        main()
               