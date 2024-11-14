num=int(input("Enter the number:"))
n=num
prodct_digits=1
while n!=0:
    rem=n%10
    prodct_digits =prodct_digits*rem
    num//=10
print(product_digits)
