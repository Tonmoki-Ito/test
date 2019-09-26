#!/usr/bin/env python
# coding: utf-8

# In[ ]:


i=0
while True:
    i+=1
    x,y=input().split()
    if(0<=int(x) and int(y)<=10000):
        if(x>=y):
            print(y,x)
        else:
            print(x,y)
    if(i>=3000):
        print(x,y)
        break


# In[ ]:




