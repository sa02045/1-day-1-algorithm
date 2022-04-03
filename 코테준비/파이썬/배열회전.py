from copy import deepcopy

def print_list(list):
    for i in range(len(list)):
        for j in range(len(list[0])):
            print(list[i][j],end=" ")
        print()


def rotate_list(list,r):
    new_list = deepcopy(list)
    for _ in range(r):
        for i in range(len(list)):
            for j in range(len(list)):
                new_list[j][len(list)-1-i] = list[i][j]

    return new_list




list1=[[1,2,3],[4,5,6],[7,8,9]]
list2=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

print_list(rotate_list(list2,2))