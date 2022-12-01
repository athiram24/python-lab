#part A
print("1.List of positive numbers using list comprehension:")
l=[12,-6,-67,50,-70,-21,5,100,-100,99]
print("Given list:",l)
num1=[i for i in l if i>=0]
print("List of Positive numbers:",num1)        
        
#part B
print("2.Squares of number:")
print("Enter a number upto which the squares are displayed:")
n=int(input("Enter a number"))
lst=[item**2 for item in range(1,n+1)]
print("The squares upto number",n,"is",lst)

#part c
print("3.The list of vowels from a word")
print("Enter a string to display the list of vowels:")
c=input("Enter the string:")
x=[i for i in c if i in'aeiou']
print(x)
#part D
print("4.List of ordinal values from a word:")
print("Enter the string whose unicode value is to be found")
n1=input("Enter the string:")
z=[ord(i) for i in n1]
print("The unicode value of ",n1 ,"is",z)

 

       
        
