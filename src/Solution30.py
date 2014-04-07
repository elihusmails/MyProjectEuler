
if __name__ == '__main__':
    
    i = 1
    out = 0
    while i < 1000000:
        t = 0
        i +=1
        s = str(i)
        
        for n in s:
            t += int(n)**5
    
        if t == i:
            out += t
    
    print out