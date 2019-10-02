#!/usr/bin/env python
# coding: utf-8

# In[59]:


list = input().split()
p= len(list)
if(p<1200):
    for x in range(p):
        list[x]=list[x].swapcase()
        x+=1
    print(list)


# In[ ]:




