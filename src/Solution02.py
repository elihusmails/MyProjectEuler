
def fib2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)

def fib1(n):
    result = []
    a,b = 0, 1
    while a < n and a < 4000000:
        result.append(a)
        a,b = b, a+b
        
    return result

if __name__ == '__main__':
    
    answer = 0
    array = fib1(4000000)
    for i in array:
        if i % 2 == 0:
            answer += i
            
    print answer
        
        
        
    
    