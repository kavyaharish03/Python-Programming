
print("Write a progrm to find the given number is odd or even?")

a = input("Enter a number, a=")

# logic for finding even or odd
result = int(a)%2

if result:
    print("This is odd number, result={}".format(result))
else:
    print("This is even number, result={}".format(result))
