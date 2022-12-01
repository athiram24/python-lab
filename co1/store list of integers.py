l=[]
n=int(input("Enter the limit:"))
print("Enter the numbers:")
for i in range(0,n):
    num=int(input("no"))
    l.append(num)
for i in  range (len(l)):
      if(l[i]>100):
       l[i]="over"
print(l)
            
               
               
