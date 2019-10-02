#!/usr/bin/env python
# coding: utf-8

# In[18]:


a = int(input("入力する数を答えてください"))

list = input().split()
for x in range(a):  
    list[x] = int(list[x])
b = min(list)
c = max(list)
d = sum(list)
print(b,c,d)


# In[ ]:




