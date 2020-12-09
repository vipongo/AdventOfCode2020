f = open('input.txt','r')
mapGane = f.readlines()
def task3(right, down):
    currentCase = [0,0]
    length = len(mapGane)
    print(length)
    for line in range(len(mapGane)):
        mapGane[line]= mapGane[line].split("\n")
        mapGane[line] = mapGane[line][0]
    treeCount = 0
    for downside in range(length-1):
        if downside == length:
            break
        
        else:
            currentCase[0] =currentCase[0]+ right
            if currentCase[0]>len(mapGane[0])-1:
                currentCase[0] = currentCase[0]- len(mapGane[0])
            currentCase[1] =currentCase[1]+down
            if currentCase[1] == length:
                break
            if currentCase[1] >= len(mapGane):
                break

            if(mapGane[currentCase[1]][currentCase[0]] == '#'):
                treeCount = treeCount+1
    return treeCount
print(task3(1,1)*task3(3,1)*task3(5,1)*task3(7,1)*task3(1,2))
#print(task3(3,1))