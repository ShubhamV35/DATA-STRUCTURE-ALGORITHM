

# CODE

n = int(input("enter how many size of length pattern you want !!!"))


for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
    print()

# TC --> O(N*N)
# SC --> O(1)