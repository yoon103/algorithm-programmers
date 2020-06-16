# 프로그래머스 - 피보나치 수
# https://programmers.co.kr/learn/courses/30/lessons/12945
# n번째 피보나치 수에 % 1234567 한 값 리턴


# # 재귀 - 런타임에러 테스트케잇 7~14
# def solution(n):
#     if n <= 1:
#         return n
#     return (solution(n-1) + solution(n-2)) % 1234567



# # 재귀&메모이제이션 - 런타임에러 7,10,13,14
# def solution(n):
#     fibo_list = [0] * (n+1)    
#     return fibonacci(n, fibo_list)
# 
# def fibonacci(n, fibo_list):
#     print(fibo_list, n)
#     if n <= 1:
#         fibo_list[n] = n
#         return n
#     if fibo_list[n] == 0:
#         fibo_list[n] = (fibonacci(n-1, fibo_list) + fibonacci(n-2, fibo_list)) % 1234567
#     print(n,fibo_list)
#     return fibo_list[n]



def solution(n):
    a = 0
    b = 1
    i = 2
    while i <= n:
        a, b = b % 1234567, (a+b) % 1234567
        i += 1
    return b


print(solution(5)) # 5
print(solution(3)) # 2