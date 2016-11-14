n_max = 60

def readstockhom():
    filename = input('Which Sequence File?')

    fp = open(filename)

    for line in fp:
        if(line[0] != '#' and line[0] != '//' and line[0] != '\n'):
            linesplit=line.split()
            if(len(linesplit)>1):
                printName(linesplit[0])
                printsequence(linesplit[1])
            else:
                printName(linesplit[0])

def printName(name):
    if (name !='//' and len(name)>0):
        print('>'+name)

def printsequence(seq):
    olines = len(seq)//n_max
    r=len(seq) % n_max
    for i in range(olines):
        print(seq[(i*n_max):(((i+1)*n_max))])
    if(r>0):
        print(seq[olines*n_max:olines*n_max+r]) 
def main():
    readstockhom() 

if __name__ == "__main__":
    main()       