#!/usr/bin/env python
# coding: utf-8

# In[11]:


n, m, l = map(int,input().split())
aij = [list(map(int,input().split())) for _ in range(n)]
bij = [list(map(int,input().split())) for _ in range(m)]

[print(*x) for x in [[sum(j*k for j, k in zip(x, y)) for y in zip*bij]  for x in ail]]


# In[ ]:




