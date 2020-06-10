# 스택/큐 > 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583


# 반복문으로 트럭 가져오기
# 1. 무게 합에서 다리 끝 도달한 트럭 무게 빼기
# 2. 새로운 트럭 다리에 넣기
#    2-1. 맨 앞 트럭 무게 <= 최대중량-중량합 : 맨 앞 트럭 넣기 & 무게 추가
#    2-2. 아니면 0 넣기 
# 3. 시간 초 증가
# 

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque(maxlen=bridge_length)
    trucks = deque(truck_weights)
    total = 0
    while trucks:
        # 다리에서 빼기
        if len(bridge) == bridge_length:
            total -= bridge.popleft()
        # 다리에 넣기
        if trucks[0] <= weight - total:
            total += trucks[0]
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
        answer += 1
    return answer+bridge_length



print(solution(2, 10, [7,4,5,6]))  # 8
print(solution(100, 100, [10])) # 101
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10])) # 110