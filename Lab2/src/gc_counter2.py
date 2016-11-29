__author__ = 'Bonny Wong'

import sys

gcCount = 0
gcContent = 0
sequenceLength = 0

'''
Read the content of the file.
'''
def readFile(filename):
    file = open(filename)

    for line in file:
        if '>' not in line:
            countGC(line.strip())
            # If we want to print out the name
            # else:
            #    print(line)

    calcGC()


'''
Counts the the GC nucleotides in a provided sequence
'''
def countGC(sequence):
    global gcCount
    global gcContent
    global sequenceLength
    if len(sequence) != 0:
        # print("Sequence length: " + str(sequenceLength))
        sequenceLength += len(sequence)
        gcCount += sequence.count('G')
        gcCount += sequence.count('C')


'''
Calculate the GC ratio
'''
def calcGC():
    gcContent = gcCount / float(sequenceLength)
    print("%.4f" % round(gcContent, 4))


def main():
    files = sys.argv[1:]
    for filename in files:
        readFile(filename)


if __name__ == "__main__":
    main()