
# a =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

a = [[1,2,3],[4,5,6],[7,8,9]]



for i in range(len(a)):
    for j in range(len(a)):
        if i == 0  or i == len(a)-1:
            print(a[i][j],end=" ")
        else:
            print(a[i][len(a)-1-i],end=" ")
            
            break
# TC --> O(N*N)
# SC --> O(1)
