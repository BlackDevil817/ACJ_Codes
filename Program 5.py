def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)
    
num=int(input("ENTER A NUMBER: "))
r=int(input("ENTER THE VALUE OF R: "))
nCr = fact(num)/(fact(r)*fact(num-r))
print(num,"C",r,"=",nCr,sep=" ")