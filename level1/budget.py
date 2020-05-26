def solution(d, budget):
    answer = 0
    d.sort()
    sum = 0
    for i in d:
        sum += i
        if sum > budget:
            return answer
        answer += 1
    return answer


print(solution([1,3,2,5,4],9)) # 3
print(solution([2,2,3,3],10)) # 4