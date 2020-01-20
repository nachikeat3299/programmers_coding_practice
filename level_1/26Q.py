# 0115(0114)
# 0115(0114) 
# 제일 작은 수 제거하기

from testBench import *

def solution(arr):
    answer = []
    minima = min(arr)
    arr.remove(minima)
    answer = arr[:]
    if len(answer) < 1:
        answer = [-1]
    return answer

TestCases.addCase([4, 3, 2, 1], [4, 3, 2])
TestCases.addCase([10], [-1])

TestCases.solve(solution)
TestCases.printResult()
