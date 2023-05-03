#!/usr/bin/python
from io import StringIO
from networkx.algorithms import isomorphism
import os
import csv
import networkx as nx
import collections
import itertools
from collections import Counter
from collections import defaultdict

from networkx.algorithms.isomorphism.isomorph import is_isomorphic
from networkx.generators.classic import cycle_graph
from helper import cross, dot, nested_cross
from verify_sat import verify_sat

import sys, getopt

"""
find_assignments take in a graph and find all possible interpretations of its orthogonal relations.
determine_embed takes in one of the interpretation and convert it into a system of nonlinear equations that's readable by SMT solver Z3
"""

import os

# get the current working directory
current_dir = os.getcwd()



def g6_to_dict(g6):
    """ Input a g6 string, output a dictionary representing a graph that can be inputted in find_assignments"""
    graph_dict = {}
    G = nx.from_graph6_bytes(bytes(g6, encoding='ascii'))
    for v in list(G.nodes()):
        graph_dict[v] = (list(G.neighbors(v)))
    return graph_dict

def find_assignments(g):
    # Create list of edges
    edges_without_duplicates = set()
    edges = set()
    for v in g:
        for w in g[v]:
            if (w, v) not in edges:
                edges_without_duplicates.add((v, w))
            edges.add((v,w))
    # Fill stack with choices of initial edge
    frame = collections.namedtuple('frame',
                                ('first_edge',
                                 'to_visit',
                                 'nvar',
                                 'ortho',
                                 'var',
                                 'assign',
                                 'easily_embeddable',
                                 'iterative_assignment',
                                 'base',
                                 'touched_by',
                                 'edges_used'))
    batch = list()
    for first_edge in edges_without_duplicates:
        f = frame(
                first_edge=first_edge,
                to_visit=set(first_edge),
                nvar=0,
                ortho=[],
                var=[first_edge[0], first_edge[1]],
                assign={first_edge[0]: 0,
                        first_edge[1]: 1},
                easily_embeddable=True,
                iterative_assignment=True,
                base=set(first_edge),
                touched_by={first_edge[0]: first_edge[1],
                            first_edge[1]: first_edge[0]},
                edges_used=set([first_edge, (first_edge[1], first_edge[0])]))
        for z in (frozenset(g[first_edge[0]]) &
                  frozenset(g[first_edge[1]])):
            f.base.add(z)
            f.assign[z] = (0, 1)
            f.edges_used.add((first_edge[0], z))
            f.edges_used.add((first_edge[1], z))
            f.edges_used.add((z, first_edge[0]))
            f.edges_used.add((z, first_edge[1]))
            f.to_visit.add(z)
            f.touched_by[z] = first_edge[0]
        batch.append(f)
    completed = []
    while batch:
        new_batch = []
        for f in batch:
            # First, deduce all assignments
            while f.to_visit:
                v = f.to_visit.pop()
                for w in g[v]:
                    # Skip the edge, if it is already used
                    if (v, w) in f.edges_used:
                        continue
                    if w not in f.touched_by:
                        # If the node has not been touched before, touch it
                        # and continue
                        if w not in f.assign:
                            f.touched_by[w] = v
                            continue
                        # It is a variable.  Record the orthogonality
                        f.edges_used.add((v, w))
                        f.edges_used.add((w, v))
                        f.ortho.append((f.assign[v], f.assign[w]))
                        continue
                    # The node has been touched before.  We now can derive a
                    # cross-product expression for this node.  Two cases:
                    #  (i) the node has already been assigned a value: we can
                    #      derive a new equation; or (ii) the node has not been
                    #      assigned a value: we will assign one.  In both cases:
                    v2 = f.touched_by[w]
                    assert v != v2
                    f.edges_used.add((v, w))
                    f.edges_used.add((w, v))
                    # (i) the node has been assigned a value; derive an equation
                    if w in f.assign:
                        f = f._replace(easily_embeddable=False)
                        f.ortho.append((f.assign[w], f.assign[v]))
                        continue
                    # (ii) the node has not been assigned a value --- assign it
                    f.edges_used.add((v2, w))
                    f.edges_used.add((w, v2))
                    f.assign[w] = (v, v2)
                    f.to_visit.add(w)
            # Check whether finished
            if len(f.assign) == len(g):
                for v1, v2 in edges_without_duplicates - f.edges_used:
                    f.ortho.append((f.assign[v1], f.assign[v2]))
                    f = f._replace(easily_embeddable=False)
                """if f.easily_embeddable:
                    print ("easily embeddable")
                    num_vertices = len(g)
                    num_edges = int(len(edges)/2)
                    file = open("embed_result.txt", "a")
                    file.write('  ' + str(label) + ', ' + 'sat' + ' ' + str(num_vertices) + ' ' + str(num_edges) )
                    break"""
                completed.append(f)
                continue
            # If not: consider every possible node for the new variable
            for v in g:
                if v in f.assign:
                    continue
                new_var = len(f.var)
                f2 = frame(
                        first_edge=f.first_edge,
                        to_visit=set([v]),
                        nvar=f.nvar+3,
                        ortho=list(f.ortho),
                        var=f.var + [v],
                        assign=dict(f.assign),
                        easily_embeddable=f.easily_embeddable,
                        iterative_assignment=f.iterative_assignment,
                        base=f.base,
                        touched_by=dict(f.touched_by),
                        edges_used=set(f.edges_used))
                f2.assign[v] = new_var
                for b in f2.base:
                    if v in g[b]:
                        f2 = f2._replace(nvar=f2.nvar - 1)
                        break
                iterative_step = False
                for w in g[v]:
                    if w in f.assign:
                        f2.ortho.append((f2.assign[v], f2.assign[w]))
                        f2.edges_used.add((v, w))
                        f2.edges_used.add((w, v))
                        iterative_step = True
                if not iterative_step:
                    f2 = f2._replace(easily_embeddable=False,
                                     iterative_assignment=False)
                new_batch.append(f2)
        batch = new_batch
    # Find best assignment: we want the least number of variables;
    # then the least number of cross-product equations and finally
    # the least number of orthogonallity requirements.
    completed.sort(key=lambda f: (f.nvar, len(f.ortho)))
    return completed

def determine_embed(g, assignment, g_sat, order, index, using_subgraph, normalize, output_unsat_f, output_sat_f, prop1, verify):
    """
    g: dictonary of vertices and their adjacent vertices
    assignment: an assignment generated from find_assignments
    g_sat: graph in the format of the output from MapleSAT
    order: order of the graph to solve
    index: which orthogonality assignment to start solving from, usually we set this to 0 and use the first assignment
    using_subgraph: option to use minimal unembeddable subgraph with less than 13 vertices
    normalize: option to restrict every vector on the unit sphere
    output_unsat_f: file name to log nonembeddable graphs
    output_sat_f: file name to log embeddable graphs
    prop1: option to use proposition 1 in the paper that excludes graph with a vertex of degree less than 2
    verify: option to verify embeddable graph's vector solutions, will log vector solutions and verification results to output_sat_f
    """
    #print (assignment)
    #print (g)
    io = StringIO()
    io.write('from helper import cross \n')
    io.write('from z3 import * \n')
    io.write("s = Solver()\n")
    v_dict = {}
    for i in range(len(assignment.var)):
        v_dict[i] = ('v'+str(i)+'c1', 'v'+str(i)+'c2', 'v'+str(i)+'c3') #{0: (v0c1, v0c2, v0c3)}
    for i in range(len(assignment.var)):
        #first define the base vectors
        io.write( 'v'+str(i)+'c1 = Real("v'+ str(i) + 'c1")\n')
        io.write( 'v'+str(i)+'c2 = Real("v'+ str(i) + 'c2")\n')
        io.write( 'v'+str(i)+'c3 = Real("v'+ str(i) + 'c3")\n')
        io.write( 'v' + str(i) + '= (' + 'v' + str(i) + 'c1, v' + str(i) + 'c2, v' + str(i) + 'c3)\n')
        io.write('s.add(' + 'v' + str(i) + 'c3 >= 0)\n')
    #no need to define the rest of the vectors
    for i in assignment.assign:
        #now define every vertex
        io.write( 'ver'+str(i)+'c1 = Real("ver'+ str(i) + 'c1")\n')
        io.write( 'ver'+str(i)+'c2 = Real("ver'+ str(i) + 'c2")\n')
        io.write( 'ver'+str(i)+'c3 = Real("ver'+ str(i) + 'c3")\n')
        str_format = "ver{0} = (ver{0}c1, ver{0}c2, ver{0}c3)\n"
        io.write(str_format.format(str(i)))
        io.write('s.add(' + 'ver' + str(i) + 'c3 >= 0)\n')
        #io.write('s.add(' + dot('ver' + str(i), 'ver' + str(i)) + '== 1) \n')
    for i in assignment.assign:
        #s.add() its corresponding vector as a condition
        if isinstance(assignment.assign[i], int):
            io.write('s.add('+'ver'+str(i)+'[0]=='+'v'+str(assignment.assign[i])+'[0]) \n')
            io.write('s.add('+'ver'+str(i)+'[1]=='+'v'+str(assignment.assign[i])+'[1]) \n')
            io.write('s.add('+'ver'+str(i)+'[2]=='+'v'+str(assignment.assign[i])+'[2]) \n')
            if normalize == "True":
                io.write('s.add(' + dot('ver' + str(i), 'ver' + str(i)) + '== 1) \n')
        else:
            str_format = "s.add(Or(And(ver{2}[0]==cross({0},{1})[0], ver{2}[1]==cross({0},{1})[1], ver{2}[2]==cross({0},{1})[2]), And(ver{2}[0]==cross({1},{0})[0], ver{2}[1]==cross({1},{0})[1], ver{2}[2]==cross({1},{0})[2])))\n"
            if i in assignment.base:
                io.write(str_format.format("v" + str(assignment.assign[i][0]), "v" + str(assignment.assign[i][1]), str(i)))
            else:
                io.write(str_format.format("ver" + str(assignment.assign[i][0]), "ver" + str(assignment.assign[i][1]), str(i)))
    io.write('s.add('+v_dict[0][0] +' == 1) \n')
    io.write('s.add('+v_dict[0][1] +' == 0) \n')
    io.write('s.add('+v_dict[0][2] +' == 0) \n')
    io.write('s.add('+v_dict[1][0] +' == 0) \n')
    io.write('s.add('+v_dict[1][1] +' == 1) \n')
    io.write('s.add('+v_dict[1][2] +' == 0) \n')
    edges = set()
    for v in g:
        for w in g[v]:
            edges.add((v,w))
    had = set()
    for v1 in g:
        for v2 in g:
            if v1 == v2:
                continue
            if (v1, v2) in edges:
                continue
            if (v2, v1) in had:
                continue
            had.add((v1, v2))
            cross_product = "cross(" + "ver" + str(v1) + "," + "ver" + str(v2) + ")"
            str_format = "s.add(Or(Not({0}[0]==0), Not({0}[1]==0), Not({0}[2]==0))) \n"
            io.write(str_format.format(cross_product))
    #revert assign dict
    assign_inv = defaultdict(list)
    for k, v in assignment.assign.items():
        assign_inv[v].append(k)
    for dot_relation in assignment.ortho:
        if len(assign_inv[dot_relation[0]]) > 1:
            for v_base in assign_inv[dot_relation[0]]:
                if v_base in assignment.base:
                    v = "ver" + str(v_base)
        else:
            v = "ver" + str(assign_inv[dot_relation[0]][0])
        if len(assign_inv[dot_relation[1]]) > 1:
            for w_base in assign_inv[dot_relation[1]]:
                if w_base in assignment.base:
                    w = "ver" + str(w_base)
        else:
            w = "ver" + str(assign_inv[dot_relation[1]][0])
        io.write('s.add(' + dot(v,w) + '== 0) \n')
    io.write('s.set("timeout", 10000) \n')
    io.write('result = s.check() \n')
    io.write('if result == unknown: \n')
    io.write('    index = int(index) + 1 \n')
    io.write('    main(g_sat, order, index, using_subgraph, normalize, output_unsat_f, output_sat_f, prop1, verify) \n')
    io.write('if result == unsat: \n')
    io.write('    with open(output_unsat_f, "a+") as f: \n')
    io.write('        f.write(g_sat + "\\n") \n')
    io.write('if result == sat: \n')
    io.write('    with open(output_sat_f, "a+") as f: \n')
    io.write('        f.write(g_sat + "\\n") \n')
    if verify == "True":
        io.write('    m = s.model() \n')
        io.write('    with open("solution.log", "w+") as f2: \n')
        for i in g:
            io.write("        f2.write( " + " '" + str(i) + "' + '\\n' ) " + "\n")
            io.write('        f2.write(str(m.evaluate(ver' + str(i) + '[0]).as_decimal(100)).replace("?","")+' + '"\\n" )' + '\n')
            io.write('        f2.write(str(m.evaluate(ver' + str(i) + '[1]).as_decimal(100)).replace("?","")+' + '"\\n" )' + '\n')
            io.write('        f2.write(str(m.evaluate(ver' + str(i) + '[2]).as_decimal(100)).replace("?","")+' + '"\\n" )' + '\n')
        exec (io.getvalue())
        io.close()
        if not verify_sat(g, "solution.log"):
            print ("verification failed")
    else:
        exec (io.getvalue())
        io.close()

#graph in sat labeling format

def maple_to_edges(input, v):
    str_lst = input.split()[1:-1]
    edge_lst = []
    for j in range(0, v):
        for i in range(0, j):
            edge_lst.append((i,j))
    actual_edges = []
    for i in str_lst:
        indicator = int(i)
        if indicator > 0:
            actual_edges.append(edge_lst[int(i)-1])
    return actual_edges

def main(g, order, index, using_subgraph, normalize, output_unsat_f, output_sat_f, prop1, verify):
    """takes in graph in maplesat output format, order of the graph, count corresponds to the line
       number of the candidates, and index indicates which vector assignment we will be using. """
    """print ("original graph: " + str(g))
    print ("order of the graph: " + str(order))
    print ("using_subgraph: " + str(using_subgraph))
    print ("normalize: " + str(normalize))
    print ("using proposition 1: " + str(prop1))
    print ("verifying result: " + str(verify))"""
    order = int(order)
    edge_lst = maple_to_edges(g, int(order))
    G = nx.Graph()
    G.add_edges_from(edge_lst)
    degree_sequence = [d for n, d in G.degree()]
    if prop1 == "True":
        #graph is either empty, or has a vertex of degree 1 or 0. 
        if (1 in degree_sequence) or (0 in degree_sequence):
            return
    else:
        if nx.is_empty(G):
            return
    if using_subgraph == "True":
        #print ("Checking minimum nonembeddable subgraph")
        file_path = os.path.join(current_dir, "embedability/min_nonembed_graph_10-12.txt")
        my_file = open(file_path, "r")
        content = my_file.read()
        min_non_subgraphs = content.split("\n")
        my_file.close()
        for string in min_non_subgraphs:
            min_g = nx.from_graph6_bytes(bytes(string, encoding='utf-8'))
            gm = isomorphism.GraphMatcher(G, min_g)
            if gm.subgraph_is_monomorphic():
                with open(output_unsat_f, "a+") as f:
                    f.write(g + "\n")
                    return
        #check if G contains a minimum nonembedabble subgraph
        print ("this graph does not contain known minimal nonembeddable subgraph")
        graph_dict = {}
        for v in list(G.nodes()):
            graph_dict[v] = (list(G.neighbors(v)))
        assignments = find_assignments(graph_dict)
        assignment = assignments[int(index)]
        determine_embed(graph_dict, assignment, g, order, index, using_subgraph, normalize, output_unsat_f, output_sat_f, prop1, verify) #write the file
    else:
        graph_dict = {}
        for v in list(G.nodes()):
            graph_dict[v] = (list(G.neighbors(v)))
        assignments = find_assignments(graph_dict)
        assignment = assignments[int(index)]
        determine_embed(graph_dict, assignment, g, order, index, using_subgraph, normalize, output_unsat_f, output_sat_f, prop1, verify) #write the file

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9])
