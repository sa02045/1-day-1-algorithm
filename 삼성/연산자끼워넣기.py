from itertools import permutations
if __name__ == "__main__":
    N = int(input())
    Ai = list(map(int,input().split()))

    oper = list(map(int,input().split()))
    
    oper_list=[]
    for i in range(len(oper)):
        if oper[i] == 0:
            continue
        if i==0:
            for _ in range(oper[i]):
                oper_list.append('+')
        elif i==1:
            for _ in range(oper[i]):
                oper_list.append('-')
        elif i==2:
            for _ in range(oper[i]):
                oper_list.append('x')
        elif i==3:
            for _ in range(oper[i]):
                oper_list.append('%')

    oper_list = (list(permutations(oper_list,len(oper_list))))
    
    max = -1000000001
    min = 1000000001
    sum=Ai[0]
    tmp_oper=[]
    for oper in oper_list:
        for i in range(1,N):
            if oper[i-1]=='+':
                sum += Ai[i]
            elif oper[i-1]=='-':
                sum -= Ai[i]
            elif oper[i-1]=='x':
                sum *= Ai[i]
            elif oper[i-1]=='%':
                if sum <0:
                    sum =- ( -sum // Ai[i])
                else :
                    sum = sum //Ai[i]

        if max < sum:
            max = sum
            tmp_oper =oper
        if min > sum:
            min = sum
        sum=Ai[0]


print(max)
print(min)