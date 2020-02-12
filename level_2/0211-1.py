# Due           0211
# Solving in    0211(2252)
# Solved in     0211(2257)
# 최댓값과 최솟값

from testBench import *

def solution(s):
    answer = ''

    max_int = max(map(int, s.split(' ')))
    min_int = min(map(int, s.split(' ')))

    return str(min_int) + ' ' + str(max_int)


TestCases.addCase("1 2 3 4","1 4")
TestCases.addCase("-1 -2 -3 -4","-4 -1")
TestCases.addCase("-1 -1","-1 -1")
TestCases.solve(solution)
TestCases.printResult()



