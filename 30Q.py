# 0117(0115) 1128
# 0117(0115) 1131
# 평균 구하기

from testBench import *

def solution(arr):
    answer = 0
    for i in arr:
        answer += i
    answer /= len(arr)
    return answer


TestCases.addCase([1, 2, 3, 4], 2.5)
TestCases.addCase([5, 5], 5)
TestCases.solve(solution)
TestCases.printResult()
