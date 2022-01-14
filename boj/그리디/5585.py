money=1000-int(input())
changes =[500,100,50,10,5,1]
changes_index=0
cnt=0
while money:
    if money >= changes[changes_index]:
        money -= changes[changes_index]
        cnt += 1
    else:
        changes_index += 1

print(cnt)
