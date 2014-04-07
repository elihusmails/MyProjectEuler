
import itertools
import math

def worksForThree():
    size = 4
    n = size
    sum = 0
    
    while( n > 0):
        sum += size * (size-n)
        n -= 1
        
    sum += 1
    sum *= 2
    print sum


def jake1(size):
    
    sum = 1
    sum += size
    x = size - 2
    while x > 0:
        z = size - x -1
        while z > 0:
            y = size
            while y > 0:
                sum += y
                y -= 1
            z -= 1
        x -= 1
    
    return sum * 2


s = set()
def addToSet( array ):
    
    for i in array:
        s.add(i)
      
    
def mark2():
    
    two = [3,3]
    three = [1,2,3]
    four = [1,1,2,2]
    five = [1,1,1,1,2]
    six = [1,1,1,1,1,1]
    
    addToSet( itertools.permutations(two, 2) )
    addToSet( itertools.permutations(three, 3) )
    addToSet( itertools.permutations(four, 4) )
    addToSet( itertools.permutations(five, 5) )
    addToSet( itertools.permutations(six, 6) )
    
    for x in s:
        print x
    

def jake2():
    
    two =    [1,1,1,1]
    three =  [1,2,1,0]
    one =    [2,2,0,0]
    four =   [3,1,0,0]
    five =   [4,0,0,0]
    
    addToSet( itertools.permutations(one, 4) )
    addToSet( itertools.permutations(two, 4) )
    addToSet( itertools.permutations(three, 4) )
    addToSet( itertools.permutations(four, 4) )
    addToSet( itertools.permutations(five, 4) )
    
    for x in s:
        print x
    
    print len(s) * 2    

def generate():
    number = 5
    
    test = [0,1,2,3,4,5,4,1,0,0,0,0,0,0,0,0,0,0,0,0]
    addToSet( itertools.permutations(test,20))
    
    for x in s:
        print x

def f(n):
    
    total = 1
    
    for i in range(1,n+1):
        total *= i

    return total

if __name__ == '__main__':
      
#    mark2()
#    jake2()

    print (f(40)) / (f(20)*f(20))  
        
        