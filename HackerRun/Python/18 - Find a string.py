def count_substring(string, sub_string):
    
    
    counter = 0
    
    #1st
    index_string = string.find(sub_string)
    step = 0
    while (step < len(string)):
        if string[index_string:index_string+len(sub_string)] == sub_string:
            counter+=1
            index_string +=1
            
            #2nd and so on
            index_string = string.find(sub_string, index_string)
            if index_string == -1: break
        step+=1
        
    return (counter)

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count