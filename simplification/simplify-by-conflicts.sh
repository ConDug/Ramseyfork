#!/bin/bash

s=""

# Option parsing
while getopts ":s" opt; do
  case $opt in
    s) s="true" ;;
    \?) echo "Invalid option: -$OPTARG" >&2; exit 1 ;;
  esac
done

shift $((OPTIND -1))

# Ensure parameters are specified on the command-line
if [ -z "$2" ]; then
  echo "Need filename, order, and the number of conflicts for which to simplify"
  exit
fi

f=$1 # Filename
o=$2 # Order
m=$3 # Number of conflicts
e=$((o*(o-1)/2)) # Number of edge variables

# Directory to log simplification output
mkdir -p log

# Directory for simplified output
mkdir -p simp

f_dir=$f
f=$(basename "$f")

# Simplify m seconds
echo "simplifying for $m conflicts"
i=1
./cadical-ks/build/cadical-ks "$f_dir" "$f_dir.drat" --order $o -o simp/"$f".simp1 -e simp/"$f".ext1 -n -c $m | tee log/"$f".simp1

if [ "$s" != "true" ]; then
	echo "verifying the simplification now..."
	./drat-trim/drat-trim "$f_dir" "$f_dir.drat" -f | tee log/"$f".simp1.verify
	if ! grep -E "s DERIVATION|s VERIFIED" -q log/"$f".simp1.verify; then
	echo "ERROR: Proof not verified"
	fi
	rm "$f_dir.drat"
fi

str=$(less log/"$f".simp1 | grep "c conflicts:")
conf_used=$(echo $str | awk -F ' ' '{print $3; exit;}')
echo "$conf_used conflicts used for simplification"

if grep -q "UNSATISFIABLE" log/"$f".simp1; then
  conf_left=0
else
  conf_left=$(echo $m-$conf_used | bc)
fi

while [ $(echo "$conf_used < $m" | bc) -ne 0 ] && [ "$conf_left" != 0 ]; do
  conf_left=$(echo $m-$conf_used | bc)
  ./gen_cubes/concat-edge.sh $o simp/"$f".simp"$i" simp/"$f".ext"$i" | ./cadical-ks/build/cadical-ks /dev/stdin simp/"$f".simp"$i".drat --order $o -o simp/"$f".simp$((i+1)) -e simp/"$f".ext$((i+1)) -n -c $conf_left | tee log/"$f".simp$((i+1))
  if [ "$s" != "true" ]; then
	./gen_cubes/concat-edge.sh $o simp/"$f".simp"$i" simp/"$f".ext"$i" | ./drat-trim/drat-trim /dev/stdin simp/"$f".simp"$i".drat -f | tee log/"$f".simp$((i+1)).verify
	if ! grep -E "s DERIVATION|s VERIFIED" -q log/"$f".simp1.verify; then
	echo "ERROR: Proof not verified"
	fi
	rm simp/"$f".simp"$i".drat simp/"$f".simp"$i" simp/"$f".ext"$i" 2>/dev/null
  fi
  str=$(less log/"$f".simp$((i+1)) | grep "c conflicts:")
  conf_used_2=$(echo $str | awk -F ' ' '{print $3; exit;}')
  conf_used=$(echo $conf_used+$conf_used_2 | bc)
  ((i+=1))
  if grep -q "UNSATISFIABLE" log/"$f".simp$i; then
    break
  fi
done

echo "Called CaDiCaL $i times"

# Output final simplified instance
./gen_cubes/concat-edge.sh $o simp/"$f".simp"$i" simp/"$f".ext"$i" > "$f_dir".simp