
def factor(n):  
    
    factors = []
    factors.append(1)
    factors.append(n)
    
    i = 2  
    limit = n**0.5
    while i <= limit:  
        if n % i == 0:  
            factors.append(i)  
            factors.append(n/i)
            
        i += 1  
        
    factors.sort(cmp=None, key=None, reverse=False)
    return factors


if __name__ == '__main__':
    
    total = 0
    
    for i in range(2, 10000):
        
        factors = factor( i )
        factors.remove(i)
        theSum = sum(factors)
        
        facs = factor(theSum)
        facs.remove(theSum)
        newSum = sum(facs)
        
        if i == newSum and i != theSum:
            total += i
        
    print total