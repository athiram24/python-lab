string=input("Enter a string:")
unique=set(string.split())
words=string.split()
count=dict()
for word in unique:
    count[word]=words.count(word)
print(count)    
