checkedBag = []
def containesShynyBag(lookingFor):
    f = open('input.txt','r')
    bagsRules = f.read()
    f.close()
    bagsRules = bagsRules.split('\n')
    count = 0
    for bagRule in bagsRules:
        bagRule = bagRule.split(' bags contain ')
        allBag = bagRule[1].split(', ')
        if(bagRule[0] != lookingFor):
            for element in allBag:
                if(lookingFor in element):
                    count += 1
                    if(bagRule[0] not in checkedBag):
                        checkedBag.append(bagRule[0])
                        count += containesShynyBag(bagRule[0])
                        
                    break
    return count

print(containesShynyBag("shiny gold"))

def check1(ruledict, col):
    count = 0
    for rule in list(ruledict):
        if any(col in bag for bag in ruledict[rule]) and not any('flag' in bag for bag in ruledict[rule]):
            ruledict[rule].append('flag')
            count += 1 + check1(ruledict, rule)
    return count        

def check2(ruledict, col):
    count = 0
    for bag in ruledict[col]:
        if bag != "no other":
            count += int(bag[0]) * (1 + check2(ruledict, bag[2:]))
    return count           
                                       
def main():
    ruledict = {}
    with open('input.txt', 'r') as ipnt:
        for line in ipnt:
            [outer, inner] = line.strip().split(' contain ')
            outer = outer.replace(' bags', '')
            inner = inner.strip('.').split(', ')
            ruledict[outer] =  [col.replace(' bags', '').replace(' bag', '') for col in inner]
    print('Part1: {}, Part2: {}'.format(check1(ruledict, 'shiny gold'), check2(ruledict, 'shiny gold')))
                                                                    
if __name__ == "__main__":                                          
    main()