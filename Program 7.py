num=input("Enter a number: ")
print("The number entered is:",num)
uniqDigit=set(num)
for elem in uniqDigit:
    print(elem,"occurs",num.count(elem),"times")