print("Enter  big number among three")
a=int(input("Enter the number 1:"))
b=int(input("Enter the number 2:"))
c=int(input("Enter the number 3:"))
if a>b and a>c:
    print(f"{a} is a biggest number")
elif b>c and b>a:
    print(f"{b} is a biggest number")
else:
    print(f"{c} is a biggest number ")