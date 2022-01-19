from helper import cross, dot, nested_cross 
from z3 import * 
import multiprocessing 
def solve(): 
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
    v3c1 = Real("v3c1")
    v3c2 = Real("v3c2")
    v3c3 = Real("v3c3")
    v3= (v3c1, v3c2, v3c3)
    s.add(v0c1== 1) 
    s.add(v0c2== 0) 
    s.add(v0c3== 0) 
    s.add(v1c1== 0) 
    s.add(v1c2== 1) 
    s.add(v1c3== 0) 
    s.add(v3c2 == 0)
    s.add(Or(Not(cross(cross(cross(cross(v3,v2),v3),v0),v2)[0] == 0), Not(cross(cross(cross(cross(v3,v2),v3),v0),v2)[1] == 0), Not(cross(cross(cross(cross(v3,v2),v3),v0),v2)[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(v3,v2),v3),v0),cross(cross(v2,cross(v0,v1)),v2))[0] == 0), Not(cross(cross(cross(cross(v3,v2),v3),v0),cross(cross(v2,cross(v0,v1)),v2))[1] == 0), Not(cross(cross(cross(cross(v3,v2),v3),v0),cross(cross(v2,cross(v0,v1)),v2))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(v3,v2),v3),v0),cross(v2,cross(v0,v1)))[0] == 0), Not(cross(cross(cross(cross(v3,v2),v3),v0),cross(v2,cross(v0,v1)))[1] == 0), Not(cross(cross(cross(cross(v3,v2),v3),v0),cross(v2,cross(v0,v1)))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(v3,v2),v3),v0),cross(v3,v2))[0] == 0), Not(cross(cross(cross(cross(v3,v2),v3),v0),cross(v3,v2))[1] == 0), Not(cross(cross(cross(cross(v3,v2),v3),v0),cross(v3,v2))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(v3,v2),v3),v0),cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)))[0] == 0), Not(cross(cross(cross(cross(v3,v2),v3),v0),cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)))[1] == 0), Not(cross(cross(cross(cross(v3,v2),v3),v0),cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(v3,v2),v3),v0),cross(v0,v1))[0] == 0), Not(cross(cross(cross(cross(v3,v2),v3),v0),cross(v0,v1))[1] == 0), Not(cross(cross(cross(cross(v3,v2),v3),v0),cross(v0,v1))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(v3,v2),v3),v0),v3)[0] == 0), Not(cross(cross(cross(cross(v3,v2),v3),v0),v3)[1] == 0), Not(cross(cross(cross(cross(v3,v2),v3),v0),v3)[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(v3,v2),v3),v0),cross(v3,v1))[0] == 0), Not(cross(cross(cross(cross(v3,v2),v3),v0),cross(v3,v1))[1] == 0), Not(cross(cross(cross(cross(v3,v2),v3),v0),cross(v3,v1))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(v3,v2),v3),v0),v1)[0] == 0), Not(cross(cross(cross(cross(v3,v2),v3),v0),v1)[1] == 0), Not(cross(cross(cross(cross(v3,v2),v3),v0),v1)[2] == 0)))
    s.add(Or(Not(cross(v2,cross(cross(v3,v2),v3))[0] == 0), Not(cross(v2,cross(cross(v3,v2),v3))[1] == 0), Not(cross(v2,cross(cross(v3,v2),v3))[2] == 0)))
    s.add(Or(Not(cross(v2,cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)))[0] == 0), Not(cross(v2,cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)))[1] == 0), Not(cross(v2,cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)))[2] == 0)))
    s.add(Or(Not(cross(v2,v0)[0] == 0), Not(cross(v2,v0)[1] == 0), Not(cross(v2,v0)[2] == 0)))
    s.add(Or(Not(cross(v2,cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)))[0] == 0), Not(cross(v2,cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)))[1] == 0), Not(cross(v2,cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)))[2] == 0)))
    s.add(Or(Not(cross(v2,cross(v0,v1))[0] == 0), Not(cross(v2,cross(v0,v1))[1] == 0), Not(cross(v2,cross(v0,v1))[2] == 0)))
    s.add(Or(Not(cross(v2,v3)[0] == 0), Not(cross(v2,v3)[1] == 0), Not(cross(v2,v3)[2] == 0)))
    s.add(Or(Not(cross(v2,cross(v3,v1))[0] == 0), Not(cross(v2,cross(v3,v1))[1] == 0), Not(cross(v2,cross(v3,v1))[2] == 0)))
    s.add(Or(Not(cross(v2,v1)[0] == 0), Not(cross(v2,v1)[1] == 0), Not(cross(v2,v1)[2] == 0)))
    s.add(Or(Not(cross(cross(cross(v2,cross(v0,v1)),v2),cross(cross(v3,v2),v3))[0] == 0), Not(cross(cross(cross(v2,cross(v0,v1)),v2),cross(cross(v3,v2),v3))[1] == 0), Not(cross(cross(cross(v2,cross(v0,v1)),v2),cross(cross(v3,v2),v3))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(v2,cross(v0,v1)),v2),cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)))[0] == 0), Not(cross(cross(cross(v2,cross(v0,v1)),v2),cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)))[1] == 0), Not(cross(cross(cross(v2,cross(v0,v1)),v2),cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(v2,cross(v0,v1)),v2),v0)[0] == 0), Not(cross(cross(cross(v2,cross(v0,v1)),v2),v0)[1] == 0), Not(cross(cross(cross(v2,cross(v0,v1)),v2),v0)[2] == 0)))
    s.add(Or(Not(cross(cross(cross(v2,cross(v0,v1)),v2),cross(v3,v2))[0] == 0), Not(cross(cross(cross(v2,cross(v0,v1)),v2),cross(v3,v2))[1] == 0), Not(cross(cross(cross(v2,cross(v0,v1)),v2),cross(v3,v2))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(v2,cross(v0,v1)),v2),cross(v0,v1))[0] == 0), Not(cross(cross(cross(v2,cross(v0,v1)),v2),cross(v0,v1))[1] == 0), Not(cross(cross(cross(v2,cross(v0,v1)),v2),cross(v0,v1))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(v2,cross(v0,v1)),v2),v3)[0] == 0), Not(cross(cross(cross(v2,cross(v0,v1)),v2),v3)[1] == 0), Not(cross(cross(cross(v2,cross(v0,v1)),v2),v3)[2] == 0)))
    s.add(Or(Not(cross(cross(cross(v2,cross(v0,v1)),v2),cross(v3,v1))[0] == 0), Not(cross(cross(cross(v2,cross(v0,v1)),v2),cross(v3,v1))[1] == 0), Not(cross(cross(cross(v2,cross(v0,v1)),v2),cross(v3,v1))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(v2,cross(v0,v1)),v2),v1)[0] == 0), Not(cross(cross(cross(v2,cross(v0,v1)),v2),v1)[1] == 0), Not(cross(cross(cross(v2,cross(v0,v1)),v2),v1)[2] == 0)))
    s.add(Or(Not(cross(cross(v2,cross(v0,v1)),cross(cross(v3,v2),v3))[0] == 0), Not(cross(cross(v2,cross(v0,v1)),cross(cross(v3,v2),v3))[1] == 0), Not(cross(cross(v2,cross(v0,v1)),cross(cross(v3,v2),v3))[2] == 0)))
    s.add(Or(Not(cross(cross(v2,cross(v0,v1)),cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)))[0] == 0), Not(cross(cross(v2,cross(v0,v1)),cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)))[1] == 0), Not(cross(cross(v2,cross(v0,v1)),cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)))[2] == 0)))
    s.add(Or(Not(cross(cross(v2,cross(v0,v1)),v0)[0] == 0), Not(cross(cross(v2,cross(v0,v1)),v0)[1] == 0), Not(cross(cross(v2,cross(v0,v1)),v0)[2] == 0)))
    s.add(Or(Not(cross(cross(v2,cross(v0,v1)),cross(v3,v2))[0] == 0), Not(cross(cross(v2,cross(v0,v1)),cross(v3,v2))[1] == 0), Not(cross(cross(v2,cross(v0,v1)),cross(v3,v2))[2] == 0)))
    s.add(Or(Not(cross(cross(v2,cross(v0,v1)),cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)))[0] == 0), Not(cross(cross(v2,cross(v0,v1)),cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)))[1] == 0), Not(cross(cross(v2,cross(v0,v1)),cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)))[2] == 0)))
    s.add(Or(Not(cross(cross(v2,cross(v0,v1)),v3)[0] == 0), Not(cross(cross(v2,cross(v0,v1)),v3)[1] == 0), Not(cross(cross(v2,cross(v0,v1)),v3)[2] == 0)))
    s.add(Or(Not(cross(cross(v2,cross(v0,v1)),cross(v3,v1))[0] == 0), Not(cross(cross(v2,cross(v0,v1)),cross(v3,v1))[1] == 0), Not(cross(cross(v2,cross(v0,v1)),cross(v3,v1))[2] == 0)))
    s.add(Or(Not(cross(cross(v2,cross(v0,v1)),v1)[0] == 0), Not(cross(cross(v2,cross(v0,v1)),v1)[1] == 0), Not(cross(cross(v2,cross(v0,v1)),v1)[2] == 0)))
    s.add(Or(Not(cross(cross(cross(v3,v2),v3),cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)))[0] == 0), Not(cross(cross(cross(v3,v2),v3),cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)))[1] == 0), Not(cross(cross(cross(v3,v2),v3),cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(v3,v2),v3),v0)[0] == 0), Not(cross(cross(cross(v3,v2),v3),v0)[1] == 0), Not(cross(cross(cross(v3,v2),v3),v0)[2] == 0)))
    s.add(Or(Not(cross(cross(cross(v3,v2),v3),cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)))[0] == 0), Not(cross(cross(cross(v3,v2),v3),cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)))[1] == 0), Not(cross(cross(cross(v3,v2),v3),cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(v3,v2),v3),cross(v0,v1))[0] == 0), Not(cross(cross(cross(v3,v2),v3),cross(v0,v1))[1] == 0), Not(cross(cross(cross(v3,v2),v3),cross(v0,v1))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(v3,v2),v3),cross(v3,v1))[0] == 0), Not(cross(cross(cross(v3,v2),v3),cross(v3,v1))[1] == 0), Not(cross(cross(cross(v3,v2),v3),cross(v3,v1))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(v3,v2),v3),v1)[0] == 0), Not(cross(cross(cross(v3,v2),v3),v1)[1] == 0), Not(cross(cross(cross(v3,v2),v3),v1)[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)),v0)[0] == 0), Not(cross(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)),v0)[1] == 0), Not(cross(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)),v0)[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)),cross(v3,v2))[0] == 0), Not(cross(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)),cross(v3,v2))[1] == 0), Not(cross(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)),cross(v3,v2))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)),cross(v0,v1))[0] == 0), Not(cross(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)),cross(v0,v1))[1] == 0), Not(cross(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)),cross(v0,v1))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)),v3)[0] == 0), Not(cross(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)),v3)[1] == 0), Not(cross(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)),v3)[2] == 0)))
    s.add(Or(Not(cross(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)),v1)[0] == 0), Not(cross(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)),v1)[1] == 0), Not(cross(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1)),v1)[2] == 0)))
    s.add(Or(Not(cross(v0,cross(v3,v2))[0] == 0), Not(cross(v0,cross(v3,v2))[1] == 0), Not(cross(v0,cross(v3,v2))[2] == 0)))
    s.add(Or(Not(cross(v0,cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)))[0] == 0), Not(cross(v0,cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)))[1] == 0), Not(cross(v0,cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)))[2] == 0)))
    s.add(Or(Not(cross(v0,v3)[0] == 0), Not(cross(v0,v3)[1] == 0), Not(cross(v0,v3)[2] == 0)))
    s.add(Or(Not(cross(v0,cross(v3,v1))[0] == 0), Not(cross(v0,cross(v3,v1))[1] == 0), Not(cross(v0,cross(v3,v1))[2] == 0)))
    s.add(Or(Not(cross(cross(v3,v2),cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)))[0] == 0), Not(cross(cross(v3,v2),cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)))[1] == 0), Not(cross(cross(v3,v2),cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)))[2] == 0)))
    s.add(Or(Not(cross(cross(v3,v2),cross(v0,v1))[0] == 0), Not(cross(cross(v3,v2),cross(v0,v1))[1] == 0), Not(cross(cross(v3,v2),cross(v0,v1))[2] == 0)))
    s.add(Or(Not(cross(cross(v3,v2),cross(v3,v1))[0] == 0), Not(cross(cross(v3,v2),cross(v3,v1))[1] == 0), Not(cross(cross(v3,v2),cross(v3,v1))[2] == 0)))
    s.add(Or(Not(cross(cross(v3,v2),v1)[0] == 0), Not(cross(cross(v3,v2),v1)[1] == 0), Not(cross(cross(v3,v2),v1)[2] == 0)))
    s.add(Or(Not(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v0,v1))[0] == 0), Not(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v0,v1))[1] == 0), Not(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v0,v1))[2] == 0)))
    s.add(Or(Not(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),v3)[0] == 0), Not(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),v3)[1] == 0), Not(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),v3)[2] == 0)))
    s.add(Or(Not(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),v1)[0] == 0), Not(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),v1)[1] == 0), Not(cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),v1)[2] == 0)))
    s.add(Or(Not(cross(cross(v0,v1),v3)[0] == 0), Not(cross(cross(v0,v1),v3)[1] == 0), Not(cross(cross(v0,v1),v3)[2] == 0)))
    s.add(Or(Not(cross(cross(v0,v1),cross(v3,v1))[0] == 0), Not(cross(cross(v0,v1),cross(v3,v1))[1] == 0), Not(cross(cross(v0,v1),cross(v3,v1))[2] == 0)))
    s.add(v3[0]*v1[0]+v3[1]*v1[1]+v3[2]*v1[2]== 0) 
    s.add(cross(cross(cross(v3,v2),v3),v0)[0]*cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1))[0]+cross(cross(cross(v3,v2),v3),v0)[1]*cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1))[1]+cross(cross(cross(v3,v2),v3),v0)[2]*cross(cross(cross(v3,v1),cross(cross(v2,cross(v0,v1)),v2)),cross(v3,v1))[2]== 0) 
    f = open("embed_result.txt", "a") 
    f.write( "  "+ str(2) + "  "  +str(s.check()))
if __name__ == '__main__':
    p = multiprocessing.Process(target=solve) 
    p.start()
    p.join(10)
    if p.is_alive(): 
        print ('running... kill it...') 
        p.terminate() 
        p.join() 
    else: 
        p.terminate() 
        p.join() 
