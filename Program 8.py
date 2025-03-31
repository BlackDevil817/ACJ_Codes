num=int(input("Enter the Fibonacci sequence length to be generated"))
Firstterm=0
Secondterm=1
print("The Fibonacci series with",num,"terms is:")
print(Firstterm,Secondterm,end=" ")
for i in range(2,num):
    Fib3=Firstterm+Secondterm
    print(Fib3,end=" ")
    Firstterm=Secondterm
    Secondterm=Fib3