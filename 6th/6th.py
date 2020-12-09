def sumYes():
    f = open('input.txt','r')
    questions = f.read()
    f.close()
    questions = questions.split('\n\n')
    count = 0
    for element in questions:
        currentCount = 0
        currentLetters = []
        for letters in element:
            if (letters not in currentLetters) and (letters != "\n"):
                currentCount = currentCount +1
                currentLetters.append(letters)
        count = count + currentCount

    return count

def sumAllYes():
    f = open('input.txt','r')
    questions = f.read()
    f.close()
    count = 0
    questions = questions.split('\n\n')
    for groupAnswer in questions:
        groupAnswer = groupAnswer.split('\n')
        firstAnswer = groupAnswer[0]
        
        for oneAnswer in groupAnswer:
            for letters in firstAnswer:
                if letters not in oneAnswer:
                    firstAnswer = firstAnswer.replace(letters, '')
        count = count + len(firstAnswer)
    return count

print(sumYes())
print(sumAllYes())