n=int(input("Enter a number"))
for i in range(1,n+1):
    x=i
    for j in range(i+1):
      print(x,end=" ")
      x=x+i
    print()   
