def getHighestId():
    f = open('input.txt','r')
    boardingcard = f.read()
    f.close()
    boardingcard = boardingcard.split('\n')
    maxId = 0
    
    for element in boardingcard:
        rows = []
        columns = []
        for i in range(128):
            rows.append(i)
        for i in range(8):
            columns.append(i)

        for i in range(10):
            if element[i]=="F":
                rows = rows[:len(rows)//2]

            elif  element[i]== "B":
                rows = rows[len(rows)//2:]

            elif  element[i]== "R":
                columns = columns[len(columns)//2:]
            else:
                columns = columns[:len(columns)//2]
        currentId = (rows[0]*8)+columns[0]
        if(currentId > maxId):
            maxId = currentId
    return maxId

def getYourId():
    f = open('input.txt','r')
    boardingcard = f.read()
    f.close()
    boardingcard = boardingcard.split('\n')
    idList = []
    for element in boardingcard:
        rows = []
        columns = []
        for i in range(128):
            rows.append(i)
        for i in range(8):
            columns.append(i)
            
        for i in range(10):
            if element[i]=="F":
                rows = rows[:len(rows)//2]

            elif  element[i]== "B":
                rows = rows[len(rows)//2:]

            elif  element[i]== "R":
                columns = columns[len(columns)//2:]

            else:
                columns = columns[:len(columns)//2]
        currentId = (rows[0]*8)+columns[0]
        idList.append(currentId)
    for currentId in range(min(idList), max(idList) + 1):
        if currentId not in idList:
            return currentId

print(getHighestId())
print(getYourId())