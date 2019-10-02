#!/usr/bin/env python
# coding: utf-8

# In[49]:


n = input()
def digitSum(n):
    s = str(n)
    a = list(map(int, s))
    return sum(a)
print(digitSum(n))


# ### 
