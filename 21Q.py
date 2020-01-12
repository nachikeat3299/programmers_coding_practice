# 0113(0112) 1003
# 0113(0112) 1303
# 이상한 문자 만들기

def makeStrange(word):
    WoRd = ''
    for i in range(0, len(word)):
        if i % 2 == 0:
            WoRd += word[i].upper()
        else:
            WoRd += word[i].lower()
    return WoRd

def solution(s):
    answer = ''
    space_word = ''
    word_list = s.split(' ')
    strange_word_list = list()
    space_word_list = list()

    for word in word_list:
        if word != '':
            strange_word_list.append(makeStrange(word))

    # print(len(s))
    for i in range(len(s)):
        #print(i)
        if s[i] != " ":
            if space_word != "":
                space_word_list.append(space_word)
                space_word = ""
            
        else:
            space_word += " "
            #space_word += str(i) 
            
            if i == len(s) - 1:
                space_word_list.append(space_word)

    """ 
    print("* s", s)
    print("space_word_list", space_word_list)
    print("len(space_word_list)", len(space_word_list))
    print("strange_word_list", strange_word_list)
    print("len(strange_word_list)", len(strange_word_list))
    """
   

    if len(space_word_list) > len(strange_word_list):
        for i in range(len(strange_word_list)):
                answer += space_word_list[i]
                answer += strange_word_list[i]
        answer += space_word_list[-1]

    elif len(space_word_list) < len(strange_word_list):
        for i in range(len(space_word_list)):
                answer += strange_word_list[i]
                answer += space_word_list[i]
        answer += strange_word_list[-1]

    elif len(space_word_list) == len(strange_word_list):
        if s[0] == " ":
            # print("this")
            for i in range(len(strange_word_list)):
                answer += space_word_list[i]
                answer += strange_word_list[i]
        else:
            #print("this")
            for i in range(len(strange_word_list)):
                answer += strange_word_list[i]
                answer += space_word_list[i]
    return answer

testCases = list()
testCases.append("try hello world")
testCases.append("    aa  a")
testCases.append("bb  b    ")
testCases.append("sP aCe")



if __name__ == "__main__":
    for t in testCases:
        print(solution(t))
