# Due           0209
# Solving in    0210(1300)
# Solved in     0210(1307)
# 다음 큰 숫자

from testBench import *

def solution(n):
    answer = 0

    k = n + 1
    while True:
        if bin(k).count('1') == bin(n).count('1'):
            break
        k += 1

    return k

TestCases.addCase(78, 83)
TestCases.addCase(15, 23)
TestCases.solve(solution)
TestCases.printResult()



