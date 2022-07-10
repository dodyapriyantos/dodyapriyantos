import textwrap

def wrap(string, max_width):
    
    tempString = ""
    startIndex = 0
    for i in range(1, len(string)+1):
        if (i % max_width == 0):
            tempString = tempString+string[startIndex:i] + "\n"; startIndex = i
            if (i+max_width > len(string)): tempString = tempString + string[i:]
    return(tempString)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)