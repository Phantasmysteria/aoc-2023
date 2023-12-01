import sys
sys.path.append('..')
import AoCUtils

curInput = AoCUtils.listLines(day=1, part=2)

numberList = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

def printAllCombine():
    for i in numberList:
        for j in numberList:
            if i[-1] == j[0]:
                print(f"{i}{j[1:]}")

def solve(inp):
    numerifyInp = []
    for item in inp:
        checks = [1 for i in range(9)]

        while not all(list(map(lambda x: x == 69420, checks))):
            checks = list(map(lambda x: 69420 if x == -1 else x, [item.find(numberList[j]) for j in range(9)]))
            checkMin = checks.index(min(checks))
            item = item.replace(numberList[checks.index(min(checks))], str(checks.index(min(checks))+1) + numberList[checks.index(min(checks))][-1], 1)
    
        numerifyInp.append(item)

    result = sum([int(j[0] + j[-1]) for j in [list(filter(lambda x: x.isnumeric(), i)) for i in numerifyInp]])
    print(result)

if __name__ == '__main__':
    solve(curInput)