'''nested_list=[["Apple","Banana","Guava","pomogranite"],[10,20,30,40],["Red",96.8,100,"Hello"]]
print(nested_list[0])
print(nested_list[1])
print(nested_list[2])
print(nested_list[0][1])
print(nested_list[1][2])
print(nested_list[2][3])
print(nested_list)'''
'''nested_list=[["Apple","Banana","Guava","pomogranite"],[10,20,30,40],["Red",96.8,100,"Hello"]]
for main_index in range(len(nested_list)):
    for sub_index in range(len(nested_list[main_index])):
                print(nested_list[main_index][sub_index])
    print("")
for sub_list in nested_list:
    for data in sub_list:
        print("data is :",data)
    print(" ")'''
'''list=["applle","banana","mango","cherry"]
print(list)
print(list.append("kiwe"))
print(list)
print(list.insert(1,"kiwe"))
print(list)
print(list.remove("cherry"))
print(list)'''
'''a=[0,9,8,7,5,6,4,1,3,2]
print(a.reverse())
print(a)
print(a.sort())
print(a)'''
'''count=0
num=2
while num<100:
    is_prime=True
    for i in range(2,int(num**0.5)+1):
      if num%i==0:
        is_prime=False
        break
      if is_prime:
        print(num)
        count+=1
    num+=1'''

'''count=0
num=2
while num<100:
    is_prime=True
    for i in range(2,int(num**0.5)+1):
      if num%i==0:
        is_prime=False
        break
      if is_prime:
        print(num)
        count+=1
    num+=1'''

'''count=0
num=2
while num<100:
    is_prime=True
    for i in range(2,int(num**2)+1):
        if num%i==0:
            is_prime=False
            break
        if is_prime:
            print(num)
            count+=1
    num+=1'''
sub1=int(input("telegu:"))
sub2=int(input("tamil:"))
sub3=int(input("maths:"))
sub4=int(input("physics:"))
sub5=int(input("cemistry:"))
sub6=int(input("zoolyg:"))
print()
total=sub1+sub2+sub3+sub4+sub5+sub6
print(total)
precentage=(total/600)*100
print(precentage,"%")
