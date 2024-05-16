list1=[7,8,5,1,0,5]
list1.append("hello")
list1.insert(3,"bye")
print(list1[3])
print(list1[-1])
for i in range(1,len(list1)):
    print(list1[i])
for i in list1:
    print(i)
print(list1[2:3])
print(list1[:4])
print(list1[3:])
print(list1[::3])
list1[1]="Deepu"
print(list1)