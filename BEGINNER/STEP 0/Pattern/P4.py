

# CODE

n = int(input("enter how many size of length pattern you want !!!"))


for i in range(n):
    for j in range(i+1):
        print(chr(65+i) ,end="")
    print()



# TC --> O(N*N)
# SC --> O(1)