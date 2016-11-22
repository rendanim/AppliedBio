#!/bin/bash
for file in ../data/*.fna; do
    echo ----Reading-----$file
    head  -n +1 $file  
    echo ---Number of charaters---
    tail -n +2 $file | wc
done;

