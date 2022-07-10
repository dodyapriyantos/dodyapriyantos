def swap_case(s):
    
    finalresult = ""
    for i in range (0, len(s)):
        if s[i].islower(): finalresult += s[i].upper()
        elif s[i].isupper(): finalresult += s[i].lower()
        else: finalresult += s[i]
    
    return(finalresult)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)