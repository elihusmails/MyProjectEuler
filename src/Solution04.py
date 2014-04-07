

def isPalindrome(phrase):

    phrase_letters = [c for c in phrase]
    return (phrase_letters == phrase_letters[::-1])

def ispalindrome(num):

    numStr = str(num)
    return isPalindrome(numStr)
  

if __name__ == '__main__':
    
    answers = []
    for i in reversed(range(100, 999)):
        for x in reversed(range(i, 1000)):
            if ispalindrome( i * x ):
                answers.append( i * x)
    
    answers.sort(cmp=None, key=None, reverse=False)
    answers.reverse()
    
    print "Largest palindrome = %d" % (answers[0])
        