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

#Day 2
ip = open("day2.txt","r").readlines()
splt = re.compile(r"[,;]")
cutOff = {"red":12,"green":13,"blue":14}

# Part 1
def makeCntDict(gmList):
    clrDict = defaultdict(int)
    for c,b in gmList:
        b = int(b)
        clrDict[c]+=b
    return clrDict

games = [[int(ln.split(":")[0].split()[-1]),[gm.strip().split()[::-1] for gm in re.split(splt,ln.split(":")[-1].strip())]] for ln in ip]

"""
games above is formatted like this:
[[1, # Game ID
  [['blue', '7'], #Contents
   ['green', '6'],
   ['red', '3'],
   ['red', '3'],
   ['green', '5'],
   ['blue', '1'],
   ['red', '1'],
   ['green', '5'],
   ['blue', '8'],
   ['red', '3'],
   ['green', '1'],
   ['blue', '5']]],

"""
sum([idx for idx,gm in games if all([int(b)<=cutOff[c] for c,b in gm ])])

# Part 2

games = [[int(gm.split(":")[0].split()[-1]),[dict([bc.strip().split()[::-1] for bc in grp.split(",")]) for grp in gm.split(":")[-1].strip().split(";") ]] for gm in ip]

prods = []
for idx,gm in games:
    clrDict = defaultdict(list)
    for g in gm:
        for c,b in g.items():
            clrDict[c].append(int(b))
    prods.append(np.prod([max(i) for _,i in clrDict.items()]))
        
"""
games above is formatted like this:
[[1, #Game ID
  [{'blue': '7', 'green': '6', 'red': '3'}, #Contents
   {'red': '3', 'green': '5', 'blue': '1'},
   {'red': '1', 'green': '5', 'blue': '8'},
   {'red': '3', 'green': '1', 'blue': '5'}]],
   
"""
sum(prods)
