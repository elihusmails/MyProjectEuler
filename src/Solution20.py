
import math

if __name__ == '__main__':
        
    number = math.factorial(100)
    
    numStr = str(number)
    total = 0
    
    for i in numStr:
        total += int(i)
        
    print total