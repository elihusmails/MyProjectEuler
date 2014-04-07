
if __name__ == '__main__':
    
    number = 2**1000
    numStr = str(number)
    total = 0
    
    for i in numStr:
        total += int(i)
        
    print total
    