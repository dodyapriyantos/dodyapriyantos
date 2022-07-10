#import string
#alpha = string.ascii_uppercase
vowels = 'AEIOU'
consonants = 'BCDFGHJKLMNPQRSTVWXYZ'

def minion_game(string):
    # your code goes here
    global vowels
    global consonants
    
    #1st attempt
    #scoreStuart = count_stuart(string)
    #scoreKevin = count_kevin(string)
    
    #2nd attempt
    #scoreKevin, scoreStuart = count_stuart_kevin(string)
    
    #3rd attempt
    scoreKevin, scoreStuart = count_smartly_stuart_Kevin(string)
    
    if   (scoreStuart > scoreKevin) : print ('Stuart ' + str(scoreStuart))
    elif (scoreKevin > scoreStuart) : print ('Kevin '  + str(scoreKevin))
    elif (scoreKevin == scoreStuart) : print ('Draw')

#3rd attempt, after look on more detail on how the possibilities of words are drawn.
def count_smartly_stuart_Kevin(string):
    global vowels
    
    counter_consonents = 0
    counter_vowels = 0
    
    #if found a string with vowels as starting, the combinations is count by
    #the len of the string minus the position of the words
    for i in range(len(string)):
        if vowels.find(string[i]) != -1:
            counter_vowels+= len(string)-i
        else:
            counter_consonents+=len(string)-i
    #print (counter_consonents)
    #print (counter_vowels)            
    return(counter_vowels, counter_consonents)

#2nd attempt using brute force by registering all possibilities to a string and use count API
# count API is not reliable as it is missing 1 case for Kevin on "ANA" case
def count_stuart_kevin(string):
    global vowels
    global consonants

    counter_vowels = 0
    counter_consonents = 0
    result_vowels = ','
    result_consonents = ','
    
    for i in range (0, len(string)+1):
        for j in range (0, len(string)+1):
            temp = string[i:j]
            if (temp != ''):
                if (consonants.find(temp[0]) != -1) and (result_consonents.find(','+temp+',')==-1):
                    result_consonents+=temp+','
                    counter_consonents+=string.count(temp)
                if (vowels.find(temp[0]) != -1) and (result_vowels.find(','+temp+',')==-1):
                    result_vowels+=temp+','
                    counter_vowels+=string.count(temp)
    #print (result_consonents)
    #print (counter_consonents)
    #print (result_vowels)
    #print (counter_vowels)
    return (counter_vowels, counter_consonents)
    
#1st attempt using brute force by registering all possibilities to a list
def count_stuart(string):
    #start as consonants
    global consonants
    
    counter = 0
    result = []
    for i in range (0, len(string)+1):
        for j in range (0, len(string)+1):
            temp = string[i:j]
            if (temp != ''):
                if (consonants.find(temp[0]) != -1) and not(temp in result):
                    result.append(temp)
                    found = string.find(temp, 0)
                    if (found >= 0) : counter +=1
                    z=found+1
                    while (found>=0):
                        found = string.find(temp, z)
                        if found>=0: counter+=1;z=found+1
    return (counter)

#1st attempt using brute force by registering all possibilities to a list
def count_kevin(string):
    #start as vowels
    global vowels
    
    counter = 0
    result = []
    for i in range (0, len(string)+1):
        for j in range (0, len(string)+1):
            temp = string[i:j]
            if (temp != ''):
                if (vowels.find(temp[0]) != -1) and not(temp in result):
                    result.append(temp)
                    found = string.find(temp, 0)
                    if (found >= 0) : counter +=1
                    z=found+1
                    while (found>=0):
                        found = string.find(temp, z)
                        if found>=0: counter+=1;z=found+1
    return (counter)
    
    

if __name__ == '__main__':
    s = input()
    minion_game(s)