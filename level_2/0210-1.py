# Due           0210
# Solving in    0210(1227)
# Solved in     0210(1238)
# 폰켓몬

from testBench import *

def solution(nums):
    number_of_pocketmon_kinds = len(set(nums))
    number_of_select = len(nums) / 2
    return min(number_of_pocketmon_kinds, number_of_select)



TestCases.addCase([3, 1, 2, 3], 2)
TestCases.addCase([3, 3, 3, 2, 2, 4], 3)
TestCases.addCase([3, 3, 3, 2, 2, 2], 2)
TestCases.solve(solution)
TestCases.printResult()



