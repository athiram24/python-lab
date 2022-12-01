str=input("Enter the string:")
f={}
for i in str:
    if i in f:
     f[i]+=1
        
    else:
     f[i]=1
print("The number of characters in string:",f)
      
