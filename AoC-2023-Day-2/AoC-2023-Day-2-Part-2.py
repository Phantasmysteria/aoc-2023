import sys
sys.path.append('..')
import AoCUtils
from typing import List

inputLines = AoCUtils.listLines(day=2, part=2)

colors = {
    "red": 0,
    "green": 1,
    "blue": 2
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

    powers = []

    # time to loop this bad boy
    for game in range(len(gameInfo)):
        mins = [0, 0, 0] # red, green, blue
        for balls in gameInfo[game]:
            if int(balls[0]) > mins[colors[balls[1]]]:
                mins[colors[balls[1]]] = int(balls[0])
        powers.append(mins[0] * mins[1] * mins[2])    

    result = sum(powers)        

    return result
    

if __name__ == '__main__':
    gameInfo = solve(inputLines)
    print(gameInfo)