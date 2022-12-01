L1=[]
L2=[]
L3=[]
L4=[]
n1=int(input("Enter the number of elements in the first list"))
print("Enter the elements in the first list")
for i in range(n1):
      num=int(input())
      L1.append(num)

n2=int(input("Enter the number of elements in the second list:"))
print("Enter the elements in the second list")
for i in range(n2):
      num=int(input())
      L2.append(num)
print("First list:",L1)      
print("Second list:",L2)
L3=sorted(L1)
L4=sorted(L2)
print("Sorted first list:",L3)
print("Sorted second list:",L4)
L3=L1.extend(L2)
print("Sorted list after merging:",sorted(L1))
      
      
      
