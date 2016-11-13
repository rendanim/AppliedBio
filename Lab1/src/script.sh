#!/bin/bash
echo "-------------Running WordCount------------" > ../results/results.txt
tail -n +2 ../data/gpcr.tab |wc -l >> ../results/results.txt
echo "---------Using Grep for Human counts------" >> ../results/results.txt
grep -c "HUMAN" ../data/gpcr.tab >> ../results/results.txt
echo "--------Homo sapiens----------------------" >> ../results/results.txt
grep -c "Homo sapiens" ../data/gpcr.tab  >> ../results/results.txt
echo "-----Finding the Minimum Length-----------" >> ../results/results.txt
tail -n +2 ../data/gpcr.tab | cut -f 7 | sort -g|head -n +1 >> ../results/results.txt
echo "------Finding the Maximum Length----------" >> ../results/results.txt
cut -f 7  ../data/gpcr.tab | sort -g -r | head -1 >> ../results/results.txt
echo "-------Unique Species---------------------" >> ../results/results.txt
tail -n +2 ../data/gpcr.tab | cut -f 6 |sort | uniq | wc -l >> ../results/results.txt
echo "-------------DNA-Alignment------------------">>../results/results.txt
echo "------------instaling-----------------------">>../results/results.txt
chmod +x ../bin/muscle
echo "------------Aligning------------------------">>../results/results.txt
for file in ../data/testatin/*;do
     size=${#file}
     l=$(($size-20))
     ofile=${file:17:l}
     echo $ofile >>../results/results.txt
    ../bin/muscle -in $file -out ../results/$ofile.afa
done
