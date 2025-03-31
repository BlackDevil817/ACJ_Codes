def fact(num):
    if num == 0:
        return 1
    else:
        return num*fact(num-1)
    
num=int(input("Enter a number: "))
r=int(input("Enter the value of r: "))
nCr=fact(num)/(fact(r)*fact(num-r))
print(num,"C",
      r,"=",nCr,sep=" ")