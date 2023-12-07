import sys
sys.path.append('..')
import AoCUtils
from typing import List
import itertools

inputLines = AoCUtils.listLines(day=7, part=1)

"""
Five of a kind = [5]         prio 0
Four of a kind = [1, 4]      prio 1
Full house = [2, 3]          prio 2
Three of a kind = [1, 1, 3]  prio 3 
Two pair = [1, 2, 2]         prio 4
One pair = [1, 1, 1, 2]      prio 5
High card = [1, 1, 1, 1, 1]  prio 6
"""

handTypes = [
{
    (5, ): 0,
    (1, 4): 1,
    (2, 3): 2,
    (1, 1, 3): 3,
    (1, 2, 2): 4,
    (1, 1, 1, 2): 5,
    (1, 1, 1, 1, 1): 6
},

{
    (4, ): 0,
    (1, 3): 1,
    (2, 2): 2,
    (1, 1, 2): 3,
    (1, 1, 1, 1): 5
},

{
    (3, ): 0,
    (1, 2): 1,
    (1, 1, 1): 3
},

{
    (2, ): 0,
    (1, 1): 1
},

{
    (1, ): 0
}
]

cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def compFlatten(ls):
    return [item for row in ls for item in row]


def cardsLessThan(left, right):

    for i in range(len(left)):
        if left[i] < right[i]:
            return True
        elif left[i] > right[i]:
            return False
        
    return False


def solve():
    
    cardInfo = [i.split(" ") for i in inputLines]
    symbols = []
    jokers = []

    cardPrio = dict([(v, k) for k, v in enumerate(cards)])

    for i in range(len(cardInfo)):
        cardInfo[i][0] = [j for j in cardInfo[i][0]]
        cardInfo[i][1] = int(cardInfo[i][1])

        symbols.append(sorted([cardInfo[i][0].count(j) for j in set(cardInfo[i][0]) if j != 'J']))
        jokers.append(cardInfo[i][0].count('J'))

    for i in range(len(symbols)):
        
        if jokers[i] == 5:
            cardInfo[i].append(0)
        else:
            cardInfo[i].append(handTypes[jokers[i]][tuple(symbols[i])])
        
        cardInfo[i][0] = list(map(lambda x: cardPrio[x], cardInfo[i][0]))
    
    cardInfo = sorted(cardInfo, key=lambda x: x[2])

    cardInfo = [list(group) for key, group in itertools.groupby(cardInfo, lambda a: a[2])]

    # insertion sort here we go
    for group in cardInfo:
        if len(group) > 1:
            for i in range(1, len(group)):
                for j in range(i, 0, -1):
                    if cardsLessThan(group[j][0], group[j-1][0]):
                        group[j-1], group[j] = group[j], group[j-1]
                    else:
                        break
    
    cardInfo = compFlatten(cardInfo)

    winnings = [(len(cardInfo) - i)*cardInfo[i][1] for i in range(len(cardInfo))]

    result = sum(winnings)

    return result
    

if __name__ == '__main__':
    result = solve()
    print(result)