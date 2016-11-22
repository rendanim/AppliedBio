#!/usr/bin/env python3
import glob
import  os

os.chdir("../data")
for file in glob.glob("*.fna"):
    print('Reading---'+file)
    f=open(file, 'r')
    print(f.readline())
    lines=0
    chars=0
    for line in f:
        if(lines>0):
            chars += len(line)
        lines+=line    #print(chars)
    print('Length of Genome: '+str(chars)+' Lines: '+str(lines))