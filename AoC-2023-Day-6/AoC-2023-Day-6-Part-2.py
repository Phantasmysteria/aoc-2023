from math import ceil, floor, sqrt
import sys
sys.path.append('..')
import AoCUtils
from typing import List

inputLines = AoCUtils.listLines(day=6, part=2)

def solve(inp):
    
    info = [int("".join(k)) for k in [list(filter(lambda x: x != '', j)) for j in [i[i.find(":")+1:].split(" ") for i in inputLines]]]

    """
    Wow i had foresight in part 1, now it's trivial

    equation of distance: distance = x(time - x) = -x^2 + time*x for 0 <= x <= time

    then this question is equivalent to solving the number of integers in domain of x which satisfy
    x^2 - time*x + distance < 0
    """

    root1 = ceil((info[0] - sqrt(info[0]**2 - 4*info[1])) / 2)
    root2 = floor((info[0] + sqrt(info[0]**2 - 4*info[1])) / 2)
    # need to check equal
    if root1*(info[0]-root1) == info[1]:
        root1 = root1 + 1
    if root2*(info[0]-root2) == info[1]:
        root2 = root2 - 1

    result = root2 - root1 + 1

    return result
    

if __name__ == '__main__':
    result = solve(inputLines)
    print(result)