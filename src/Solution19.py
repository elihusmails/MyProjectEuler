
from datetime import * 

if __name__ == '__main__':
    
    s=0 
    for j in range(1901,2001): 
        for m in range(1,13): 
            day=date(j,m,1) 
            if day.isoweekday()==7: 
                s+=1 
            
    print s