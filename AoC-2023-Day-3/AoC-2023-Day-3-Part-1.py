import sys
sys.path.append('..')
import AoCUtils
from typing import List
from itertools import product

inputLines = AoCUtils.listLines(day=3, part=1)

gridSize = 140

grid = [list(i) for i in inputLines]
hasNum = [[0 for i in range(gridSize)] for j in range(gridSize)]
visited = [[0 for i in range(gridSize)] for j in range(gridSize)]
numbers = []

def findNum(col, row):

    c = col; r = row
    num = []

    # find the start of the number
    while hasNum[r][c] == 1:
        c -= 1

    # complete the number
    num.append(grid[r][c])
    hasNum[r][c] = 2
    visited[r][c] = 1
    c += 1

    while c != gridSize and hasNum[r][c] != 0:
        num.append(grid[r][c])
        hasNum[r][c] = 2
        visited[r][c] = 1
        c += 1

    return int("".join(num))
    

def solve(inp):
    
    for row in range(gridSize):
        for col in range(gridSize):
            if grid[row][col].isnumeric():
                if col != 0 and grid[row][col-1].isnumeric():
                    hasNum[row][col] = 1
                else:
                    hasNum[row][col] = 2

    for row in range(gridSize):
        for col in range(gridSize):
            if grid[row][col] != '.' and grid[row][col] != 'V' and not grid[row][col].isnumeric():

                visited[row][col] = 1
            
                # traverse adjacents, there are no symbols at the edges
                for r in [row-1,row,row+1]:
                    for c in [col-1,col,col+1]:
                        if not visited[r][c]:

                            visited[r][c] = 1
        
                            # if there is a number, find the number
                            if hasNum[r][c] != 0:
                                numbers.append(findNum(c, r))


    result = sum(numbers)

    return result
    

if __name__ == '__main__':
    result = solve(inputLines)
    print(result)