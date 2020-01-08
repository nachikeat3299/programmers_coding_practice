# 0109(0108) 2340
# 0109(0108) FAILED
# 소수 찾기

def n_solution(n):
    answer = 0
    n_list = list()
    for target in range(1, n + 1): 

        for i in range(2, target):
            if target % i == 0:
                break;

            if i == target - 1:
                n_list.append(target)

    answer = len(n_list) + 1
    return answer

def solution(n):
    n_list = [True] * (n + 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if n_list[i] == True:
            for j in range(i + i, n + 1, i):
                n_list[j] = False
    answer = len([i for i in range(2, n + 1) if n_list[i] == True])

    return answer
        


testCases = list()
testCases.append(10)
testCases.append(5)
testCases.append(2)
testCases.append(10000)

if __name__ == "__main__":
    for t in testCases:
        print(solution(t))

