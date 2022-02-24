import math


def solution(n, info):
    global answer, max_score_diff
    answer = [-1]
    max_score_diff = -math.inf

    def get_score_diff(lion,apeech):
        lion_sum,apeech_sum=0,0
        for i in range(11):
            if lion[i] == 0 and apeech[i] == 0:
                continue
            if apeech[i] >= lion[i]:
                apeech_sum += 10-i
            else:
                lion_sum += 10-i
        return lion_sum - apeech_sum

    def dfs(idx,apeech,lion,cnt):
        global answer, max_score_diff
        if cnt < 0 :
            return
        if idx == 11:
            lion[-1] += cnt
            score = get_score_diff(lion,apeech)

            if score <= 0:
                return 

            if max_score_diff < score :
                max_score_diff = score
                answer=lion
                
            elif max_score_diff == score :
                min_score_idx = 0 
                for i in range(10,-1,-1):
                    if answer[i] !=0 or lion[i] !=0:
                        min_score_idx = i
                        break
                if answer[min_score_idx] < lion[min_score_idx]:
                    answer = lion[:]
            return

        new_lion1 = lion[:]
        new_lion1[idx] = apeech[idx]+1
        dfs(idx+1 , apeech , new_lion1,cnt - (apeech[idx]+1))

        new_lion2 = lion[:]
        new_lion2[idx] = 0
        dfs(idx+1,apeech,new_lion2,cnt)

    dfs(0,info,[0 for _ in range(11)],n)
    return answer
