

def numbergood( num ):
    
    val = 0
    valOne = 0
    
    numStr = str(num)
    for i in numStr:
        val += int(i)
        
    numStrOne = str(num*137)
    for i in numStrOne:
        valOne += int(i)
       
    return val == valOne
    
   

if __name__ == '__main__':
    
    x = 0
    answers = []
    
    while( x < 10**6 ):
        if( numbergood( x )):
            answers.append((x))

        x += 9



    print "Length = %d\n" % (len(answers))