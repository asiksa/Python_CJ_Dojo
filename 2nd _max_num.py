a = [1,2,5,4,0,3]
a.sort()
print(a[-2])
#4

list1 = [0,1,2,8,3,4,5]
list2=set(list1)
print(list2)             
#{0, 1, 2, 3, 4, 5, 8}

list2.remove(max(list2))
print(max(list2))
#5

list3=[1,2,3,4,5]
list4=[]
for i in list3:
  list4.append(i)
print sorted(list4)[-2]
#4
