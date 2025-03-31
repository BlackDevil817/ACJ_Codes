import math

def main():
    r = float(input("Enter the radius of the circle: "))
    c = 2 * math.pi * r
    area = math.pi * r ** 2
    print("The circumference of the circle is: ",c)
    print("The area of the circle is: ",area)

main()