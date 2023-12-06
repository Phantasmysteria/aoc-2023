from functools import reduce
from math import ceil, floor, sqrt
import sys
sys.path.append('..')
import AoCUtils
from typing import List

inputLines = AoCUtils.listLines(day=6, part=1)

def solve(inp):
    
    info = [list(map(lambda y: int(y), list(filter(lambda x: x != '', j)))) for j in [i[i.find(":")+1:].split(" ") for i in inputLines]]

    """
    equation of distance: distance = x(time - x) = -x^2 + time*x for 0 <= x <= time

    then this question is equivalent to solving the number of integers in domain of x which satisfy
    x^2 - time*x + distance < 0
    """

    numWays = []

    for i in range(4):
        root1 = ceil((info[0][i] - sqrt(info[0][i]**2 - 4*info[1][i])) / 2)
        root2 = floor((info[0][i] + sqrt(info[0][i]**2 - 4*info[1][i])) / 2)
        # need to check equal
        if root1*(info[0][i]-root1) == info[1][i]:
            root1 = root1 + 1
        if root2*(info[0][i]-root2) == info[1][i]:
            root2 = root2 - 1
        numWays.append(root2 - root1 + 1)

    result = reduce(lambda acc, curr: acc * curr, numWays)

    return result
    

if __name__ == '__main__':
    result = solve(inputLines)
    print(result)