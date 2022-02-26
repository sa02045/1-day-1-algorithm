def solution(s):
    s=s[1:]
    s=s[:-1]
    idx = 0 
    tuples = []
    while idx <len(s):
        if s[idx] == '{':
            idx+=1
            num = ""
            stack = []
            while s[idx] != '}':
                if s[idx] == ",":
                    stack.append(int(num))
                    num = ""
                else:
                    num += (s[idx])
                idx+=1
            stack.append(int(num))
            tuples.append(stack)
        idx+=1
        
    tuples.sort(key=lambda x:len(x))
    result = []
    for tuple in tuples:
        for num in tuple:
            if not num in result:
                result.append(num)
    return result