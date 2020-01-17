# 0119(0116) 1045
# 0119(0116) 1104
### 34. x만큼 간격이 있는 n개의 숫자
from testBench import *

def solution(x, n):
    answer = list()
    for i in range(n):
        answer.append(x * (i + 1))
    return answer

def err_solution(x, n):
    return list(range(x, x + n * x, x))

TestCases.addCase([2, 5], [2, 4, 6, 8, 10])
TestCases.addCase([4, 3], [4, 8, 12])
TestCases.addCase([-4, 2], [-4, -8])

TestCases.solve(solution)
TestCases.printResult()
