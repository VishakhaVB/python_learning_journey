# 9. Write a program to print the following star pattern.
#    * * *
#    *   *
#    * * *
#    for n = 3

n = 3

for i in range(1, n+1):          # rows
    for j in range(1, n+1):      # columns
        
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    
    print()
