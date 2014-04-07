
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
            #n = n / i  
            #limit = n**0.5  
            
        i += 1  
        
    factors.sort(cmp=None, key=None, reverse=False)
    return factors
        
if __name__ == '__main__':
    
    i = 7
    x = 28
    
    while( 1 ):
        
        if( len(factor(x)) > 500 ):
            print x
            break
        
        i += 1
        x += i