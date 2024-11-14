add=0
for i in range(10):
    print("add is:",add)
   
   
   
    num = int(input("Enter num:"))
    sum = 0
    for i in range(num+1):
        print(f"sum of first {num} natural number{sum} ")

# find the give number or odd
add = 0
num =1 
while num<=10:
    add+=num
    add+=1
    print(add)
    
    num =int(input("enter the num:"))
    if num%2==0:
        print("Given num is even")
    else:
        print("Given num is odd")


# prime number are not ----divided
num = int(input("Ente the num:"))
for i in  range(1,num+1):
    if num % i == 0:
        isprint = isprint+1 #2
if isprint == 2:

    print(" num print is prime:")
else:
    print(" num not a prime:")
