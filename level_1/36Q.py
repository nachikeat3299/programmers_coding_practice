# 0120(0117) 1035
# 0120(0117) 1057
### 36. 예산 

from testBench import *

def solution(d, budget):
    answer = 0
    d_sorted = d[:]
    d_sorted.sort()
    for i in range(len(d)):
        d_partial_sum = sum(d_sorted[0:len(d) - i])
        if d_partial_sum <= budget and len(d) - i > answer:
            answer = len(d) - i

    return answer

TestCases.addCase([[1, 3, 2, 5, 4], 9], 3)
TestCases.addCase([[2, 2, 3, 3], 10], 4)

TestCases.solve(solution)
TestCases.printResult()
