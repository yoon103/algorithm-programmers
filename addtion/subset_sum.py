# <구간 합 빠르게 계산하기>
querys = [(1,3), (2,5), (3,4)]
# N개의 정수 수열 [10, 20, 30, 40, 50]
# M개의 쿼리 L, R
#     1)     1  3
#     2)     2  5
#     ...
#     M)     3  4
# 구간 L, R 사이에 해당하는 데이터들의 합 모두 구하기
# 조건 : O(N+M)


# 슬라이싱 이용 -> O(N^2)
# 리스트 슬라이싱의 시간복잡도는 O(N)
def solution1(num_list, querys):
    answer = []
    for L,R in querys:
        answer.append(sum(num_list[L-1:R]))
    return answer




#  O(N+M) 풀이 : 
# 1) 1:N 까지 구간 합 각각 구해서 메모
# 2) 메모에서 쿼리에 필요한 구간 합 찾아 계산
#     ex.  (2,5) = (1,5) - (1,1)
#          (3,4) = (1,4) - (1,2) 
def solution2(num_list, querys):
    answer = []
    sum_memo = {}
    temp = 0
    for i in range(len(num_list)):
        temp += num_list[i]
        sum_memo[(1,i+1)] = temp
    for L, R in querys:
        if L == 1:
            answer.append(sum_memo[(L,R)])
        else:
            answer.append(sum_memo[(1,R)] - sum_memo[(1,L-1)])
    return answer



num_list = [10, 20, 30, 40, 50]
querys = [(1,3), (2,5), (3,4)]


# print(solution1(num_list, querys))
print(solution2(num_list, querys))




