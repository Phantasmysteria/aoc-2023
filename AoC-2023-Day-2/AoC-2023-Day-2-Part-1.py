import sys
sys.path.append('..')
import AoCUtils
from typing import List

inputLines = AoCUtils.listLines(day=2, part=1)

colors = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def compFlatten(ls):
    return [item for row in ls for item in row]

def solve(inp):

    splits = []
    gameInfo = []

    for item in inp:
        splits.append([i.split(",") for i in item[item.find(":")+1:].split(";")])

    for i in splits:
        gameInfo.append([j[1:].split(" ") for j in compFlatten(i)])

    result = 5050 # sum of 1 to 100

    # time to loop this bad boy
    for game in range(len(gameInfo)):
        for balls in gameInfo[game]:
            if int(balls[0]) > colors[balls[1]]:
                result -= (game + 1)
                break

    return result
    

if __name__ == '__main__':
    result = solve(inputLines)
    print(result)