import pdb 
import sys
import traceback

dnaDictionary = {}

# Loads the DNA codon table and converts it into a dictionary
def loadSTable():
	dnafile = open("stddna.txt")
	for line in dnafile:
		llist = line.strip().split(',')
		l=len(llist)
		for key in llist[0:l-1]:
			dnaDictionary[key]=llist[l-1]


#reads the input file and allots them to appropriate methods
def readInput():
	dnaSeq = ""
	fileInput = input("Write input file name here:")
	file = open(fileInput)
	#file = open("translationtest.dna")
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
			translateDNA(DNASeq)
			DNASeq=""
			i+=1
		else:
			DNASeq+=line.replace('\n','')
			if line is last:	
				print(names[i-1])
				translateDNA(DNASeq)	
		
# translates the DNA sequence into proteins using the DNA codon table
def translateDNA(seq):
	protSeq = ""
	flag=0	
	i=1;
	if len(seq)>0:
		for i in range(3):
			protSeq += '#'
			while i < len(seq)-2:
				value = mapping(seq[i:(i+3)]) 
				#pdb.set_trace()
				#traceback.print_stack()
				if value == 'STOP':
					i = i+3
					protSeq += '#'
					continue
				else:
					i = i+3
					protSeq += value
	printSeq(protSeq)
	
		

# finds and prints the protein sequence corresponding to the ORF
def printSeq(protSeq):
	listseq=protSeq.split('#')
	#print(listseq)
	print(max(listseq,key=len))
		

# reads the value from the dictionary for each codon	
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
