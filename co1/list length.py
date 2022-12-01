l1=[]
num=int(input("How many numbers in list one:"))
for i in range(num):
    n=int(input("Enter number:"))
    l1.append(n)
l2=[]
num=int(input("Enter the nos in list 2:"))
for i in range(num):
    n=int(input("Enter number:"))
    l2.append(n)
if(len(l1)==len(l2)):
   print("Same length:")
else:
    print("Not same length:")
s1=0
s2=0
for i in l1:
    s1=s1+i
for i in l2:
    s2=s2+i
if(s1==s2):
    print("Sums are same:",s1)
else:
    print("Sums are not same:")
c=set(l1).intersection(l2)
if(c==0):
    print("There is no common elements in the list:")
else:
    print("common elements are:",c)
    
 
    
