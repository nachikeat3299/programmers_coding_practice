# 0121(0117) 1143
# 0121(0117) 
### 38. 실패율

from testBench import *

# fail_rate = 스테이지에 도달했으나 아직 클리어 못한 사람 수 / 스테이지 도달한 사람 수
def solution(N, stages):
    stage_reach = [0] * (N + 1)
    stage_reach_but_not_clear = [0] * (N + 1)
    fail_rate = [(0, 0)] * (N + 1)
    for i in stages:
        if i == 1:
            stage_reach[1] += 1
            stage_reach_but_not_clear[1] += 1
    
        elif i == N + 1:
            for j in range(1, i):
                stage_reach[j] += 1

        else:
            for j in range(1, i + 1):
                stage_reach[j] += 1
            stage_reach_but_not_clear[i] += 1

    for i in range(1, N + 1):
        if stage_reach[i] == 0:
           fail_rate[i] = (i, 0)
        else:
            fail_rate[i] = (i, stage_reach_but_not_clear[i] / stage_reach[i])

    fail_rate.sort(key = lambda pair: pair[1], reverse=True)
    del fail_rate[fail_rate.index((0, 0))]
    answer = [i for i, j in fail_rate]

    return answer

TestCases.addCase([5, [2, 1, 2, 6, 2, 4, 3, 3]], [3, 4, 2, 1, 5])
TestCases.addCase([4, [4, 4, 4, 4, 4]], [4, 1, 2, 3])
TestCases.solve(solution)
TestCases.printResult()
