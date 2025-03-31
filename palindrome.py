rev=0
n=int(input("Enter a number:"))
num=n
while n !=0:
    digit=n%10
    rev=rev*10+digit
    n=n/10
print(n)
print(rev)
print(num)
if rev == num:
    print("It is a palindrome")