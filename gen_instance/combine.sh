#!/bin/bash
n=$1
p=$2
q=$3
lower=${4:-0}
upper=${5:-0}
edge_b=${6:-0} #lower bound on triangles per blue edge
Edge_b=${7:-0} #upper bound on triangles per blue edge
edge_r=${8:-0} #lower bound on triangles per red edge
Edge_r=${9:-0} 
v=${10}
c=${11}

#Part of CNF file creation
#v= total num var in cnf file
#c= total num constraints in cnf file

echo "p cnf ${v} ${c}" > ./temp_head_${n}_${p}_${q}_${lower}_${upper}_${edge_b}_${Edge_b}_${edge_r}_${Edge_r} #create cnf file and header
cat ./temp_head_${n}_${p}_${q}_${lower}_${upper}_${edge_b}_${Edge_b}_${edge_r}_${Edge_r} ./constraints_temp_${n}_${p}_${q}_${lower}_${upper}_${edge_b}_${Edge_b}_${edge_r}_${Edge_r} > ./constraints_${n}_${p}_${q}_${lower}_${upper}_${edge_b}_${Edge_b}_${edge_r}_${Edge_r} #write constraints in temp_n_p_q to constraints

rm constraints_temp_${n}_${p}_${q}_${lower}_${upper}_${edge_b}_${Edge_b}_${edge_r}_${Edge_r}
rm temp_head_${n}_${p}_${q}_${lower}_${upper}_${edge_b}_${Edge_b}_${edge_r}_${Edge_r}
