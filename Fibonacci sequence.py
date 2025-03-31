num = int(input("Enter the Fibonacci series length to be generated"))
Firsttem=0
Secondterm=1
print("The fibonacci series with",num,"terms is")
print(Firsttem,Secondterm,end=" ")
for i in range (2,num):
    Fib3 = Firsttem + Secondterm
    print(Fib3,end=" ")
    Firsttem = Secondterm
    Secondterm = Fib3