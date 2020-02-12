# Due           0212
# Solving in    0212(1146)
# Solved in     0212(1205)
# 피보나치 수

from testBench import *

# n번째 피보나치 수 리턴
def fibbo_rec(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return fibbo(n - 1) + fibbo(n - 2)

def fibbo_iter(n):
    fib_list = [0, 1]
    while len(fib_list) != n + 1:
        f_a = fib_list[-1]
        f_b = fib_list[-2]
        fib_list.append(f_a + f_b)
    return fib_list[-1]

def solution(n):
    f = fibbo_iter(n)
    return f  % 1234567 

TestCases.addCase(3, 2)
TestCases.addCase(5, 5)
TestCases.solve(solution)
TestCases.printResult()



