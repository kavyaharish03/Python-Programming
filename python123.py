# write a prohram to oppositiev right triangle



#num=int(input("Enter the number rows"))

#for i in range(num,0,-1):
 #   for j in range(0,i):
  #      print("*",end="")
   #print()
'''num=int(input("Enter the number rows"))
for i in range(num,0,-1):
    for j in range(0,i):
        print("*",end="")
    print()'''
# write a program to print 1,22,333,444

'''num=int(input("Enter the number"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end="")
    print() '''

'''num=int(input("Enter the number:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="")
    print()'''
'''num=int(input("Enter the number:"))
for i in range(0,num):
    for j in range(0,num-i):
        print(" ",end=" ")
    for k in range(0,i+1):
        print("*",end="")
    print("") '''
'''num=int(input("Enter the number:"))
for i in range(0,num):
    for j in range(0,num-i):
        print(" ",end="")
    for k in range(0,i+1):
        print("*",end="")
    print("") '''
'''num=int(input("Enter the number "))
for i in range(0,num):
    for j in range(0,num-i-1):
        print("",end="")
    for j in range(0,i+1):
        print("*",end=" ")
    print()'''
'''num= int(input("enter the number:"))
x=num
r=0
while num>0:
    d=num%10
    r=r%10+d
    num=num//10
if x==r:
    print("The nmber is polindrome")
else:                   
    print("The number is not polindrome")'''
'''num=int(input("Enter the number"))
x=num
r=0
while num>0:
    d=num%10
    r=r*10+d
    num=num//10
print("The reversed variable:",r)'''
'''num=int(input("Enter the number:"))
if num%2==0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")'''

'''lest=[1,23,45,67,89,456]
print(sum(lest))'''
'''lest=[1,23,45,67,89,456]
total=0
for num in lest:
    print(total)
    total=total+num
print(total)'''
lest=[1,23,45,67,89,456]
detal=[]
for num in lest:
   detal.append(num*2)
   print(detal)
