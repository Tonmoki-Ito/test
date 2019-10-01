#!/usr/bin/env python
# coding: utf-8

# In[22]:


n = int(input())
i=0
list=[]
if(3<=n<=10000):
    for x in range(n):
        x+=1
        if(x%3==0 and x!=0):
            list.insert(i, x)
            i+=1
print( " ".join( repr(e) for e in list ) )


# In[ ]:




