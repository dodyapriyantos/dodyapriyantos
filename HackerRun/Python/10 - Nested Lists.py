if __name__ == '__main__':
    ListNames = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ListNames.append([name, score])
        score_list.append(score)
    score_list.sort()
    
    found=False
    for i in range (0, len(score_list)):
        a = score_list[i]
        if a > score_list[0]: found=True
        if found == True: break
    
    toPrint = []
    for i in range (0, len(ListNames)):
        if a == ListNames[i][1]: toPrint.append(ListNames[i][0])
    
    toPrint.sort()
    for dataInList in toPrint: print (dataInList)
