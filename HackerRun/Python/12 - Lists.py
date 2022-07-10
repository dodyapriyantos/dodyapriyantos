if __name__ == '__main__':
    N = int(input())
    
    ListList = []
    dataOut = ''
    
    for _ in range(N):
        command = (input()).split()
        #print (command)
        if command[0] == 'insert':
            ListList.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print (ListList)
        elif command[0] == 'remove':
            ListList.remove(int(command[1]))
        elif command[0] == 'append':
            ListList.append(int(command[1]))
        elif command[0] == 'sort':
            ListList.sort()
        elif command[0] == 'pop':
            ListList.pop()
        elif command[0] == 'reverse':
            ListList.reverse()
        else:
            print (command[0] + " not known!")
