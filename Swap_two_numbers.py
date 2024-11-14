print("Program to swap two numbers using a temporary variable!")

a = input("Enter a: ")
b = input("Enter b: ")
a = int(a)
b = int(b)

print("Before swapping, a={0}, b={1}".format(int(a),int(b)))

a = a*b
b = a/b
a = a/b

print("After swapping, a={0}, b={1}".format(int(a),int(b)))

a =input("Enter the a:")
b =input("Enter the b:")
a =int(a)
b=int(b)
print("Before Swapping, a={0},b={1}".format(a,b))
temp=a
a=b
b=temp

print("After Swapping, a={0},b={1}".format(a,b))
