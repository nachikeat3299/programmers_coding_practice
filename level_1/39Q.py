# 0122(0118) 1456
# 0122(0118) 1630
### 39. 다트 게임 

from testBench import *
import re

def solution(dartResult):
    base_score = [0, 0, 0]
    SDT_multiplier = [1, 1, 1]
    star = [1, 1, 1]
    shop = [1, 1, 1]

    parse_dartResult = re.compile('[0-9]{1,2}[S|D|T][*|#]?')
    
    match_list = parse_dartResult.findall(dartResult)
    parse_match = re.compile('([0-9]{1,2})([S|D|T])([*|#]?)')
    for i, match in enumerate(match_list):
        base_score[i] = int(parse_match.search(match).group(1))
        SDT_multiplier[i] = (lambda x: 1 if x == 'S' else 2 if x == 'D' else 3 if x == 'T' else -1)(parse_match.search(match).group(2))
        shop[i] = (lambda x: -1 if x == '#' else 1)(parse_match.search(match).group(3))
        if i == 0:
            star[i] *= (lambda x: 2 if x == '*' else 1)(parse_match.search(match).group(3))
        else:
            star[i] *= (lambda x: 2 if x == '*' else 1)(parse_match.search(match).group(3))
            star[i - 1] *= (lambda x: 2 if x == '*' else 1)(parse_match.search(match).group(3))

    """
    print("bs =", base_score)
    print("MU =", SDT_multiplier)
    print("## =", shop)
    print("** =", star)
    print("=" * 60)

    """
    answer = 0
    for i, bs in enumerate(base_score):
        answer += (bs ** SDT_multiplier[i]) * shop[i] * star[i]
    
    return answer

TestCases.addCase("1S2D*3T", 37)
TestCases.addCase("1D2S#10S", 9)
TestCases.addCase("1D2S0T", 3)
TestCases.addCase("1S*2T*3S", 23)
TestCases.addCase("1D#2S*3S", 5)
TestCases.addCase("1T2D3D#", -4)
TestCases.addCase("1D2S3T*", 59)

TestCases.solve(solution)
TestCases.printResult()
