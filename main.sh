#!/bin/bash
# Ensure parameters are specified on the command-line

[ "$1" = "-h" -o "$1" = "--help" ] && echo "
Description:
    Updated on 2023-01-25
    This is a driver script that handles generating the SAT encoding, generating non-canonical subgraph blocking clauses,
    simplify instance using CaDiCaL, solve the instance using maplesat-ks, then finally determine if a KS system exists for a certain order.

Usage:
    ./main.sh [-p] [-m] n t s b r
    If only parameter n is provided, default run ./main.sh n 10000 2 2 0 10

Options:
    [-d]: cubing/solving in parallel
    <n>: the order of the instance/number of vertices in the graph
    <p>:
    <q>:
    <o>: simplification option, option c means simplifying for t conflicts, option v means simplify until t% of variables are eliminated
    <t>: conflicts for which to simplify each time CaDiCal is called
    <s>: option for simplification, takes in argument 1 (before adding noncanonical clauses), 2 (after), 3(both)
    <b>: option for noncanonical blocking clauses, takes in argument 1 (pre-generated), 2 (real-time-generation), 3 (no blocking clauses)
    <r>: number of variable to remove in cubing, if not passed in, assuming no cubing needed
    <a>: amount of additional variables to remove for each cubing call
" && exit


while getopts "pmd:D:E:F:" opt
do
    case $opt in
        p) d="-p" ;;
        m) m="-m" ;;
        d) lower=${OPTARG} ;; #lower bound on degree of blue vertices
        D) upper=${OPTARG} ;; #upper bound on degree of blue vertices
        E) Edge_b=${OPTARG} ;; #upper bound on blue triangles per blue edge
        F) Edge_r=${OPTARG} ;; #upper bound on red triangles per red edge
        *) echo "Invalid option: -$OPTARG. Only -p and -m are supported. Use -h or --help for help" >&2
           exit 1 ;;
    esac
    
done
shift $((OPTIND-1))

if [[ ! -v lower ]]; then
    lower=0
fi
if [[ ! -v upper ]]; then
    upper=0
fi

if [[ ! -v Edge_b ]]; then
    Edge_b=0
fi

if [[ ! -v Edge_r ]]; then
    Edge_r=0
fi

#step 1: input parameters
if [ -z "$1" ]
then
    echo "Need instance order (number of vertices) and number of simplification, use -h or --help for further instruction"
    exit
fi

n=$1 #order
p=$2
q=$3
t=${4:-100000} #conflicts for which to simplify each time CaDiCal is called, or % of variables to eliminate
r=${5:-0} #num of var to eliminate during first cubing stage
a=${6:-10} #amount of additional variables to remove for each cubing call


#step 2: setp up dependencies
dir="${n}_${p}_${q}_${lower}_${upper}_${Edge_b}_${Edge_r}_${t}_${r}_${a}"
./dependency-setup.sh
 
#step 3 and 4: generate pre-processed instance
dir="."

if [ -f constraints_${n}_${p}_${q}_${lower}_${upper}_${Edge_b}_${Edge_r}_${t}_${r}_${a}.simp.log ]
then
    echo "Instance with these parameters has already been solved."
    exit 0
fi

module load python/3.10
if [ -f constraints_${n}_${p}_${q}_${lower}_${upper}_${Edge_b}_${Edge_r} ]
then
    echo "instance already generated"
    cp constraints_${n}_${p}_${q}_${lower}_${upper}_${Edge_b}_${Edge_r} constraints_${n}_${p}_${q}_${lower}_${upper}_${Edge_b}_${Edge_r}_${t}_${r}_${a}
else
    #echo $n $p $q $lower $upper $Edge_b $Edge_r
    python3 gen_instance/generate.py $n $p $q $lower $upper $Edge_b $Edge_r #generate the instance of order n for p,q
    cp constraints_${n}_${p}_${q}_${lower}_${upper}_${Edge_b}_${Edge_r} constraints_${n}_${p}_${q}_${lower}_${upper}_${Edge_b}_${Edge_r}_${t}_${r}_${a}
fi

echo "Simplifying constraints_${n}_${p}_${q}_${lower}_${upper}_${Edge_b}_${Edge_r}_${t}_${r}_${a} for" $t "conflicts using CaDiCaL+CAS"
./simplification/simplify-by-conflicts.sh constraints_${n}_${p}_${q}_${lower}_${upper}_${Edge_b}_${Edge_r}_${t}_${r}_${a} $n $t

#need to fix the cubing part for directory pointer
#step 5: cube and conquer if necessary, then solve
if [ "$r" != "0" ]
then
    dir="${n}_${p}_${q}_${lower}_${upper}_${Edge_b}_${Edge_r}_${t}_${r}_${a}"
    echo "Starting cubing" dir
    ./cube-solve.sh $p $n constraints_${n}_${p}_${q}_${lower}_${upper}_${Edge_b}_${Edge_r}_${t}_${r}_${a}.simp $dir $r $a
    
else
echo "Solving constraints_${n}_${p}_${q}_${lower}_${upper}.simp using MapleSAT+CAS"
    ./maplesat-solve-verify.sh $n constraints_${n}_${p}_${q}_${lower}_${upper}_${Edge_b}_${Edge_r}_${t}_${r}_${a}.simp
    #step 5.5: verify all constraints are satisfied
    #./verify.sh $n

    #step 6: 
    echo "checking max clique size..."
    ./4-check-clique-size.sh $n $p $q

fi

#summary.sh?
