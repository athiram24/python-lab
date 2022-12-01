start=int(input("Enter the start year:"))
end=int(input("Enter the end year:"))
print("Starting year:",start,"Ending year:",end)
print("The future leap years are:")
for i in range(start,end):
    if(i%4==0)and(i%100!=0)or(i%400==0)and(i%100==0):
        print(i)
        
