

def fib():
    a, b = 0, 1
    i = 0
    
    while(1):
        a, b = b, a + b
        if( len(str(a)) == 1000 ):
            print a
            print i
            break

        i += 1

    return a

if __name__ == '__main__':
    
    fib()