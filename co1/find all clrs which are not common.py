clr1=input("Enter colours(comma separated:").split(",")
clr2=input("Enter the colours(commma separated):").split(",")

Set_diff=set(clr1)-set(clr2)
clr3=list(Set_diff)
print(clr3)
