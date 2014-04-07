

if __name__ == '__main__':

    
    list = [i for i in range(1000) if (i%3) == 0 or (i%5) == 0]
    print list
    answer = 0
    for l in list:
        answer += l
        
    print answer
