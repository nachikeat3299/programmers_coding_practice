# Due           0210
# Solving in    0210(1242)
# Solved in     0210(1300)
# 숫자의 표현

from testBench import *


def solution(n):
    init_k = 1
    bound = n / 2 if n % 2 == 0 else (n / 2) + 1
    answer_list = [n]

    while init_k < bound:
        list_ = []
        k = init_k
        sum_ = k

        while sum_ < n:
            if k + 1 <=  n - k:
                sum_ += k + 1
                k += 1
                list_.append(k)

            else:
                break

        if sum_ == n:
            answer_list.append(list_)

        init_k += 1

    return len(answer_list)



TestCases.addCase(15, 4)
TestCases.solve(solution)
TestCases.printResult()
