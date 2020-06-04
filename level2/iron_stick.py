# 스택/큐 > 쇠막대기
# https://programmers.co.kr/learn/courses/30/lessons/42585

# () : 레이저
# () 뒤에 나오는 ) : 쇠막대기 하나 끝났다는 표시
# 레이저로 잘려진 후면 laser = True로 설정. 
# ")"만났을 때 레이저 체크시 
# false면 true로 바꾸고 스택 길이 answer에 더하고, 
# true면 answer+1, stack 마지막 원소 pop


def solution(arrangement):
    answer = 0
    laser = False
    stack = []
    for i in arrangement:
        if i == "(":
            stack.append(i)
            laser = False
        elif i == ")":
            stack.pop(-1)
            if laser == False:
                laser = True
                answer += len(stack)
            elif laser == True:
                answer += 1         
    return answer



print(solution("()(((()())(())()))(())")) # 17
