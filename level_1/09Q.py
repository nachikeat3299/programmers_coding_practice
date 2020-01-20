# 0106 1155
# 0106 1202
# 나누어떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for e in arr:
        if e % divisor == 0:
            answer.append(e)

    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer

testCases = list()
t1 = [[5, 9, 7, 10], 5]
t2 = [[2, 36, 1, 3], 1]
t3 = [[3, 2, 6], 10]
testCases.append(t1)
testCases.append(t2)
testCases.append(t3)

if __name__ == "__main__":
    for t in testCases:
        print(solution(t[0], t[1]))
