
def isPyth( a, b, c ):

    return (a**2 + b**2) == c**2

def isThousand( a, b, c ):
    
    return a + b + c == 1000

if __name__ == '__main__':
    
    for a in range(1,1000):
        for b in range(a,1000):
            for c in range(b,1000):
                
                if isPyth(a,b,c) and isThousand(a,b,c):
                    print "%d, %d, %d" % (a,b,c)
                    print a*b*c
    