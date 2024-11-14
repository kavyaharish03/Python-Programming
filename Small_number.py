'''a=int(input("Enter the number 1 : "))
b=int(input("Enter the number 2 : "))
if a<b:
    print(f"{a} is a less than")
else:
    print(f"{b} is a less than")'''
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
operators=input("Enter the operator(+-*/%//):")
if operators == '+':
   if a+b:
elif operators == '-':
   if a-b:
elif operators == '*':
   return a*b
elif operators == '%': 
   return a%b
elif operators =='/':
   return a/b
elif operators == '//':
   return a//b
else :
    print(f"{operators}  is a invelad operator")