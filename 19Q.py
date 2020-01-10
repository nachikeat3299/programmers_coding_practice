# 0111(0110) 1245
# 0111(0110) 1304
# 시저 암호

def solution(s, n):
    answer = ''
    upper_normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_normal = "abcdefghijklmnopqrstuvwxyz"
    n %= len(upper_normal)

    if n != 0:
        upper_changed = upper_normal[n:len(upper_normal)] + upper_normal[0:n]
        lower_changed = lower_normal[n:len(lower_normal)] + lower_normal[0:n]

    for c in s:
        if c in upper_normal:
            c = upper_changed[upper_normal.find(c)]

        elif c in lower_normal:
            c = lower_changed[lower_normal.find(c)]

        else:
            pass

        answer += c

    return answer

testCases = list()
testCases.append(["AB", 1])
testCases.append(["z", 1])
testCases.append(["a B z", 4])

if __name__ == "__main__":
    for t in testCases:
        print(solution(t[0], t[1]))
