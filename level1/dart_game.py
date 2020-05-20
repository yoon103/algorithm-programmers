# 프로그래머스 = [1차] 다트게임
# https://programmers.co.kr/learn/courses/30/lessons/17682

# 반복문 돌면서 
# 숫자 만나면 숫자 배열에 넣기
# STD 만나면 배열 마지막 원소에 n제곱
# '#' 만나면 배열 마지막 원소에 *(-1)
# '*' 만나면 배열 첫 원소부터 마지막 원소에 *2

def solution(dartResult):
    answer = 0
    score = []
    i = 0
    while i < len(dartResult):
        if dartResult[i].isdigit():
            if dartResult[i:i+2]=="10":
                score.append(10)
                i += 1
            else:
                score.append(int(dartResult[i]))
        elif dartResult[i] == 'S':
            score[-1] **= 1
        elif dartResult[i] == 'D':
            score[-1] **= 2
        elif dartResult[i] == 'T':
            score[-1] **= 3
        elif dartResult[i] == '#':
            score[-1] *= -1
        elif dartResult[i] == '*':
            score[-2:] = [j*2 for j in score[-2:]]
        i += 1
    answer = sum(score)
    return answer


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))