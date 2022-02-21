from itertools import combinations

if __name__ == "__main__":
    N,S= map(int,input().split())
    numbers = list(map(int,input().split()))
    answer =0
    
    def get_sum(li):
        sum=0
        for num in li:
            sum+=num
        return sum
    for i in range(1,N+1):
        for combi in combinations(numbers,i):
            if get_sum(combi) == S:
                answer +=1
    print(answer)