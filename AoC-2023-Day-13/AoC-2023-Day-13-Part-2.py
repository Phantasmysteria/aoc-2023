import itertools
import math
import sys
sys.path.append('..')
import AoCUtils
from typing import List
import numpy as np

inputLines = AoCUtils.listLines(day=13, part=1)

def solve():
    
    mirrorGrid = [list(y) for x, y in itertools.groupby(inputLines, lambda a: a == '') if not x]
    mirrorGrid = [np.array([np.array([i for i in chars]) for chars in grid]) for grid in mirrorGrid]

    flippedGrid = [np.transpose(grid) for grid in mirrorGrid]

    refls = []

    for grid in range(len(mirrorGrid)):
        gridRow, gridCol = mirrorGrid[grid].shape
        
        rowReflFound = False
        colReflFound = False

        # rows
        for rowRefl in [i+0.5 for i in range(0,gridRow-1)]:

            applySmudgeFix = False
            rowReflCheck = True

            if rowReflFound:
                break

            upStart = math.floor(rowRefl)
            downStart = math.ceil(rowRefl)

            while upStart > -1 and downStart < gridRow:
                if any(mirrorGrid[grid][upStart] != mirrorGrid[grid][downStart]):
                    if not applySmudgeFix and np.sum(mirrorGrid[grid][upStart] != mirrorGrid[grid][downStart]) == 1:
                        applySmudgeFix = True
                    else:
                        rowReflCheck = False
                
                upStart -= 1
                downStart += 1

            if rowReflCheck and applySmudgeFix:
                refls.append((rowRefl+0.5)*100)
                rowReflFound = True
        
        if rowReflFound:
            continue

        # cols
        for colRefl in [i+0.5 for i in range(0,gridCol-1)]:

            applySmudgeFix = False
            colReflCheck = True

            if colReflFound:
                break

            leftStart = math.floor(colRefl)
            rightStart = math.ceil(colRefl)

            while leftStart > -1 and rightStart < gridCol:
                if any(flippedGrid[grid][leftStart] != flippedGrid[grid][rightStart]):
                    if not applySmudgeFix and np.sum(flippedGrid[grid][leftStart] != flippedGrid[grid][rightStart]) == 1:
                        applySmudgeFix = True
                    else:
                        colReflCheck = False
                
                leftStart -= 1
                rightStart += 1

            if colReflCheck and applySmudgeFix:
                refls.append(colRefl+0.5)
                colReflFound = True

    result = int(sum(refls))

    return result
    

if __name__ == '__main__':
    result = solve()
    print(result)