if __name__ == '__main__':
    s = raw_input()
    
    status = False
    for Letter in s:
        if (Letter.isalnum()): status = True; break
    print (status)
    
    status = False
    for Letter in s:
        if (Letter.isalpha()): status = True; break
    print (status)
    
    status = False
    for Letter in s:
        if (Letter.isdigit()): status = True; break
    print (status)
    
    status = False
    for Letter in s:
        if (Letter.islower()): status = True; break
    print (status)
    
    status = False
    for Letter in s:
        if (Letter.isupper()): status = True; break
    print (status)
    
