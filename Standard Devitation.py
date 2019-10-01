#!/usr/bin/env python
# coding: utf-8

# In[20]:


import math
list1=[]
p=0
p= int(p)
while True:
    n= input()
    n= int(n)
    if(n==0):
        break
    list1 = input().split()
    if(n<1000):
        for x in range(n):
            k=sum(int(i) for i in list1)
            list1 = [int(s) for s in list1]
            p=(list1[x] - k/n)**2/n
            x+=1
print(math.sqrt(p))


# ## 
