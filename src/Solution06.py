
def sumsquares(n):
    retval = 0
    for i in range(1,n):
        retval = retval + (i**2)

    return retval


def squaresums(n):
    retval = 0
    for i in range(1,n):
        retval +=i

    return retval * retval

if __name__ == '__main__':
    
    num = 100
    
    sqsum = squaresums(num+1)
    sumsq = sumsquares(num+1)
    
    print "SqSum = %d, SumSq = %d.  Answer = %d" % (sqsum, sumsq, sqsum - sumsq)