# 0108 2320
# 0108 2324
# 문자열 내림차순으로 배치하기

def solution(s):
    answer = ''
    string_list = list(s)
    string_list.sort(reverse=True)
    for i in string_list:
        answer += i
    return answer

testCases = list()
t1 = "Zbcdefg"
testCases.append(t1)

if __name__ == "__main__":
    for t in testCases:
        print(solution(t))
