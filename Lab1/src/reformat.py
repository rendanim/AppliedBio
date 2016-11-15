n_max = 60

def readstockhom():
    filename = input('Which Sequence File?')

    fp = open(filename)

    for line in fp:
        #check for comments and end of file 
        if(line[0] != '#' and line[0] != '//' and line[0] != '\n'):
            linesplit=line.split()
            if(len(linesplit)>1):
                #not just name
                printName(linesplit[0])
                #print the sequence
                printsequence(linesplit[1])
            else:
                printName(linesplit[0])

def printName(name):
    if (name !='//' and len(name)>0):
        print('>'+name)
    else:
        print("Corner Case")    

def printsequence(seq):
    #find number of full lines
    olines = len(seq)//n_max
    #find remaining lines
    r=len(seq) % n_max
    for i in range(olines):
        print(seq[(i*n_max):(((i+1)*n_max))])
    if(r>0):
        print(seq[olines*n_max:olines*n_max+r]) 
def main():
    readstockhom() 

if __name__ == "__main__":
    main()       