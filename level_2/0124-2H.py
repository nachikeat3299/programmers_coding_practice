# Due           0124
# Solving in    0123(1843 - FAILED) 
# Solving in    0127(1210 - 1435)
# 다리를 지나는 트럭 

from testBench import *

def solution(bridge_length, weight, truck_weights):
    # 트럭은 bridge_length 초 만큼의 수명동안 bridge위에서 crossing 상태에 놓인다고 보면 됨.
    time_passed = 0

    # 대기하고있는 트럭들의 list인 trucks를 선언하는데, 이 경우 각 요소는 (해당 트럭 무게, 트럭이 다리에서 진행한 거리) 이다.
    trucks = [(w, 0) for w in truck_weights]
    # print(f"- bridge_length = {bridge_length}")
    # print(f"- limit = {weight}")
    # print(f"- trucks = {trucks}")

    # print("-" * 40)
    crossed = []
    crossing = []

    # print(f"### TIME = {time_passed}")
    # print(f"* trucks = {trucks}")
    # print(f"* crossing = {crossing}")
    # print(f"* crossed = {crossed}")
    # print()

    while len(crossed) != len(truck_weights):
        # 시간을 1초 흐르게 하고 그 1초동안 일어난일을 루프에서 처리

        time_passed += 1
        # print(f"### TIME = {time_passed}")

        # 아직 다리에 오르지 않고 대기하고 있는 트럭이 존재하는 경우, 트럭이 다리 무게를 고려하여 다리에 진입할지 말지 판단
        # truck, crossing 리스트 모두 스택으로 보았고, 최 좌측에서(top = 리스트 인덱스가 0) 스택 연산이 일어난다고 보았다.
        if trucks != []:
            if sum([w for (w, lf) in crossing if lf < bridge_length] + [trucks[0][0]]) <= weight:
                crossing.append(trucks.pop(0))

        # crossing의 모든 트럭들이 다리를 거리 1씩 전진
        crossing = list(map(lambda x: (x[0], x[1] + 1), crossing))

        # 만약에 트럭이 진행한 거리가, 다리의 길이보다 크다면 crossing스택에서 pop하여 crossed 리스트에 append한다.
        if crossing[0][1] > bridge_length:
            crossed.append(crossing.pop(0))

        # print(f"* trucks = {trucks}")
        # print(f"* crossing = {crossing}")
        # print(f"* crossed = {crossed}")
        # print()
    # print("*" * 40)

    return time_passed

# bridge_length | weight | truck_weights || return
if __name__ == "__main__":
    TestCases.addCase([2, 10, [7, 4, 5, 6]], 8)
    TestCases.addCase([100, 100, [10]], 101)
    TestCases.addCase([100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]], 110)
    TestCases.solve(solution)
    TestCases.printResult()

