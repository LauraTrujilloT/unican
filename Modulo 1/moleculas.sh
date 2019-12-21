datadir="data-shell/data/pdb"

#fname = "data/pdb/cholesterol.pdb"
mkdir -p  "$renamed_molecules"

for fname in ${datadir}/*.pdb
do

    formula=$(grep ATOM ${fname}  | awk '{print $ 3}' | sort | uniq -c |
      awk '{print $2,$1}' | tr -d '\n')
    echo ${formula}
done
