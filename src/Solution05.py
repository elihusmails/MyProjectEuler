
def check( lowest, step ):
    for i in range(1,step):
        if lowest % i != 0:
            return False
        
    return True

if __name__ == '__main__':
    
    # for 10, the answer is 2520
    max = 20
    answer = 1
    for i in range(1,(max)):
        answer *= i
#        print answer
        
    lowest = answer
    for i in reversed(range(1,max)):
        number = lowest / i
        if check(number, max):
            lowest = number
        
    print lowest