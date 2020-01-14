# 0116(0114) 0953
# 0116(0114) 1013
# 최대공약수와 최소공배수

from testBench import *

def gcd(n, m):
    if max(n, m) % min(n, m) != 0:
        return gcd(max(n, m) % min(n, m), min(n, m))
    else:
        return min(n, m)

def solution(n, m):
    G = gcd(n, m)
    print(G)
    L = G * (n / G) * (m / G) 

    return [G, L]

TestCases.addCase([3, 12], [3, 12])
TestCases.addCase([2, 5], [1, 10])
TestCases.solve(solution)
TestCases.printResult()
