def solution(s):
    min=len(s)
    for compp_len in range(1,len(s)//2 + 1):
        answer = ""
        
        compare_str = s[0:0+compp_len]
        cnt = 1
        for i in range(0,len(s),compp_len):

            if s[i:i+compp_len] == compare_str:
                cnt += 1
            else :
                if cnt == 1:
                    answer += compare_str
                else :
                    answer += str(cnt) + compare_str
                cnt = 1
                compare_str = s[i:i+compp_len]
                
        if cnt == 1:    
            answer = answer+compare_str
        else :
            answer = answer+str(cnt)+compare_str
            
        if min > len(answer):
            min = len(answer)
            
    return min