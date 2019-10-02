#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while 1:
    s = str(input())
    m = int(input())
    if(s == '-'): 
        break
    
    for _ in range(0,m):
        h=int(input())
        s = s[h:]+s[0:h]
    print(s)


# In[ ]:




