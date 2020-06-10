# 124 나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899

# [풀이]
# 10진법 -> 3진법으로 변환
# 단 0일 경우, 4로 대체 & 앞자리 수 -1

def solution(n):
    answer = ''
    while n:
        n, remainder = divmod(n, 3)
        if remainder == 0:
            answer = '4' + answer
            n -= 1
        else:
            answer = str(remainder) + answer
    return answer


print(solution(1))  # 1
print(solution(2))  # 2
print(solution(3))  # 4
print(solution(4))  # 11
print(solution(9))  # 24
print(solution(10))  # 41