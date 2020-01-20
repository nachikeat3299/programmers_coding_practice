# 0118(0116) 1131
# 0118(0116) 1139
# 하샤드 수

from testBench import *

def solution(x):
    digit_sum = 0
    for c in str(x):
        digit_sum += int(c)
    return True if x % digit_sum == 0 else False


TestCases.addCase(10, True)
TestCases.addCase(12, True)
TestCases.addCase(11, False)
TestCases.addCase(13, False)
TestCases.solve(solution)
TestCases.printResult()
