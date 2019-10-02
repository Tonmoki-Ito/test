#!/usr/bin/env python
# coding: utf-8

# In[3]:


r, c = map(int, input().split())

array = []
for i in range(r):
    array.append(list(map(int, input().split())))
for line in array:
    line.append(sum(line))  
array.append([sum([line[i] for line in array]) for i in range(c+1)])
for line in array:
    print(*line)


# In[ ]:




