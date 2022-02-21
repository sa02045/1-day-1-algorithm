
if __name__ == "__main__":
    N= int(input())
    rows = [0] * N 
    # row[1] = 2  1번째 행, 2번쩌 열에 퀸을 놓음 # row는 하나의 값만 가지기 때문에 row는 따져줄 필요가 없어짐
    # row[2] = 2  (1,2) (2,2) 2번째 열이 겹침
    answer = 0

    def isValid(row):
        # row 까지만 탐색, row이상은 아직 안 놓았으니 탐색할 필요가 없음
        for i in range(row):
            # 같은 열인지 확인
            if rows[row] == rows[i] :
                return False
            # 대각선이 겹치는지 확인 = 열의 차이가 1인지 확인
            if rows[row] - rows[i] ==1 or rows[row] - rows[i] == -1:
                return False
        return True


