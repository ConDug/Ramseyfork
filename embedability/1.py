from z3 import * 
from helper import cross, dot, nested_cross 
import multiprocessing 
def test_embed(): 
    f = open("embed_result.txt", "a") 
    s = Solver() 
    v0c1 = Real("v0c1")
    v0c2 = Real("v0c2")
    v0c3 = Real("v0c3")
    v0= (v0c1, v0c2, v0c3)
    v1c1 = Real("v1c1")
    v1c2 = Real("v1c2")
    v1c3 = Real("v1c3")
    v1= (v1c1, v1c2, v1c3)
    v2c1 = Real("v2c1")
    v2c2 = Real("v2c2")
    v2c3 = Real("v2c3")
    v2= (v2c1, v2c2, v2c3)
    s.add(v0c1== 1) 
    s.add(v0c2== 0) 
    s.add(v0c3== 0) 
    s.add(v1c1== 0) 
    s.add(v1c2== 1) 
    s.add(v1c3== 0) 
    s.add(cross(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)))[0] == 0) 
    s.add(cross(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)))[1] == 0) 
    s.add(cross(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)))[2] == 0) 
    s.add(Or(Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),v0)[0] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),v0)[1] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),v0)[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),v1)[0] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),v1)[1] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),v1)[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),cross(v2,v0))[0] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),cross(v2,v0))[1] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),cross(v2,v0))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1))[0] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1))[1] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),cross(v0,v1))[0] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),cross(v0,v1))[1] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),cross(v0,v1))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),cross(cross(v2,v0),v2))[0] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),cross(cross(v2,v0),v2))[1] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),cross(cross(v2,v0),v2))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[0] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[1] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),cross(cross(cross(v2,v0),v2),cross(v0,v1)))[0] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),cross(cross(cross(v2,v0),v2),cross(v0,v1)))[1] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2),cross(cross(cross(v2,v0),v2),cross(v0,v1)))[2] == 0)))
    s.add(Or(Not(cross(v2,cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)))[0] == 0), Not(cross(v2,cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)))[1] == 0), Not(cross(v2,cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)))[2] == 0)))
    s.add(Or(Not(cross(v2,v0)[0] == 0), Not(cross(v2,v0)[1] == 0), Not(cross(v2,v0)[2] == 0)))
    s.add(Or(Not(cross(v2,v1)[0] == 0), Not(cross(v2,v1)[1] == 0), Not(cross(v2,v1)[2] == 0)))
    s.add(Or(Not(cross(v2,cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1))[0] == 0), Not(cross(v2,cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1))[1] == 0), Not(cross(v2,cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1))[2] == 0)))
    s.add(Or(Not(cross(v2,cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)))[0] == 0), Not(cross(v2,cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)))[1] == 0), Not(cross(v2,cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)))[2] == 0)))
    s.add(Or(Not(cross(v2,cross(v0,v1))[0] == 0), Not(cross(v2,cross(v0,v1))[1] == 0), Not(cross(v2,cross(v0,v1))[2] == 0)))
    s.add(Or(Not(cross(v2,cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[0] == 0), Not(cross(v2,cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[1] == 0), Not(cross(v2,cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[2] == 0)))
    s.add(Or(Not(cross(v2,cross(cross(cross(v2,v0),v2),cross(v0,v1)))[0] == 0), Not(cross(v2,cross(cross(cross(v2,v0),v2),cross(v0,v1)))[1] == 0), Not(cross(v2,cross(cross(cross(v2,v0),v2),cross(v0,v1)))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),v0)[0] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),v0)[1] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),v0)[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),v1)[0] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),v1)[1] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),v1)[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),cross(v2,v0))[0] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),cross(v2,v0))[1] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),cross(v2,v0))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)))[0] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)))[1] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),cross(v0,v1))[0] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),cross(v0,v1))[1] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),cross(v0,v1))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),cross(cross(v2,v0),v2))[0] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),cross(cross(v2,v0),v2))[1] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),cross(cross(v2,v0),v2))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),cross(cross(cross(v2,v0),v2),cross(v0,v1)))[0] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),cross(cross(cross(v2,v0),v2),cross(v0,v1)))[1] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2)),cross(cross(cross(v2,v0),v2),cross(v0,v1)))[2] == 0)))
    s.add(Or(Not(cross(v0,cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1))[0] == 0), Not(cross(v0,cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1))[1] == 0), Not(cross(v0,cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1))[2] == 0)))
    s.add(Or(Not(cross(v0,cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)))[0] == 0), Not(cross(v0,cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)))[1] == 0), Not(cross(v0,cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)))[2] == 0)))
    s.add(Or(Not(cross(v0,cross(cross(v2,v0),v2))[0] == 0), Not(cross(v0,cross(cross(v2,v0),v2))[1] == 0), Not(cross(v0,cross(cross(v2,v0),v2))[2] == 0)))
    s.add(Or(Not(cross(v0,cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[0] == 0), Not(cross(v0,cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[1] == 0), Not(cross(v0,cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[2] == 0)))
    s.add(Or(Not(cross(v0,cross(cross(cross(v2,v0),v2),cross(v0,v1)))[0] == 0), Not(cross(v0,cross(cross(cross(v2,v0),v2),cross(v0,v1)))[1] == 0), Not(cross(v0,cross(cross(cross(v2,v0),v2),cross(v0,v1)))[2] == 0)))
    s.add(Or(Not(cross(v1,cross(v2,v0))[0] == 0), Not(cross(v1,cross(v2,v0))[1] == 0), Not(cross(v1,cross(v2,v0))[2] == 0)))
    s.add(Or(Not(cross(v1,cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)))[0] == 0), Not(cross(v1,cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)))[1] == 0), Not(cross(v1,cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)))[2] == 0)))
    s.add(Or(Not(cross(v1,cross(cross(v2,v0),v2))[0] == 0), Not(cross(v1,cross(cross(v2,v0),v2))[1] == 0), Not(cross(v1,cross(cross(v2,v0),v2))[2] == 0)))
    s.add(Or(Not(cross(v1,cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[0] == 0), Not(cross(v1,cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[1] == 0), Not(cross(v1,cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[2] == 0)))
    s.add(Or(Not(cross(v1,cross(cross(cross(v2,v0),v2),cross(v0,v1)))[0] == 0), Not(cross(v1,cross(cross(cross(v2,v0),v2),cross(v0,v1)))[1] == 0), Not(cross(v1,cross(cross(cross(v2,v0),v2),cross(v0,v1)))[2] == 0)))
    s.add(Or(Not(cross(cross(v2,v0),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1))[0] == 0), Not(cross(cross(v2,v0),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1))[1] == 0), Not(cross(cross(v2,v0),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1))[2] == 0)))
    s.add(Or(Not(cross(cross(v2,v0),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)))[0] == 0), Not(cross(cross(v2,v0),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)))[1] == 0), Not(cross(cross(v2,v0),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)))[2] == 0)))
    s.add(Or(Not(cross(cross(v2,v0),cross(v0,v1))[0] == 0), Not(cross(cross(v2,v0),cross(v0,v1))[1] == 0), Not(cross(cross(v2,v0),cross(v0,v1))[2] == 0)))
    s.add(Or(Not(cross(cross(v2,v0),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[0] == 0), Not(cross(cross(v2,v0),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[1] == 0), Not(cross(cross(v2,v0),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[2] == 0)))
    s.add(Or(Not(cross(cross(v2,v0),cross(cross(cross(v2,v0),v2),cross(v0,v1)))[0] == 0), Not(cross(cross(v2,v0),cross(cross(cross(v2,v0),v2),cross(v0,v1)))[1] == 0), Not(cross(cross(v2,v0),cross(cross(cross(v2,v0),v2),cross(v0,v1)))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)))[0] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)))[1] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1),cross(v0,v1))[0] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1),cross(v0,v1))[1] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1),cross(v0,v1))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1),cross(cross(v2,v0),v2))[0] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1),cross(cross(v2,v0),v2))[1] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1),cross(cross(v2,v0),v2))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1),cross(cross(cross(v2,v0),v2),cross(v0,v1)))[0] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1),cross(cross(cross(v2,v0),v2),cross(v0,v1)))[1] == 0), Not(cross(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1),cross(cross(cross(v2,v0),v2),cross(v0,v1)))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),cross(cross(v2,v0),v2))[0] == 0), Not(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),cross(cross(v2,v0),v2))[1] == 0), Not(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),cross(cross(v2,v0),v2))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[0] == 0), Not(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[1] == 0), Not(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[2] == 0)))
    s.add(Or(Not(cross(cross(v0,v1),cross(cross(v2,v0),v2))[0] == 0), Not(cross(cross(v0,v1),cross(cross(v2,v0),v2))[1] == 0), Not(cross(cross(v0,v1),cross(cross(v2,v0),v2))[2] == 0)))
    s.add(Or(Not(cross(cross(v0,v1),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[0] == 0), Not(cross(cross(v0,v1),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[1] == 0), Not(cross(cross(v0,v1),cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)))[2] == 0)))
    s.add(cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2))[0]*cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1)[0]+cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2))[1]*cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1)[1]+cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(v0,v1)),v2))[2]*cross(cross(cross(cross(cross(v2,v0),v2),cross(v0,v1)),cross(cross(v2,v0),v2)),v1)[2]== 0) 
    dir = __file__
    dir = dir.split('\\')
    row = int(dir[-1][:-3])
    f.write('  ' + str(row) + ', ' + str(s.check())+ ' ' +str(12)+ ' ' +str(20)+'\n')
    f.close()
if __name__ == '__main__': 
    p = multiprocessing.Process(target=test_embed) 
    p.start() 
    p.join(5) 
    if p.is_alive(): 
        print (1)
        p.terminate() 
        p.join() 
    else: 
        p.terminate() 
        p.join() 
