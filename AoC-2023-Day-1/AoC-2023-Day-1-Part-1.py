import sys
sys.path.append('..')
import AoCUtils

curInput = AoCUtils.listLines(day=1, part=1)

def solve(inp):
    result = sum([int(j[0] + j[-1]) for j in [list(filter(lambda x: x.isnumeric(), i)) for i in inp]])
    print(result)

if __name__ == '__main__':
    solve(curInput)