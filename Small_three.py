a=int(input("Enter the number 1: "))
b=int(input("Enter the number 2: "))
c=int(input("Enter the number 3: "))
if a<b and a<c:
    print(f"{a} is small number {b}")
elif b<c and b<a:
    print(f"{b} is small number {c}")
else:
    print(f"{c} is small number ")