# 0116(0112) 0950
# 0116(0112) 0953
# 홀수 짝수 판별하기

from testBench import *

def solution(num):
    answer = "Even" if num % 2 == 0 else "Odd"
    return answer

TestCases.addCase(3, "Odd")
TestCases.addCase(4, "Even")
TestCases.solve(solution)
TestCases.printResult()
