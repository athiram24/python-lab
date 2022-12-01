num=int(input("Enter the rows of the pattern:"))
n=int(num/2)
for i in range(n):
 for j in range(i+1):
    print("*",end=" ")
 print()
for i in range(n+1,0,-1):
    for j in range(0,i):
        print("* ",end=" ")
    print()    
                        
