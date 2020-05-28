# 스택/큐 > 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587


# 1. 기존 인덱스값 같이 리스트에 저장
# 2. 반복문으로 맨 앞 요소를 pop 해서
# 2-1. 나머지 요소들 중 최대값보다 크거나 같으면 answer에 카운트+1
#        pop한 값의 idx값이 인쇄요청문서 인덱스이면 answer 리턴
# 2-2. 작으면 다시 맨 뒤에 append


def solution(priorities, location):
    answer = 0
    pri2 = [[value, idx] for idx, value in enumerate(priorities)]
    while(pri2):
        a = pri2.pop(0)    
        if a[0] >= (max(pri2)[0] if pri2 != [] else 0) :
            answer += 1
            if a[1] == location:
                return answer
        else:
            pri2.append(a)
    return answer



print(solution([2, 1, 3, 2], 2)) # 1
print(solution([1, 1, 9, 1, 1, 1], 0)) # 5