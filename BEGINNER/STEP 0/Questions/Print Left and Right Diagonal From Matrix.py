
#code

arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

left = []
right = []

if len(arr[0]) == len(arr):

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                left.append(arr[i][j])

                right.append(arr[i][len(arr[i])-1-i])
else:
    print(" it is a rectangle matrix")

print(left)
print(right)


# TC --> O(N*N)
# SC --> O(1)


