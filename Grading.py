#!/usr/bin/env python
# coding: utf-8

# In[18]:


m=0
f=0
m,f,r=map(int, input().split())
if(m + f >= 80):
    print("A")
elif(65 <= m + f <= 80 and (m!=-1 and f!=-1)):
    print("B")
elif(50 <= m + f <= 65 and m!=-1 and f!=-1):
    print("C")
elif(30 <= m + f <= 50 and m!=-1 and f!=-1):
    if(r>=50):
        print("C")
    print("D")
elif(m + f <= 30 or m==-1 or f==-1 ):
    print("F")


# In[ ]:




