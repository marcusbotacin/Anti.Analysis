#!/bin/bash

for i in Testes/*/*.s; 
do
    N="$(basename $i | rev | cut -d"." -f2- | rev)"
    D="$(dirname $i)"
    O="$D/$N.o"
    B="$D/$N"
    gcc -c $i -o $O
    gcc $O -o $B
done

