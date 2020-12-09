def getValidPassword():
    f = open('input.txt','r')
    passwordList = f.readlines()
    f.close()
    validPassword = 0
    for line in range(len(passwordList)):
        current = passwordList[line]
        variable = current.split(" ")
        numbers = variable[0].split("-")
        lower=int(numbers[0])
        highest=int(numbers[1])
        letter= variable[1].split(":")
        letter = letter[0]
        password = variable[2].split("\n")
        password = password[0]
        counter = 0
        for character in range(len(password)):
            if(password[character] == letter):
                counter = counter +1
        if(not(counter<lower or counter >highest)):
            validPassword = validPassword+1


    return validPassword


def getValidPasswordWith():
    f = open('input.txt','r')
    passwordList = f.readlines()
    f.close()
    validPassword = 0
    for line in range(len(passwordList)):
        current = passwordList[line]
        variable = current.split(" ")
        numbers = variable[0].split("-")
        lower=int(numbers[0])-1
        highest=int(numbers[1])-1
        letter= variable[1].split(":")
        letter = letter[0]
        password = variable[2].split("\n")
        password = password[0]
        counter = 0
        if(password[lower] == letter):
            counter = counter +1
        if(password[highest] == letter):
            counter = counter +1
        if(counter == 1):
            validPassword = validPassword+1


    return validPassword

print(getValidPassword())
print(getValidPasswordWith())