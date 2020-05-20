def solution(n, lost, reserve):
    answer = 0
    clothes_cnt = [1] * (n+2)
    for r in reserve:
        clothes_cnt[r] += 1
    for l in lost:
        clothes_cnt[l] -= 1
    for i in range(1, n+1):
        if clothes_cnt[i] == 2:
            if clothes_cnt[i-1] == 0:
                clothes_cnt[i-1] += 1
                clothes_cnt[i] -= 1
            elif clothes_cnt[i+1] == 0:
                clothes_cnt[i+1] += 1
                clothes_cnt[i] -= 1
    zero = 0
    for i in range(1, n+1):
        if clothes_cnt[i] == 0:
            zero += 1
    answer = n - zero
    return answer


print(solution(5,[2, 4],[1, 3, 5]))
print(solution(5,[2, 4],[3]))
print(solution(3,[3],[1]))