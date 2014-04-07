
import math

if __name__ == '__main__':
    
    theResults = list()
    for a in xrange(2,101):
        for b in xrange(2, 101):
            theResults.append( math.pow(a,b))
        
    noDups = dict(map(lambda i: (i,1),theResults)).keys()
    
    print len(noDups)