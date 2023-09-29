name=str(input("Input your father's name:"))
bplace=str(input("Input your father's birth place:"))


bmonth=int(input("Input your father's birth month(MM):"))
bday=int(input("Input your father's birth day(DD):"))
byear=int(input("Input your father's birth year(YYYY):"))
cmonth=int(input("Input the current month(MM):"))
cday=int(input("Input the current day(DD):"))
cyear=int(input("Input the current year(YYYY):"))

print("Your father's name is:",name)
print("Your father's birth place is:",bplace)
if (cmonth>=bmonth) and (cday>=bday):
    print("Your father's age is:",cyear-byear)
else:
    print("Your father's age is:",cyear-byear-1)







    