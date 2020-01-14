# 0112(0110) 1245
# 0112(0110) 1304
# 시저 암호
from testBench import *

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

def solution_jh(s, n):
    answer = ""

    for st in s:
        
        if st == " ":
            answer += " "
            continue

        if ord(st) > 96:
            # 소문자인 경우
            answer += chr(ord('a') + (ord(st) - ord('a') + n) % 26)

        elif ord(st) > 64:
            # 대문자인 경우
            answer += chr(ord('A') + (ord(st) - ord('A') + n) % 26)

    return answer

TestCases.addCase(["AB", 1], "BC")
TestCases.addCase(["z", 1], "a")
TestCases.addCase(["a B z", 4], "e F d")

TestCases.solve(solution)
TestCases.printResult()

