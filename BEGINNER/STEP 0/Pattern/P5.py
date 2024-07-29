
# A
# B C
# C D E
# D E F G
# E F G H I
# F G H I J K


# CODE

n = int(input("enter how many size of length pattern you want !!!"))

counter = 0
for i in range(n):
    for j in range(i+1):
        print(chr(65+counter),end="")
        counter = counter + 1
    counter = j+1
    print()

# TC --> O(N*N)
# SC --> O(1)
