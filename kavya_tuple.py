'''a=()
l=[]
num=int(input("Enter the limit:"))
for i in range(0,num):
    item=int(input("Enter the element:"))
    l.append(item)
a=a+tuple(1)
print("tuple is",a)'''

# write in python to create a phone dictionary


'''n=int(input("Enter the limit: "))
m={}
mob=0
name=""
i=0
for i in range(0,n):
    mob=int(input("Enter mobile number: "))
    name=str(input("Enter the name: "))
    z2=dict({mob:name})
    m.update(z2)
    print(m)
    n=int(input("Enter the no to search in dictionary: "))
    print("The name of person is ",m[n]) '''
# wap to create a list of values inputted by user
'''a=eval(input("Enter the limit:"))
n=[]
for a in range(1,a+1):
    a=eval(input("Ente the element:"))
    n.append(a) 
print(n)'''    
# wap to create a list of values inputted by user and sort in increasing order
'''a=eval(input("Enter the limit:"))
lst=[]
for a in range(1,a+1):
    a=eval(input("Ente the element:"))
    lst.append(a) 
print(lst)
l=len(lst)
for i in range(1):
    for j in range(0,1-i-1):
        if lst[j]>lst[j+1]:
            temp=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=temp
print("After sorting the list is")
print(lst)'''             