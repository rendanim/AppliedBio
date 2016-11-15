#!/bin/bash
echo "-------------Running WordCount------------"
tail -n +1 ../data/gpcr.tab |wc -l
#tail - n location in terms of number of lines '+' from begining
#wc -l return only number of lines

echo "---------Using Grep for Human counts------"
grep -c "HUMAN" ../data/gpcr.tab
#grep -c print the number of lines 
echo "-----Finding the Minimum Length-----------"
tail -n +2 ../data/gpcr.tab | cut -f 7 | sort -g|head -n +1
#cut f  - specifies the field f
#sort g - specifies numeric sort -r reverse
echo "------Finding the Maximum Length----------"
cut -f 7  ../data/gpcr.tab | sort -g -r | head -n 1  
echo "-------Unique Species---------------------" 
tail -n +2 ../data/gpcr.tab | cut -f 6 |sort | uniq | wc -l
echo "-------------DNA-Alignment------------------"
echo "------------Changing Permisions-----------------------"
chmod +x ../bin/muscle
echo "------------Aligning------------------------"
for file in ../data/testatin/*;do
     size=${#file} 
     l=$(($size-20))
     ofile=${file:17:l}
     echo $ofile proccesed
    ../bin/muscle -in $file -out ../results/$ofile.afa
done
