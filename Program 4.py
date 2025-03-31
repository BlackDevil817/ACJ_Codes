Pname=input("Enter a person name: ")
year=int(input("Enter the year of birth: "))
curyear=int(input("Enter the current year: "))
Age=curyear-year
if Age<=60:
    print(Pname,"is not a senior citizen")
else:
    print(Pname,"is a senior citizen")