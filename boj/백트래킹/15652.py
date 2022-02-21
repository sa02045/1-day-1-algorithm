if __name__ == "__main__":
    N,M = map(int,input().split())

    def dfs(seq,cnt):
        if cnt == M:
            print(" ".join(list(map(str,seq))))
            return 
        for next_number in range(1,N+1):
            if seq[-1] <= next_number:
                next_seq = seq[:]
                next_seq.append((next_number))
                dfs(next_seq,cnt+1)        

    for i in range(1,N+1):
        dfs([(i)],1)