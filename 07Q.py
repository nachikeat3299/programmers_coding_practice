# 0105 1849
# 0105 1906
# 가운데 글자 가져오기

def info(s, half):
    print("- s", s)
    print("- len", len(s))
    print("- half", half) 

def solution(s):
    answer = ''

    if len(s) % 2 == 0:
        half = int(len(s) / 2)
        # info(s, half)
        answer = s[half - 1 : half + 1]

    elif len(s) % 2 != 0:
        half = int(len(s) / 2)
        # info(s, half)
        answer = s[half]

    return answer

testCases = list()
t1 = 'abcde'
t2 = 'qwer'
testCases.append(t1)
testCases.append(t2)

if __name__ == "__main__":
    for i in testCases:
        print(solution(i))
