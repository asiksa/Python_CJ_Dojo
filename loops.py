#!/usr/bin/env python
# coding: utf-8

# In[2]:


a= ["banana", "apple", "lemon"]
for x in a:
    print(x)


# In[6]:


b=[20, 10, 5]
print(sum(b))


# In[13]:


total = 0
for i in b:
    total = total + i
print(total)


# In[18]:




c=0
for i in range(1, 101):
    if i %3==0 and i %5==0:
        c += i
print(c) 
    


# In[19]:


#While loop 

total = 0
e = 1
while e < 5:
    total += e
    e +=1
print(total)


# In[47]:


# Sum of negative numbers

list1 = [10, 8, 7, 6, -2, -5, -10]
total = 0
i=0
while i < len(list1):   
    if list1[i] <=0:      
        total += list1[i]
    i+=1
    print(total)  


# In[ ]:
#While

list1 = [10, 8, 7, 6, -2, -5, -10]
total4 = 0
j=len(list1)-1
print(j)
while list1[j] < 0 and j<len(list1):
    total4+=list1[j]
    j-=1
print(total4) 


#FOR

list1 = [10, 8, 7, 6, -2, -5, -10]
total=0
for i in list1:
    if i <0:
        total+=i
        i+=1
print(total)

#short def

list = [10, 8, 7, 6, -2, -5, -10]
def neg_num():
    return sum(x for x in list if x <0)
print(neg_num())
