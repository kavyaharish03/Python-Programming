1.# wirite a program that will take three digits from the user add the square of each digit
'''x=int(input("Enter a number"))
a=x%10
num=x//10
b=num%10
c=num//10
print(a**2+b**2+c**2)'''
2.# print all factors of a given number provided by user
'''number = int(input("Enter a number to find its factors: "))
factors = [i for i in range(1, number + 1) if number % i == 0]
print(f"The factors of {number} are: {factors}")
num=int(input("Enter the factorial number: "))
fact=1
for i in range(1,num+1):
    fact*=i
    print("The factorial number is:",fact)
start=int(input("start:"))
end=int(input("end"))
sum=0
even_sum=0
odd_sum=0
for i in range(start,end+1,1):
    sum+=i
    if (i%2==0):
        even_sum+=i
    else:
        odd_sum+=i
print("total sum:",sum)
print("total even number:",even_sum)
print("total odd number:",odd_sum)
name="python"
i=0
while i<len(name):
    print(name[i])
    i=i+1
name="kavya"
print(len(name))
for i in (name):
    print(i)'''
#narcissistic number?
x=int(input("Enter the number:"))
a=x%10
y=x//10
b=y%10
num=y//10
c=num%10
d=num//10
y=a**4+b**4+c**4+d**4
if x==y:
    print("narcissistic number")
else:
    print("not narcissistic number")

