# 1 2 3 4 5 
# 2 2 3 4 5 
# 3 3 3 4 5 
# 4 4 4 4 5 
# 5 5 5 5 5

#for taking input from user
n=int(input())
#loop for rows
for i in range(1,n+1):
    #loop for colunmns
    for j in range(1,n+1):
        if j<=i:
            print(i,end="")
        else:
            print(j,end="")
    print()