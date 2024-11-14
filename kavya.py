1.# write a program to find a given number is even or odd?

num=int(input("Enter the number: "))
if num%2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

2.# write a program to find a given nuumber is prime or not?

num=int(input("Enter the nmber: "))
i=2
while i<num:
    if num%2 == 0:
        print(f"{num} is not a prime")
        break
    i += 1
if i is num:
        print(f"{num} is a prime")

3.# write a program to find a big number among two numbers?

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if a>b:
    print(f"{a} is a greater than")
else
    print(f"{b} is a greater than")

4. #write a program to find a small number among two numbers?

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if a<b:
    print(f"{a} is a greater than")
else:
    print(f"{b} is a greater than")

5.# write a program to find a big number among three numbers?

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the thrid number: "))
if a>b and a>c:
    print(f"{a} is greater than: ")
elif b>a and b>c:
    print(f"{b} is greater than: ")
else:
    print(f"{c} is greater than: ")

6.# write a program to find a small number among three numbers?

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the thrid number: "))
if a<b and a<c:
    print(f"{a} is greater than: ")
elif b<a and b<c:
    print(f"{b} is greater than: ")
else:
    print(f"{c} is greater than: ")

7.# write a program to find the sum of digits of given number?

num=int(input("Enter the number:"))
sum_digits=0
while num>0:
    sum_digits += num % 10
    num//=10
print("sum of digits:",sum_digits)

8.# write a program to find the product of digits of given number?

num=int(input("Enter the number:"))
n=num
prodct_digits=1
while n!=0:
    rem=n%10
    prodct_digits =prodct_digits*rem
    n=n//10
print("the product :",product_digits)

9.# write a program to reverse give number?

num=int(input("Enter the number: "))
x=num
reverse=0
while num>0:
    d=num%10
    reverse=reverse*10+d
    num=num//10
print("The reversed number:",reverse)    

10.# write a program to find  the given number is palindrome or nor polindrome?

num=int(input("Enter the number:"))
x=num
rem=0
while num>0:
    d=num%10
    rem=rem*10+d
    num=num//10
if x==rem:    
   print("the number is palindrome")
else:
    print("the number is not palindrome")
    
11.# write a program to find the given number is arm strong number or not?

num = int(input("Enter a number: "))
sum_digits = 0
temp = num
n = len(str(num))
while temp > 0:
    sum_digits += (temp % 10) ** n
    temp //= 10
if num == sum_digits:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

12.# write a program to find the given year is leap year or not?

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

13.# write a program to print the below pattern?

num=int(input("Enter the number:"))
rows=num
for i in range(1,rows + 1):
    for j in range(1,i+1):
     print("*"* i)

14.# write a program to print the below pattern?

num=int(input("Enter the number:"))
rows=num
for i in range(rows ,0,-1):
   print("*"* i)

15.# write a program to print the below pattern?

i) num=int(input("Enter the number:"))
rows=num
for i in range(1,rows + 1):
   print(f"{i}" * i)

ii) num =int(input("Enter the number:"))
for i in range(1,11):
    print(num,"x",i,"==",num*i)

16.# write a program to print the below pattern?

num=int(input("Enter the number: "))
rows = num
for i in range(1, rows + 1):
    for j in range(1, i + 1):
     print(j, end=" ")
print()

17.# write a program to print the below pattern?

i) num=int(input("Enter the number:"))
for i in range(num):
    for j in range(num-i):
      print(num-i,end= "")
      print()

ii) num=int(input("Enter the number:"))
rows=num
for i in range(rows,0,-1):
    for j in range(1,i+1):
      print(j,end="")
      print()

18.# write a program to find first 100 even number among 1000 numbers?
num=int(input("Enter the number: "))
for i in range(1,11):
 while(i<=1000):
  print(i," ",end="")
  i+=10
  print()

print("Even Numbers 1 to 100 are")
index = 1
if i in enumerate(index):
  while index < 1000:
    if index % 2 ==0:
        print(index, end=" ")
        index +=1
        print()

19.# write a program to find first 100 prime number among 1000 numbers?

a=int(input("Enter the number a: "))
b=int(input("Enter the number b: "))
print("prime number")
while(a<=b):
    if (a%2)!=0:
        print=(a)
        a=a+1

20.# write a program to basci calculator?

operator=input("Enter the number(+-*///%):")
a=int(input("Enter the frish number:"))
b=int(input("Enter the second number:"))
if operator=="+":
    result=a+b
    print(round(result,3))
if operator=="-":    
    result=a-b
    print(round(result,3))
if operator=="*":    
    result=a*b
    print(round(result,3))
if operator=="/":    
    result=a/b
    print(round(result,3))
if operator=="//":    
    result=a//b
    print(round(result,3))
if operator=="%":    
    result=a%b
    operator(round(result,3))
else:
    print("is not a valid operator:",operator)
21.# write a program to calculate the gross salary of employee?
num=int(input("Enter the number:"))
basic_salary = float(input("Enter basic salary: "))
hra = 0.30 * basic_salary
da = 0.90 * basic_salary
gross_salary = basic_salary + hra + da
print("Gross Salary:",gross_salary)

22.# write a program to find the precentage of student for 6 subjects?

marks=float(input("Enter the marks of student: "))
for i in range(1,7):
     marks += marks
     percentage = (marks/600)*100
     print("percentage:",percentage)

23.# write a program to swap two number without using third variable?

a=int(input("Enter the first variable: "))
b=int(input("Enter the second variable: "))
print("Before swapping, a={0}, b={1}".format(int(a),int(b)))
a = a*b
b = a/b
a = a/b
print("After swapping, a={0}, b={1}".format(int(a),int(b)))

24.# write a program to swap two numbers?

a=int(input("Enter the swap number: "))
b=int(input("Enter the swap number: "))
print("Before Swapping, a={0},b={1}".format(a,b))
temp=a
a=b
b=temp

print("After Swapping, a={0},b={1}".format(a,b)


26.# write a program to find the factorial of a given number?

num=int(input("Enter the factorial number: "))
fact=1
for i in range(1,num+1):
    fact*=i
    print("The factorial number is:",fact)

27.# write a program to find the fibonacci series of a given number ?

num=int(input("Enter the number:"))
i=0
first_value=0
second_value=1
for i in range(0,num):
    if(i<=num):
        temp=i
    else:
        temp=first_value+second_value
        first_value=second_value
        second_value=temp
    print(temp)    
    
28.# write a program to print the ASCVII Table?

num=int(input("Enter the number:"))
for i in range(0,256):
 ch=chr(i)
 print("the ASCVII table is:",i,"=",ch)

29.# write a program to  print the below pattern?

num=int(input("Enter the number:"))
rows=num
for i in range(num):
    for j in range(i+1):
      print((i+j)%2,end=" ")
    print()

30.# write a program to  print the below pattern?

num=int(input("Enter the number:"))
rows=5
for i in range(1,rows + 1):
    print("*"* i)
    for j in range(rows - 1, 0,-1):
      print("*" * i)
      
31.# Write a program to check the given numbe r is stron g numbe r?

n=int (input("e nter anumber "))
temp= n
stron g=0
while temp! =0:
rem=t emp%1 0
fact= facto rial (rem )
stron g+=fa ct
temp/ /=10
if n==stro ng:
print (f"Th e numbe r{n}i s stron g numbe r")
else:
print (f"th e numbe r{n}t he number is not stron g")

32.# Write a program to check the vowel s?

a=str (inpu t("e nter sentenc e"))
strin g=a.l ower ()
print (stri ng)
count =0
list1 =["a" ,"e" ,"i" ,"o" ,"u"]
for char in strin g:
if char in list1:
count =coun t+1
print ("num ber of vowel in sente nce: ",co unt)

33.# Write a program to sum of 10 natur al numbe rs?

a=int (inpu t("e nter a numbe r"))
sum=0
for i in range (0,a ):
sum=s um+i
print (sum)

34.# Write a progr am to find a given numbe r is posit ive or negat ive?

a=int (inpu t("e nter a numbe r"))
if(a> =0):
print ("pos itiv e numbe r")
else:
print ("neg ativ e numbe r")

35.# Write a progr am to enter input is alpha bet or not?
a=str (inpu t("e nter a lette r"))
if(a> ='a'o r a>='A ')and (a>= 'z'o r a>='Z '):
print ("it is alpha bet" )
else:
print ("not a alpha bet" )

36.# Write a program to find factors of numbe r?

a=int (input("e nter a numbe r"))
print ("fac tor of numbe r{}a re:" .format(a ))
for i in range (1,a +1):
 if(a% i==0) :
   print (i)        







                

