# 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584

# 반복문으로 prices 접근
# 접근한 원소의 뒤의 원소를 이중 반복문으로 접근해서 cnt+1
# 뒤의 원소가 작으면 내부 반복문 break

def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break
        answer.append(cnt)
    return answer


print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]