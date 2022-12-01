s=input("Enter the string (separated by space):")
l=s.split()
print(l)
n=len(l[0])
m=l[0]
for i in l:
    if(len(i)>n):
     m=l[i]
            
print("The longest word from the given list is",m)        
