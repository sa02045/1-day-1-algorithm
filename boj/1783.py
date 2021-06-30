def sol():
    if N==1:
        return 1
    elif N==2:
        return min(4,int((M-1)/2)+1)
    elif M < 7:
        return min(4,M)
    else:
        return 5+M-7

if __name__ == "__main__":
    N,M=map(int,input().split())
    print(sol())