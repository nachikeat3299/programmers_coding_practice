# 0114(0112) 1329
# 0114(0112) 1335
# 정수 내림차순으로 배치하기

def solution(n):
    answer = 0
    s = str(n)
    digit_list = list()
    for c in s:
        digit_list.append(int(c))

    # digit_list.sort(reverse=True)
    digit_list.sort()
    for i in range(len(digit_list)):
        answer += digit_list[i] * 10 ** i


    return answer

testCases = list()
testCases.append(118372)

if __name__ == '__main__':
    for t in testCases:
        print(solution(t))
