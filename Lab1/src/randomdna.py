import random

dna = ["A","G","C","T"]
length=input("Length:")
l=int(length)
random_sequence=''

print(">myrandomsequence")
 
for i in range(0,l):
    random_sequence+=random.choice(dna)

print(random_sequence)
