
if __name__ == "__main__":
    N=int(input())
    S=input()
    cup_holders = N + 1 - S.count("LL")
    print(min(N,cup_holders))

