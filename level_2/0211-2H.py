# Due           0211
# Solving in    0212(1140)
# Solved in     0212(1144)
# 최솟값 만들기

from testBench import *
from itertools import permutations


# 이러면 시간복잡도가 n!이라서 안되요~!!
def alt_solution(A, B):
    mul = lambda x: x[0] * x[1]
    suffled_lists = permutations(A)
    results_list = []
    for sl in suffled_lists:
        results_list.append(sum(map(mul, list(zip(sl, B)))))
    return min(results_list)

def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    mul = lambda x: x[0] * x[1]
    C = sum(map(mul, list(zip(A, B))))
    return C

TestCases.addCase([[1, 4, 2], [5, 4, 4]], 29)
TestCases.addCase([[1, 2], [3, 4]], 10)
TestCases.solve(solution)
TestCases.printResult()



