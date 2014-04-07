

# find the millionth permutation of 0,1,2,3...9
import copy
 
c=0
def gen(nodes, cur):
    global c
    if not any([i >=0 for i in nodes]): 
        c+=1
        if c==1000000: print cur
 
    for i in xrange(0, len(nodes)):
        if nodes[i] >= 0: 
            cp = copy.copy(nodes)
            cp[i] = -1
            gen(cp, cur+str(i))
 
 
gen([0,1,2,3,4,5,6,7,8,9], "")