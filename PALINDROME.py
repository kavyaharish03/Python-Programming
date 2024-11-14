'''x=input("Enter the string: ")
y=x[::-1]
if x==y:
    print("the word is palindrome")
else:
    print('the word is not a palindrome')'''
'''num=int(input())
if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")'''
'''num=int(input())
i=2
while num>0:
    if num%2==0:
        print(f"{num} is not prime")
        break
    i=i+1
if i is num:
        print(f"{num} is prime")'''
'''num=int(input())
sum=0
while num>0:
    sum+=num%10
    num=num//10
print("this num:",sum)'''

'''num=int(input())
n=num
product=1
while n!=0:
    rem=n%10
    product=product*rem
    n=n//10
print("this product:",product)'''
'''num=int(input("Enter the number:"))
sum=0
while num>0:
    sum+=num%10
    num=num//10
print(sum)'''
'''num=int(input("Enter the number:"))
product=1
while num>0:
    product*=num%10
    num=num//10
print(product)'''
'''num=int(input("Enter the number:"))
x=num
rem=0
while num>0:
    d=num%10
    rem=rem*10+d
    num=num//10
if x==rem:
    print("is palindrome")
else:
    print("is not palindrome")'''
'''num=int(input("Enter the number:"))
reversed=0
while num>0:
    d=num%10
    reversed=reversed*10+d
    num=num//10
print("this is reverse:",reversed)'''
'''num=int(input("Enter the number:"))
sum_digits = 0
temp = num
n = len(str(num))
while temp > 0:
    sum_digits += (temp % 10) ** n
    temp //= 10
if num == sum_digits:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")'''
'''num=int(input("Enter the number:"))
if (num%4==0 and num%100!=0) or (num%400==0):
    print(f"{num} is leap year")
else:
    print(f"{num} is not leap year")'''
'''num=int(input("enter the number:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print(" ")  '''
'''num=int(input("Enter the number:"))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print(" ") ''' 
'''num=int(input("Enter the number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(f"{i}",end=" ")
    print(" ")'''
'''num=int(input("Enter the number:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(f"{j}",end=" ")
    print(" ")'''
'''num=int(input("Enterr the number:"))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(f"{i}",end=" ")
    print(" ")'''
'''num=int(input("Ente the number:"))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(f"{j}",end=" ")
    print(" ")'''
'''num=int(input("Enter the number:"))
list=[]
count=0
for i in range(1,num+1):
    if i %2==0:
        list.append(i)
        count+=1
    if num>100:
        break
    print(list)
operator=input("Enter th operator(+-*/):")
num1=float(input("Enter the number:"))
num2=float(input("Enter the number:"))
if operator=='+':
    result=num1+num2
    print(round(result,3))
elif operator=='-':
    result=num1-num2
    print(round(result,3))
elif operator=='/':
    result=num1/num2
    print(round(result,3))
else:
    print("not valid operator")

num=int(input("Enter the number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)'''
'''Basicsal=int(input("Enter the number:"))
UA=(Basicsal *40)/100
HRA=(Basicsal *20)/100
Gross_sal=Basicsal+UA+HRA
print("untilities Allowance 40% of Basic salary:",UA)
print("House Rante 20% of Basic Salar:",HRA)
print("Gross Salary :",Gross_sal)
import random
print(random.randrange(1,10))'''
'''num=int(input("Enter the number:"))
for i in range(1,num+1):
    for j  in range(i):
        print((i+j)%2,end=" ")
    print(" ")
num=int(input("Enter the number:"))
i=0
first=0
second=1
for i in range(0,num):
    if(i<=num):
        temp=i
    else:
        temp=first+second
        first=second
        second=temp
    print(temp)'''
'''num=int(input("enter the number:"))
a,b=0,1
for i in range(num):
    print(i)
    a,b=b,a+b
num=int(int(input("Enter the number:")))
sum=0
for i in range(1,num):
    if(num%2==0):
        sum=sum+i
        if(sum==num):
           print("perfect number")
    else:
        print("not perfect")
for i in range(0,256):
    print(i,end='')
print(chr(i))
num=int(input("Enter the number:"))
for i in range(0,256):
 ch=chr(i)
 print("the ASCVII table is:",i,"=",ch)
num=int(input("Enter the number:"))
for i in range(1,num+1):
    for j in range(i):
        print("*",end="")
    print()
    for i in range(num,0,-1):
        for j in range(i):
            print("*",end="")
        print()
num=int(input("Enter the volews:"))
if num=="a"or num=="e" or num=="i" or num=="o" or num=="u":
    print(num,"letter in volew")
else:
    print(num,"letter not in volew")



a=str(input("enter sentence:"))
string=a.lower ()
print(string)
count=0
list1=["a" ,"e" ,"i" ,"o" ,"u"]
for char in string:
  if char in list1:
    count =count+1
print("number of vowel in sentence:",count)
sum=0
print("the first 10 natural number:")
for i in range(1,11):
    print(i,end="")
    sum+=i
    print()
print(sum)'''
'''num=int(input("enter the number:"))
if num>0:
    print(f"{num} opsitive number")
else:
    print(f"{num} nagitive number")
num=input("Enter the alphabet:")
if num>='a' and num<='z':
    print("Alphabet:")
elif num>='A' and num<='Z':
    print("Alphabet")
else:
    print("Not alphabet")
num=int(input("Enter the number:"))
for i in range(1,num+1):
    if num%i==0:
     print(i)'''
a=int (input("e nter a numbe r"))
print ("fac tor of numbe r{}a re:" .format(a ))
for i in range (1,a +1):
 if(a% i==0) :
   print (i)   


