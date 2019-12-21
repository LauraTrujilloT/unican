#!/bin/bash
datadir="data-shell/data/pdb"

# -d is an operator to test whether or not the given directory exists
NEW_DIR="renamed_molecules"
[[ -d $NEW_DIR ]] && echo $NEW_DIR already exists!, EXIT && exit
mkdir $NEW_DIR

for fname in ${datadir}/*.pdb
do

    formula=$(grep ATOM ${fname}  | awk '{print $3}' | sort | uniq -c |
      awk '{print $2,$1}' | tr -d '\n')
    new_file="$(basename "${fname//".pdb"/_${formula// /}}.pdb")"
    #echo ${new_file}
    cp $fname "$NEW_DIR/${new_file}"
    #echo ${fname}
done

trace="data-shell/"
rm -rf $trace data-shell.zip
