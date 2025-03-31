def DivExp(a, b):
    try:
        assert a>0 , 'Number a is negative'
        if b==0:
            raise ZeroDivisionError('Number b is zero')
        c=a/b
        return c
    except ZeroDivisionError  as x:
        print("x")
    except AssertionError as x:
        print("Assertion error:" +str(x))
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
print(a,b)
print(DivExp(a,b))