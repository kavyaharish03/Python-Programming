'''1.# write a program to revere a string.
"Hello"->"olleH"
string="Hello"
print(string[::-1])

2.# write a program to find the given string is polindrome or not.
"hello"->Given string is not polindrome
"madam"->Given string is polindrome
a=input("Enter the first polindrome:")
b=a[::-1]
if a==b:
    print("The is polidrome")
else:
    print("The is not a polidrome")

3.# write a program to find the length of string?
Hello"->5
a="Hello"
print(len(a))

4.# implement title methond.
"iam learning python"->"I Am Learning Python"
course="i am learning python"
print("title:",course.title())

5.# find the vowel count in the string.
Hello world"->3
vowel="aeiou"
num="Hello world"
for string in num:
    if string in vowel:
      count +=1
print(count)

6.#count the no.of words in a string.
"i am learing python"->4
course="i am learing python"
print("split:",course.split())
print("i am learning python:",len(course.split()))
num=input("Enter the string:")
print(num[::-1])
x=input("Enter the letter:")
y=x[::-1]
if x==y:
    print("this is palindrome")
else:
    print("This is not palindrome")
num=input("Enter the letter:")
print(len(num))
num=input("Enter the letter:")
print(num.title())
vowel=['a','e','i','o','u']
count=0
num=str(input("Enter the string:"))
for string in num:
    if string in vowel:
        count+=1
    print(count)
Hello world"->3
vowel="aeiou"
num="Hello world"
for string in num:
    if string in vowel:
      count +=1
print(count)'''
num=input("Enter the letter:")
count=0
for i in num:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count+=1
    print(count)

































