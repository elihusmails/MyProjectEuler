

def oddNum(n):
    return 3 * n + 1

def evenNum(n):
    return n // 2

if __name__ == '__main__':
    
    maxLen = 0
    maxNum = 0
    
    for i in range(1,1000000):
        
        list = []
        x = i
        while( x != 1 ):
            list.append(x)
            if( x % 2 == 0 ):
                x = evenNum(x)
            else:
                x = oddNum(x)
        
        list.append(1)
        #print "Length of %d is %d" % (i, len(list))
        #print list
        
        if len(list) > maxLen:
            #print "Updating length of %d to %d" % (i, len(list))
            maxLen = len(list)
            maxNum = i
            
    print "Max number = %d (length = %d)" % (maxNum, maxLen)
                