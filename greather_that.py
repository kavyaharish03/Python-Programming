a=int(input("Enter the first number 1: "))
b=int(input("Enter the second number 2: "))
c=int(input("Enter the thrid number 3: "))
d=int(input("Enter the fourth number 4: "))
if a>b and a>c and a>d:
    print(f"{a} is greatest number {b}")
elif b>c and b>a:
    print(f"{b} is greatest number {c}")
elif c>b and c>b:
    print(f"{c} is greatest number {b}")
else:
    print(f"{d} is greatest number")    
