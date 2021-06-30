def solution(p):
    def 올바른괄호인지(str):
        stack=[]
        for 괄호 in str:
            if 괄호=="(":
                stack.append(괄호)
            else:
                if len(stack)==0:
                    return False
                stack.pop()
        return len(stack)==0

    def 균형잡힌괄호_분리(str):
        cnt = 0
        for 인덱스,괄호 in enumerate(str):
            if 괄호 == "(":
                cnt+=1
            else:
                cnt-=1
            if cnt==0:
                break
        return str[:인덱스+1],str[인덱스+1:]

    def 괄호뒤집기(str):
        result =""

        for 괄호 in str:
            if 괄호 =="(":
                result += ")"
            else :
                result += "("
        return result
    
    if p=="":
        return ""
    
    u,v = 균형잡힌괄호_분리(p)
    
    if 올바른괄호인지(u):
        return u + solution(v)
    else :
        return "(" + solution(v) + ")" + 괄호뒤집기(u[1:-1])

        
