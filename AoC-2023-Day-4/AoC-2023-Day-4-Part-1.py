import sys
sys.path.append('..')
import AoCUtils
from typing import List

inputLines = AoCUtils.listLines(day=4, part=1)

def solve(inp):
    
    cardInfo = []

    for item in inp:
        cardInfo.append([i.split(" ") for i in item[item.find(":")+1:].split("|")])
    
    winnings = [0 for _ in range(len(cardInfo))]

    for j in range(len(cardInfo)):
        for i in range(len(cardInfo[j])):
            cardInfo[j][i] = list(map(lambda y: int(y), list(filter(lambda x: x != '', cardInfo[j][i]))))

    # time to find the winnings
    for card in range(len(cardInfo)):
        # [0]: winning nums, [1]: currently have

        hits = list(set(cardInfo[card][0]) & set(cardInfo[card][1]))
        winnings[card] = 0 if len(hits) == 0 else 2**(len(hits)-1)

    result = sum(winnings)

    return result
    

if __name__ == '__main__':
    result = solve(inputLines)
    print(result)