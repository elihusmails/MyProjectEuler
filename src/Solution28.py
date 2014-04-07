
def squaressum(x): 
    i = 1 
    z = 0 
    while z < x-1: 
        z = z + 2 
        i = i + 4 * (z * z+.5 * z+1)

    return i 

if __name__ == '__main__':
    
    print squaressum(1001) 