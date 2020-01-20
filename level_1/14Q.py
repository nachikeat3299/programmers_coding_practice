# 0108 2324
# 0108 2330
# 문자열 다루기 기본

def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        for c in s:
            if c.isalpha():
                answer = False
                break
    else:
        answer = False

    return answer

testCases = list()
t1 = "a234"
t2 = "1234"
testCases.append(t1)
testCases.append(t2)

if __name__ == "__main__":
    for t in testCases:
        print(solution(t))

