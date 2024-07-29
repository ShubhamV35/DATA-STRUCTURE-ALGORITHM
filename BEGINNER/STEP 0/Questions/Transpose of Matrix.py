
a =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# a = [[1,2,3],[4,5,6],[7,8,9]]


temp = 0
for i in range(len(a)):
    for j in range(len(a)):
        if i < j:
            temp = a[i][j]
            a[i][j] = a[j][i]
            a[j][i] = temp
print(a)
        
# TC --> O(N*N)
# SC --> O(1)
