# Day 1
ip = open("day1.txt","r").readlines()

# Part 1
firstLast = lambda x: int("{}{}".format(x[0],x[-1]))
nums = [firstLast([c for c in ln.strip() if c.isnumeric()]) for ln in ip]
sum(nums)

# Part 2
numDict = dict(zip(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],range(1,10)))
intDict = {**numDict,**{str(i):i for i in range(1,10)}}

def replChar(ln):
    retVals = []
    for n in intDict.keys():
        for fnd in re.finditer(n,ln):
            retVals.append([intDict[n],fnd.start()])
    return sorted(retVals,key=lambda x: x[-1])

noTxt = [[replChar(ln)[0][0],replChar(ln)[-1][0]] for ln in ip]

final = [int("{}{}".format(ln[0],ln[-1])) for ln in noTxt]
sum(final)
