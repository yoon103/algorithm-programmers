# <특정한 합을 가지는 부분 연속 수열 찾기>
# - N개의 자연수로 구성된 수열이 있습니다.
# - 합이 M인 연속 수열의 개수룰 구해보세요
# - 시간제한: O(N)

# ex) 1 2 3 2 5
#  ->   2 3
#  ->     3 2
#  ->         5
# =>    총 3개


def solution(l, n):
    answer = 0
    for i in range(len(l)):
        temp = 0
        for j in range(n):
            try:
                temp += l[i+j]
                if temp == n:
                    answer += 1
            except IndexError:
                break
    return answer


print(solution([1,2,3,2,5], 5))
print(solution([1,2,3,1,5,1,2,1,5], 6))