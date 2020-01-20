# 0107(0108) 2222
# 0107(0108) 2231
# 문자열 내 p와 y의 개수 
def solution(s):
    answer = None
    s = s.lower()
    count_p = 0
    count_y = 0
    for c in s:
        if c == 'p':
            count_p += 1
        elif c == 'y':
            count_y += 1
    if count_p == count_y:
        answer = True
    else:
        answer = False
    return answer

testCases = list()
t1 = "pPoooyY"
t2 = "Pyy"
testCases.append(t1)
testCases.append(t2)
if __name__ == '__main__':
    for t in testCases:
        print(solution(t))
