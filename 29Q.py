# 0117(0114) 1014
# 0117(0114) 1013
# 콜라츠 추측

from testBench import *

def doing(num):
    if num % 2 == 0:
        num /= 2
    else:
        num = num * 3 + 1
    return num

def solution(num):
    count = None
    for i in range(500):
        if num == 1:
            count = i
            break
        else:
            num = doing(num)
        if i == 499:
            count = -1
    return count

TestCases.addCase(6, 8)
TestCases.addCase(16, 4)
TestCases.addCase(626331, -1)
TestCases.solve(solution)
TestCases.printResult()
