#!/usr/bin/env python
# coding: utf-8

# In[4]:


n = int(input())
T=0
H=0
for x in range(n):
    t,h=input().split()
    t=str(t)
    h=str(h)
    if len(t)==len(h):
        if(min(t,h)==t):
            T+=3
        elif(min(t,h)==h):
            H+=3
print(T,H)


# In[ ]:




