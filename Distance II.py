#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
n=int(input())
list1=[]
list2=[]
list3=[]
for x in range(n):
    list1 =input().split()

    for y in range(n):
        list2 =input().split()
        list3=abs(list1[x]-list2[y])
        list4=math.sqrt(list1[x]-list2[y])**2
        list5=math.sqrt(list1[x]-list2[y])**3
print(list3)
print(list4)
print(list5)


# In[ ]:




