from math import sqrt 
myList=[]
num=int(input("Enter the number of elements in the list: "))
for i in range(num):
    x=int(input("Enter a number: "))
    myList.append(x)
print('The length of the list is:',len(myList))
print('List contents:',myList)
total=0
for i in myList:
    total+=i
mean=total/num
total=0
for i in myList:
    total+=(i-mean)**2
variance=total/num
stdDev=sqrt(variance)
print('Mean:',mean)
print('Variance:',variance)
print('Standard Deviation:',"%.2f"%stdDev)