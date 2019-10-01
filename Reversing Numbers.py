#!/usr/bin/env python
# coding: utf-8

# In[35]:


n = int(input())
list = input().split()
a=0
for x in range(n):
    if(2*x>=n):
        break
    a=list[x]
    list[x]=list[-x-1]
    list[-x-1]=a
print( " ".join( repr(e) for e in list ) )


# In[ ]:




