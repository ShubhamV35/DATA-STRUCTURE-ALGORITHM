
#code

arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for i in range(len(arr)):
    for j in range(len(arr)):
        if i == 0 or j ==0 or i == len(arr)-1 or j == len(arr)-1:
            print(arr[i][j],end=" ") 





# TC --> O(N*N)
# SC --> O(1)


