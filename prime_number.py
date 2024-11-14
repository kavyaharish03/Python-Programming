num=int(input("Enter the prime number: "))
i=2
while i<num:
    if num%i == 0:
        print(f"{num} is not a prime number")
        break
    i+=1
if i is num:
    print(f"{num} is a prime number")    