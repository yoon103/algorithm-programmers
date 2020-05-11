# 프로그래머스 - [1차]비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681
# <풀이 과정>
# 10진수를 2진수로 변환할 때, 나머지 값을 이용함
# ex) 10/2= 5...0,  5/2= 2...1, 2/2= 1...0, 1/2= 0...1
#    => 10  == 1010(2)
# 따라서 두 수를 2로 나눈 나머지값으로 비교하여 둘다 0일때만 " ", 그 외의 경우는 "#" 으로 처리

def solution(n, arr1, arr2):
    answer = []
    for i in range(n): 
        row = ""
        num1 = arr1[i]
        num2 = arr2[i]
        for j in range(n):
            num1, remainder1 = divmod(num1, 2)
            num2, remainder2 = divmod(num2, 2)
            if remainder1==0 and remainder2==0:
                row = " " + row
            else:
                row = "#" + row
        answer.append(row)
    return answer



print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
# 기댓값 : ["#####", "# # #", "### #", "#  ##", "#####"]

print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
# 기댓값 : ["######", "### #", "## ##", " #### ", " #####", "### # "]