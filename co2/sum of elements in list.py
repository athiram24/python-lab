list=[]
num=int(input("Enter the no of elements in the list:"))
print("Enter the",num,"elements")
for i in range(num):
    n= int(input())
    list.append(n)
sum=0
for i in list:
    sum=sum+i
print("The Sum of ",num,"elements in the list is",sum)    
