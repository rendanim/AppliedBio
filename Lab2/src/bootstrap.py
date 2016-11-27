#!/usr/bin/env python3
from Bio import SeqIO
from Bio.Alphabet import ProteinAlphabet
import sys
import tempfile
import pexpect
import os


if len(sys.argv[1:]) == 0:
    sys.stderr.write("Usage: bootstrap <filename> <number of bootstraps>. \n")
    sys.exit(-1)
elif len(sys.argv[1:]) > 2:
    sys.stderr.write("Error: Too many arguments \n")
    sys.exit(-1)
elif len(sys.argv[1:]) < 2:
     sys.stderr.write("Error: Too few arguments \n")
     sys.exit(-1)

sqnc_file=sys.argv[1]

n_sample=sys.argv[2]
seqs=list(SeqIO.parse(sqnc_file, "fasta"))
temp=tempfile.NamedTemporaryFile(delete=False)
header=str(len(seqs))+'\t'+str(len(seqs[0].seq))+'\n'
temp.write(bytes(header,'UTF-8'))
species={}
i=0
for seq_record in seqs:
    new_id=('Record'+str(i)).ljust(10)
    species[new_id.strip()]=seq_record.id.split('/')[0]
    seq_record.id=new_id
    seq_record.seq.alphabet='ProteinAlphabet'
    data=(str(seq_record.id)+'\t'+str(seq_record.seq)+'\n')
    temp.write(bytes(data,'UTF-8'))
    i+=1
temp.seek(0)
#print(temp.read().decode())
sboot = pexpect.spawn('../bin/phylip-3.695/exe/seqboot')
sboot.expect('.* file .*')
#print(sboot.before)
#print(sboot.after)
sboot.sendline(temp.name)
sboot.expect('.* Y .*')
sboot.sendline('R')
sboot.sendline(str(n_sample))
sboot.sendline('Y')
sboot.expect('.* seed .*')
#print(sboot.after)
sboot.sendline('4333')
sboot.expect('Done.')
os.rename('outfile','infile')
#print(sboot.read())
sboot.terminate()
protdist = pexpect.spawn('../bin/phylip-3.695/exe/protdist')
protdist.sendline('M')
protdist.sendline('D')
protdist.sendline(str(n_sample))
protdist.sendline('Y')
protdist.expect('Done.')
protdist.terminate()
os.remove('infile')
os.rename('outfile','infile')
neigh = pexpect.spawn('../bin/phylip-3.695/exe/neighbor')
neigh.sendline('M')
neigh.sendline(str(n_sample))
neigh.sendline('4333')
neigh.sendline('Y')
neigh.expect('Done.')
neigh.terminate()
os.remove('infile')
os.remove('outfile')
os.rename('outtree','intree')
consense = pexpect.spawn('../bin/phylip-3.695/exe/consense')
consense.sendline('Y')
consense.expect('Done.')
consense.terminate()
outtree=open('outtree','r')
tree=outtree.readlines()
#print(tree)
#print(species)
#otree=list()
for key in species:
    #print(key)
    for i in range(len(tree)):
        if(key in tree[i]):
            tree[i] = tree[i].replace(key,species[key])

for i in range(len(tree)):
        print(tree[i],end='')

os.remove('intree') 
os.remove('outfile') 
os.remove('outtree')       