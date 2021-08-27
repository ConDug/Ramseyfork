from generate import generate_encoding
from pysat.solvers import *
from pysat.formula import CNF
from relabel import *
from testing import *

def solve(file, assumption, count):
    cnf = CNF()
    cnf.from_file(file)
    s = Cadical()
    s.append_formula(cnf.clauses)
    solving = s.solve(assumptions = assumption)
    if solving == False:
        print (count)
        print (False)
    else:
        #print (True)
        if count % 100 == 0:
            print (count)
        #solution = s.get_model()
        #n=19
        #print(solution[: int(n*(n-1))])
        #print(produce_matrix(solution[int(n*(n-1)/2) : int(n*(n-1))], 19))
        

file1 = open('19-unique-sols.txt', 'r')
Lines = file1.readlines()
count = 1
file = 'orderly_cubic_19'
for solution in Lines:
    if count > 57300: #
    	assumption = preprocess_maplesat(solution)
    	assumption = relabel_from_matching(assumption, matching(19))
    	assumption = sorted(assumption, key=abs)
    	#print (assumption)
    	#print (produce_matrix(assumption, 19))
    	solve(file, assumption, count)
    count += 1