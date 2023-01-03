import itertools

def conway(n, edge_dict, tri_dict, v, t, cnf):
    #vertex v is connected to at least t triangles
    vertices_lst = list(range(1, n+1))
    all_tri = list(itertools.combinations(vertices_lst, 3))
    v_tri_lst = [tri for tri in all_tri if v in tri]
    tr_sublst = itertools.combinations(v_tri_lst, int(len(v_tri_lst)-t))
    for comb in tr_sublst:
        clause = []
        for tri in comb:
            clause.append(tri_dict[tri])
        cnf.append(clause)
    return cnf