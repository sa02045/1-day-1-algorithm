from itertools import permutations
import math
if __name__ == "__main__":
    N=int(input())
    A=list(map(int,input().split()))
    oper_num=list(map(int,input().split())) # N-1개의 연산자
    operations = []
    for _ in range((oper_num[0])):
        operations.append('+')
    for _ in range((oper_num[1])):
        operations.append('-')
    for _ in range((oper_num[2])):
        operations.append('*')
    for _ in range((oper_num[3])):
        operations.append('/')

    max = -math.inf
    min = math.inf

    for permu in list(permutations(operations,len(operations))):
        sum = A[0]
        for i in range(len(permu)):
            if permu[i] == '+':
                sum += A[i+1] 
            if permu[i] == '-':
                sum -= A[i+1]
            if permu[i] == '*':
                sum *= A[i+1]
            if permu[i] == '/':
                if sum < 0:
                    sum = -(-sum // A[i+1])
                else :
                    sum = sum // A[i+1]
        
        if sum > max:
            max = sum
        if sum < min :
            min = sum
            
    print((max))
    print((min))


