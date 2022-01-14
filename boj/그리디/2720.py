if __name__ == "__main__":
    T= int(input())
    changes=[25,10,5,1]
    for i in range(T):
        C = int(input())
        for change in changes:
            cnt = 0
            while C >= change:
                C -= change
                cnt+=1
            print(cnt,end=" ")