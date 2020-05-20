def solution(s, n):
    answer = ''
    for c in s:
        if c == ' ':
            answer += ' '
        else:
            code = ord(c) + n
            if c.isupper() and code>ord('Z'):
                code -= 26
            elif c.islower() and code>ord('z'):
                code -= 26
            answer += chr(code)            
    return answer


print(solution("AB",1)) # "BC" 
print(solution("z",1)) # "a"
print(solution("a B z",4)) # "e F d"


	