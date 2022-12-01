l=[]
oddl=[]
n=int(input("Enter the limit:"))
print("Enter the numbers:")
for i in range(n):
    num=int(input("Num"))
    l.append(num)
for i in l:
    if(i%2!=0):
        oddl.append(i)
print(oddl)            
        
        
    
            
