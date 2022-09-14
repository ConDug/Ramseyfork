[ "$1" = "-h" -o "$1" = "--help" ] && echo "
Description:
    This script takes in an exhaust file with kochen specker candidates, and determine whether each
    of them is embeddable, if it is embeddable, then it will be outputted into a file as a Kochen
    Specker graph. We require the existance of n.exhaust in the directory.

Usage:
    ./check_embedability.sh n <s> <p> <verify>

Options:
    <n>: the order of the instance/number of vertices in the graph
    <s>: 1 to use minimal unembeddable subgraphs, 0 to not use minimal unembeddable subgraphs, default is 0
    <p>: 1 to use prop1, 0 to not to, default 0
    <verify>: 1 to verify sat result, 0 to not to, default 0
" && exit

n=$1
s=${2:-0}
p=${3:-0}
verify=${4:-0}

if [ "$verify" -ne 0 ] && [ "$verify" -ne 1 ]
then
    echo "verify must be a boolean 0 or 1"
    exit
fi

index=0

touch embeddable_$n.txt

if [ "$verify" -eq 0 ] && [ "$s" -eq 0 ] && [ "$p" -eq 0 ]
then
    while read line; do
        python3 main.py "$line" $n $index False False nonembeddable_$n.txt embeddable_$n.txt False False
    done < $n.exhaust
elif [ "$verify" -eq 1 ] && [ "$s" -eq 1 ] && [ "$p" -eq 1 ]
then
    while read line; do
        python3 main.py "$line" $n $index True False nonembeddable_$n.txt embeddable_$n.txt True True
    done < $n.exhaust
elif [ "$verify" -eq 0 ] && [ "$s" -eq 1 ] && [ "$p" -eq 1 ]
then
    while read line; do
        python3 main.py "$line" $n $index True False nonembeddable_$n.txt embeddable_$n.txt True False
    done < $n.exhaust
elif [ "$verify" -eq 0 ] && [ "$s" -eq 0 ] && [ "$p" -eq 1 ]
then
    while read line; do
        python3 main.py "$line" $n $index False False nonembeddable_$n.txt embeddable_$n.txt True False
    done < $n.exhaust
elif [ "$verify" -eq 0 ] && [ "$s" -eq 1 ] && [ "$p" -eq 0 ]
then
    while read line; do
        python3 main.py "$line" $n $index True False nonembeddable_$n.txt embeddable_$n.txt False False
    done < $n.exhaust
elif [ "$verify" -eq 1 ] && [ "$s" -eq 0 ] && [ "$p" -eq 0 ]
then
    while read line; do
        python3 main.py "$line" $n $index False False nonembeddable_$n.txt embeddable_$n.txt False True
    done < $n.exhaust
elif [ "$verify" -eq 1 ] && [ "$s" -eq 0 ] && [ "$p" -eq 1 ]
then
    while read line; do
        python3 main.py "$line" $n $index False False nonembeddable_$n.txt embeddable_$n.txt True True
    done < $n.exhaust
elif [ "$verify" -eq 1 ] && [ "$s" -eq 1 ] && [ "$p" -eq 0 ]
then
    while read line; do
        python3 main.py "$line" $n $index True False nonembeddable_$n.txt embeddable_$n.txt False True
    done < $n.exhaust
else
    echo "invalid input"
    exit 0
fi

cd ..

cp embedability/embeddable_$n.txt .
sort -u embeddable_$n.txt -o ks_solution_uniq_$n.exhaust
rm embeddable_$n.txt

