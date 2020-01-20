# 0107(0108) 2129
# 0107(0108) 2221
# 문자열 내 마은대로 정렬하기

def solution(strings, h):
    answer = [] 
    strings.sort()
    while len(strings) > 0:
        max_string = strings[0]
        max_index = strings.index(max_string)
        index = 0
        while index < len(strings):
            if strings[index][h] < max_string[h]:
                max_string = strings[index]
                max_index = strings.index(max_string)
            index += 1
        answer.append(max_string)
        del strings[max_index]

    return answer

testCases = list()
t1 = [["sun", "bed", "car"], 1]
t2 = [["abce", "abcd", "cdx"], 2]
testCases.append(t1)
testCases.append(t2)

if __name__ == '__main__':
    for t in testCases:
        print(solution(t[0], t[1]))

