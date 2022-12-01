def pallendrome(str):
        s1=str
        s2=str[-1::-1]
        print("Reverse of the given string:",s2)
        if(s1==s2):
           print("String is palllendrome:")
        else:
           print("String is not  pallendrome:")
str=input("Enter the string to be checked:")
print("Given string:",str)
pallendrome(str)
