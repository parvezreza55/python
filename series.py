

#1+2+3+⋯+n
n=int(input("enter the number"))
sum=0
for i in range(1,n+1,1):
    sum=sum+i
print(sum)

#2+4+6+⋯+n

n1=int(input("enter the number"))
sum1=0
for i in range(2,n1+1,2):
    sum1=sum1+i
print(sum1)

#1^2+2^2+.........+n^2

n2=int(input("enter the number"))
sum2=0
for i in range(1,n2+1,1):
    sum2= sum2+ i*i
print(sum2)


#1^3+2^3+3^3+⋯+n^3
n3=int(input("enter the number"))
sum3=0
for i in range(1,n3+1,1):
    sum3= sum3+ i*i*i
print(sum3)

#1+3+5+......+n
n4=int(input("enter the number"))
sum4=0
for i in range(1,n4+1,2):
    sum4= sum4+ i
print("the sum of odd num is:",sum4)
"""

#4+8+12+..........+n
n=int(input("enter the number"))
sum=0
for i in range(4,n+1,4):
    print(i)
    sum=sum+i
print(sum)

#1+1/2+1/3+.......+1/n
n1=int(input("enter the number"))
sum1=0
for i in range(1,n1+1,1):
    sum1=sum1+ 1/i
print(sum1)
"""


#fibonacci number
number = int(input("enter a number:"))
a=0
b=1
for i in range(number):
    print(a)
    c=a+b
    a=b
    b=c