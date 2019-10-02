#!/usr/bin/env python
# coding: utf-8

# In[8]:


s=str(input())
p=str(input())
a=0
if(1<=len(p)<=len(s)<=100):
    a = set(s) & set(p)
if(a!=0):
    print("Yes")
else:
    print("No")


# In[ ]:




