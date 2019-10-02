#!/usr/bin/env python
# coding: utf-8

# In[ ]:


le=list(input())
if(1<=len(le)<=1000):
    for x in range(int(input())):
        x+=1
        q=input().split()
        a,b=int(q[1]),int(q[2])
        if(q[0] == "replace "):
            le[a:b+1] = q[3]
        elif(q[0] == "reverse "):
            le[a:b+1]=reversed(le[a:b+1])
        else:
            print(*le[a:b+1],sep="")


# In[ ]:




