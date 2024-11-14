'''print("Given number is even or odd")
num=int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")'''

'''print("Given nuumber is prime or not")
num = int(input("Enter a number: "))
if num > 1:
 for i in range(2, int(num**0.5) +1):
    if num % i == 0:
     print(f"{num} is not prime")
    else:
     print(f"{num} is prime")
else:
    print(f"{num} is not prime")'''

'''print("Big number among two numbers")
a=int(input("Enter the number a: "))
b=int(input("Enter the number b: "))
if a>b:
    print(f"{a} is grater than")
else:
    print(f"{b} is grater than")'''

'''print("Small number among two numbers")
a=int(input("Enter the number a: "))
b=int(input("Enter the number b: "))
if a<b:
    print(f"{a} is less than")
else:
    print(f"{b} is less than")'''

'''print("Small number among three numbers")
a=int(input("Enter the number a: "))
b=int(input("Enter the number b: "))
c=int(input("Enter the number c: "))
if a>b and a>c:
    print(f"{a} is a biggest")
elif b>c:
    print(f"{b} is a biggest")
else:
    print(f"{c} is a biggest")'''

'''print("Enter the student Name")
num=input("Student the name: ")
num1=int(input("Student num1: "))
num2=int(input("Student num2: "))
num3=int(input("Student num3: "))
num4=int(input("Student num4: "))
num5=int(input("Student num5: "))
Totalsum= (num1+num2+num3+num4+num5)
average = Totalsum/5
percentage  = Totalsum
print(f"{average},{percentage:0.2f}%")'''

'''rows = 5
for i in range(1,rows + 1):
    print ("*" * i)'''

'''rows = 4
for i in range(1,rows + 1):
    print ("*" * i)'''

'''rows = 5
for i in range(rows ,0,- 1):
    print ("*" * i)'''

'''rows = 5
for i in range(1,rows + 1):
    print (f"{i}" * i)'''

'''rows = 5
for i in range(rows ,0,- 1):
    print (f"{i}" * i)'''

'''rows = 5
for i in range(1,rows + 1):
    for j in range(1,i + 1):
     print(j, end=" ")
    print()'''

'''rows = 5
for i in range(rows, 0, -1):
        for j in range(1, i - 1):
            print(j, end=" ")
        print()'''
'''n = 5
for i in range(1,n +1): 
   print("*" * i)
for i in range(n-1,0,-1):
   print("*" * i)'''


'''n = 4
for i in range(n):
    for j in range(i + 1):
        print((i + j) % 2, end =" ")
    print()'''

'''print("sum of 10 natural number")
Total=sum(range(1,10))
print("Sum of 10 natural numbers is:",Total)'''

'''print("swap tow numbers")
a=int(input("Enter the number a:"))
b=int(input("Enter the number b:"))

print("Befor swapping, a={0},b={1}".format(a,b))

a=a*b
b=a/b
a=b/a

print("After swapping, a={0},b={1}".format(a,b))'''

'''print("Sum of digits number")
num=int(input("Enter the number:"))
sum_digits=0
while num>0:
    sum_digits += num % 10
    num//=10
    print("sum of digits:",sum_digits)'''

print("product of digits number")
num=int(input("Enter the number:"))
product_digits=1
while num>0:
    product_digits *= num % 10
    num//10
    print("product of digits:",product_digits)

'''print("program to reversed the number")
num=int(input("Enter the number : "))
reversed_num=0
while num > 0:
    reversed_num=reversed_num*10+num % 10
    num //=10
    print("Reverse number:",reversed_num)'''

'''print("palindrome number")
num=int(input("Enter the number: "))
temp=num
reversed_num=0
while temp>0:
    reversed_num=reversed_num*10+ temp % 10
    num//10
if num == reversed_num:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a polinrome")'''


'''print("Days of the week")
days=int(input("Enter a days"))
day1=int(input("Enter a sunday:"))
day2=int(input("enter a monday:"))
day3=int(input("enter a tuesday:"))
day4=int(input("enter a wednesday:"))
day5=int(input("enter a thursday:"))
day6=int(input("enter a friday:"))
day7=int(input("enter a saturday:"))
if days == day1:
    print("Enter the sunday.")
elif days == day2:
    print("Enter the monday.")
elif days == day3:
    print("Enter the tuesday.")
elif days == day3:
    print("Enter the wednesday.")
elif days == day4:
    print("Enter the thursady.")
elif days == day5:
    print("Enter thr friday.")
elif days == day6:
    print("Enter the saturday.")
else:
    print("it's not week.") '''   

'''print("Given year leap year or not")
year=int(input("Enter the leap yera:"))
if(year%4 ==0 and year%100 !=0)or(year%4==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")'''

print("Basic calculater")
a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
operators=input("Enter the operator(+,-,*,%,/,//):")

if operators == '+':
     operators("a+b")
elif operators == '-':
    print("a-b")
elif operators == '*':
    print("a*b")
elif operators == '%': 
    print("a%b")
elif operators =='/':
    print("a/b")
elif operators == '//':
    print("a//b")
   
else :
    print("invelad operator")    


'''def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return "Invalid operator"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

result = calculator(a, b, operator)
print("Resul:",result)'''


'''a=int(input("Enter the number:"))
b=int(input("enter the number:"))
add=a+b
sub=a-b
mul=a*b
div=a/b
div=a//b
mod=a%b
print("addition is:",add)
print("substraction:",sub)
print("multiplecation:",mul)
print("division:",div)
print("floor ivision:",div)
print("modulus:",mod)'''

'''m=int(input("Enter the number:"))
n=int(input("Enter the number:"))
add=m+n
print("addition :",add)'''

'''pi=3.142
radius=float(input("Enter the number:"))
area=pi*radius*radius
print(" Enter the area of the circul:",area)'''




# Define the value of pi
'''pi = 3.142

# Get the radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the area
area = pi * radius * radius

# Display the result
print("The area of the circle is:", area)

pi = 3.142'''

'''print("Enter the number input is alphabet or not")
a=input("Enter the alphabet :")

if a >= 'a' and a <= 'z':
     print("This is a alphabet")
elif a >= 'A' and a <= 'Z':
    print("This is a alphabet")
else:
    print("This  is not a alphabet:")'''

print("Q. sum of 10 natural number")
i=0
total=0
while(i<10):
    num=input("Enter the natural number {}:".format(i+1))
    total += int(num)
    i += 1
print("sum of 10 natural numbers = {}".format(total))


