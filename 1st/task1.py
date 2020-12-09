def task1():
    numberList = []
    f = open('input.txt','r')
    numberList = f.readlines()


    for i in range(0, len(numberList)): 
        numberList[i] = int(numberList[i])

    for element in range(len(numberList)):
        for i in range(len(numberList)):
            if((numberList[element] + numberList[i])==2020):
                return(numberList[element] * numberList[i])

def task2():
    numberList = []
    f = open('input.txt','r')
    numberList = f.readlines()


    for i in range(0, len(numberList)): 
        numberList[i] = int(numberList[i])

    for element in range(len(numberList)):
        for i in range(len(numberList)):
            for j in range(len(numberList)):
                if((numberList[element] + numberList[i]+ numberList[j])==2020):
                    return(numberList[element] * numberList[i] * numberList[j])


print(task1())
print(task2())
def task1bis():
    numberList = []
    f = open('input.txt','r')
    numberList = f.read()
    print (numberList)
    for x in numberList :
        for y in numberList: 
            print(x,y)
            if x+y == 2020:
                return x*y
print(task1bis())