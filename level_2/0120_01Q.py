# 0120 1216
# 0120 
# ㄱㅣㄴㅡㅇㄱㅐㅂㅏㄹ
from testBench import *

def solution(progress, speeds):
    answer = []
    days = []

    for p, s in zip(progress, speeds):
        if (100 - p) % s == 0:
            d = int((100 - p) // s)
        else:
            d = int((100 - p) // s) + 1

        days.append(d)
    release = []

    i = 0
    while i < len(days):
        l = list()
        l.append(days[i])

        if i == len(days) - 1:
            release.append(l)
            break


        j = i + 1

        while j < len(days): 
            if days[j] <= days[i]:
                l.append(days[j])
                j += 1

            elif days[j] > days[i]:
                release.append(l)
                i = j
                break

    answer = list(map(len, release))

    return answer

TestCases.addCase([[93, 30, 55],[1, 30, 5]], [2, 1])
TestCases.addCase([[94, 95, 96, 93, 98],[1, 1, 1, 1, 1]], [])
TestCases.solve(solution)
TestCases.printResult()
