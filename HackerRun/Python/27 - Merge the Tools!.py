def merge_the_tools(string, k):
    # your code goes here
    list_string = splitting_string(string, k)
    for data in list_string:
        analyzeList(data)
    

def splitting_string(string, k):
    temp_out = []
    start = 0
    for i in range(int(len(string)/k)):
        temp_out.append(string[start:start+k])
        start += k
    return (temp_out)

def analyzeList(string):
    data_out = ''
    for i in range (len(string)):
        if data_out.find(string[i]) == -1:
            data_out += string[i]
    print (data_out)
    
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)