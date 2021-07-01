N=int(input())
A=list(map(int,input().split()))
B,C=map(int,input().split())
answer=0

for Ai in A:
    Ai=Ai-B
    answer+=1
    if Ai<=0:
        continue
    rest = Ai%C
    if rest==0:
        answer+=Ai//C
    else :
        answer +=Ai//C +1
print(answer)