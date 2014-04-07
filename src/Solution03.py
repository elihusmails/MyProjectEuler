
def isprime1(number):  
    if number<=1 or number%2==0:  
        return 0  
    check=3  
    maxneeded=number  
    while check<maxneeded+1:  
        maxneeded=number/check  
        if number%check==0:  
            return 0  
        check+=2  
    return 1 

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    
    # 0 and 1 are not primes
    if n < 2:
        return False
    
    # 2 is the only even prime number
    if n == 2: 
        return True    
    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    
    return True

def factor(n):  
    yield 1  
    i = 2  
    limit = n**0.5  
    while i <= limit:  
        if n % i == 0:  
            yield i  
            n = n / i  
            limit = n**0.5  
        else:  
            i += 1  

    if n > 1:  
        yield n  



if __name__ == '__main__':

    number = 600851475143
    
    primes = [i for i in factor(number)]
    print "Number of primes = %d" % (len(primes))
    print "Factors for %s : %s" %(number, primes )
    
    primes.reverse()
    
    for x in primes:       
        if isprime1(x):
            print x
            break


