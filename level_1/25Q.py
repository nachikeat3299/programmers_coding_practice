# 0115(0112) 1336
# 0115(0112) FAILED
# 0115(0113) 1135
# 0115(0113) SOLVED

# 정수 제곱근 판별 
import math
from testBench import *

def solution(n):
    answer = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n // i == i and n % i == 0: 
            answer = (i + 1) ** 2
    if n == 0:
        answer = 1
    if answer == 0:
        answer = -1
    return answer

def solution_jh(num):
    a = -1
    for n in range(0, int(math.sqrt(num)) + 1):
        if num == n * n:
            a = (n + 1) ** 2
    return a

def solution_hj(num):
    answer = -1
    for i in range(1, int(math.sqrt(num)) + 1):
        if num // i == i and num % i == 0:
            answer = (i + 1) ** 2
    return answer

TestCases.addCase(121, 144)
TestCases.addCase(17, -1)
TestCases.addCase(3, -1)
TestCases.addCase(5, -1)
TestCases.addCase(1000000, 1000)

TestCases.solve(solution)
TestCases.printResult()
