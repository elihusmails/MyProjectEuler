
if __name__ == '__main__':
    mylist = {} 
    mylist[0]="zero" 
    mylist[1]="one" 
    mylist[2]="two" 
    mylist[3]="three" 
    mylist[4]="four" 
    mylist[5]="five" 
    mylist[6]="six" 
    mylist[7]="seven" 
    mylist[8]="eight" 
    mylist[9]="nine" 
    mylist[10]="ten" 
    mylist[11]="eleven" 
    mylist[12]="twelve" 
    mylist[13]="thirteen" 
    mylist[14]="fourteen" 
    mylist[15]="fifteen" 
    mylist[16]="sixteen" 
    mylist[17]="seventeen" 
    mylist[18]="eighteen" 
    mylist[19]="nineteen" 
    mylist[20]="twenty" 
    mylist[30]="thirty" 
    mylist[40]="fourty" 
    mylist[50]="fifty" 
    mylist[60]="sixty" 
    mylist[70]="seventy" 
    mylist[80]="eighty" 
    mylist[90]="ninety" 
    mylist[100]="onehundred" 
    mylist[200]="twohundred" 
    mylist[300]="treehundred" 
    mylist[400]="fourhundred" 
    mylist[500]="fivehundred" 
    mylist[600]="sixhundred" 
    mylist[700]="sevenhundred" 
    mylist[800]="eighthundred" 
    mylist[900]="ninehundred" 
    mylist[1000]="onethousand" 
    
    # Create dict 
    for x in xrange(2,10): 
        count = 10 
        for y in xrange(1,10): 
            mylist[x*count+y] = mylist[x*count] + mylist[y] 
    
    for x in xrange(1,10): 
        count = 100; 
        for y in xrange(1,100): 
            mylist[x*count+y] = mylist[x*count] +"and"+ mylist[y] 
    
    # Count 
    count = 0 
    for x in xrange(1,1001): 
        for y in mylist[x]: 
            count = count + 1 
    
    print count 