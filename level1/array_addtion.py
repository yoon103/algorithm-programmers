# 행렬의 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/12950?language=python3


## solution1
# def solution(arr1, arr2):
#     answer = []
#     temp = []
#     for i in range(len(arr1)):
#         for j in range(len(arr1[0])):
#             temp.append(arr1[i][j] + arr2[i][j])
#         answer.append(temp)
#         temp = []
#     return answer


## solution2 - zip 함수 이용
def solution(arr1, arr2):
    answer = [ [x + y for x, y in zip(a1, a2)] for a1, a2 in zip(arr1, arr2)]
    return answer


print(solution([[1,2],[2,3]], [[3,4],[5,6]])) # [[4,6],[7,9]]
print(solution([[1],[2]], [[3],[4]])) # [[4],[6]]



##########################################################################
### 인덱스 접근 이상함. [0][0]으로 접근하는데 [1][0]까지 값 변경됨.
# def solution(arr1, arr2):
#     answer = [[0] * len(arr1[0])] * len(arr1)
#     print(answer)
#     for i in range(len(arr1)):
#         for j in range(len(arr1[0])):
#             print(i,j)
#             answer[i][j] = arr1[i][j] + arr2[i][j]
#             print(answer)
#     return answer