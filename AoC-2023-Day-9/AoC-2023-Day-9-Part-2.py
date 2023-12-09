import sys
sys.path.append('..')
import AoCUtils
from typing import List

inputLines = AoCUtils.listLines(day=9, part=1)

def findNextSeq(ls):
    return ([ls[i] - ls[i-1] for i in range(1, len(ls))], ls[1] - ls[0])

def solve():
    
    historyInfo = [list(map(lambda x: int(x), i.split(" "))) for i in inputLines]

    pred = [i[0] for i in historyInfo]

    predSeq = [[] for i in historyInfo]
    
    for item in range(len(historyInfo)):
        while len(list(filter(lambda x: x != 0, historyInfo[item]))) != 0:
            nextSeq = findNextSeq(historyInfo[item])
            historyInfo[item] = nextSeq[0]
            predSeq[item].append(nextSeq[1])
    
    for item in range(len(predSeq)):
        for i in range(len(predSeq[item])-2, -1, -1):
            predSeq[item][i] = predSeq[item][i] - predSeq[item][i+1] 
    
    pred = [pred[i] - predSeq[i][0] for i in range(len(pred))]

    result = sum(pred)

    return result
    

if __name__ == '__main__':
    result = solve()
    print(result)