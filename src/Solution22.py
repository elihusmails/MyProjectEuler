
if __name__ == '__main__':
    
    f = open("names.txt")
    names = f.read()
    f.close()
    
    split = names.split(",")
    realNames = []
    for s in split:
        realNames.append( s[1:-1] )
        
    realNames.sort(cmp=None, key=None, reverse=False)
    
    i = 1
    total = 0
    while i <= len(realNames):
        
        sum = 0
        for x in realNames[i-1]:
            sum += ord(x) - 64
        
        total += i * sum
        i += 1
        
        
    print total