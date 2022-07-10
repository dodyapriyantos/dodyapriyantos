if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    list_arr = list(arr)
    list_arr.sort()
    
    found = False
    for i in range (1, len(list_arr)+1):
        a = list_arr[-1*i]
        if a < list_arr[-1]: found = True
        if found == True: break
    
    print (a)
