

def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    
    if n == 2: 
        return True    
    
    if not n & 1: 
        return False
    
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    
    return True


if __name__ == '__main__':
    
    count = 0
    x = 0
    
    while( 1 ):
        if( isprime(x)):
#            print x 
            count += 1
            if count == 10001:
                break;
    
        x += 1
        
    print x