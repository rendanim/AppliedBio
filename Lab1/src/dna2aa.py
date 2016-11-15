#import pdb 
import sys

dnaDictionary = {}


def loadSTable():
	dnafile = open("stddna.txt")
	for line in dnafile:
		llist = line.strip().split(',')
		l=len(llist)
		for key in llist[0:l-1]:
			dnaDictionary[key]=llist[l-1]
	#print(dnaDictionary['TAA'])

def readInput():
	dnaSeq = ""
	#fileInput = input("Write input file name here:")
	#file = open(fileInput)
	file = open("translationtest.dna")
	DNASeq = ""
	lines = file.readlines()
	last = lines[-1]
	i=0
	names=list()	
	for line in lines:
		if ">" in line:
			names.append(line.split()[0])	
			if i!=0:
				print(names[i-1])
			#print(i)
			#print (DNA:wSeq)
			translateDNA(DNASeq)
			DNASeq=""
			i+=1
		else:
			DNASeq+=line.replace('\n','')
			if line is last:	
			#	print (DNASeq)
				print(names[i-1])
				translateDNA(DNASeq)	
		
	#print(names)
def translateDNA(seq):
	protSeq = ""
	flag=0	
	i=0;
	if len(seq)>0:
		while i < len(seq)-2:
			value = mapping(seq[i:(i+3)]) 
			#pdb.set_trace()
			if value == 'STOP':
				i = i+1
				continue
			else:
				i = i+3
				protSeq += value
		print (protSeq)	

	
def mapping(codon):
	if codon.upper() in dnaDictionary:
		return dnaDictionary[codon.upper()]
	else:
		return 'X'
	

def main():
	loadSTable()
	readInput()


if __name__ == "__main__":
    main()
