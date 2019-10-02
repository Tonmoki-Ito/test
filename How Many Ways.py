#!/usr/bin/env python
# coding: utf-8

# In[11]:


while True:
    i=0
    n,x=input().split()
    n=int(n)
    x=int(x)
    if(n==0 and x==0):
        break
        
    if(3<=n<=100) and (0<=x<=300):
        for a in range(n):
            a+=1
            for b in range(n):
                b+=1
                for c in range(n):
                    c+=1
                    if(a+b+c==x):
                        i+=1
        print(i)


# In[ ]:




