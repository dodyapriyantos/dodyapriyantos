if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    
    #1st solution
    #listlist = [x, y, z]
    #PermutationPossible = []
    #
    #for i in range (0, x+1):
    #    for j in range (0,y+1):
    #        for k in range (0,z+1):
    #            if (i+j+k != n): PermutationPossible.append([i, j, k])
    #print (PermutationPossible)
    
    #2nd solution
    list_x = [x for x in range (0,x+1)]
    list_y = [y for y in range (0,y+1)]
    list_z = [z for z in range (0,z+1)]
    
    PermutationPossible = []
    
    for DataList_x in list_x:
        for DataList_y in list_y:
            for DataList_z in list_z:
                if (DataList_x+DataList_y+DataList_z != n):
                    PermutationPossible.append([DataList_x, DataList_y, DataList_z])
    print (PermutationPossible)
