#!/usr/bin/env python
# coding: utf-8

# In[27]:


H,W = input().split()
H = int(H)
W = int(W)
x = 0
y = 0
if(1 <=H<= 300 and 1<= W <= 300):
    if(H != 0 or W !=0):
        for x in range(H):
            x+=1
            for y in range (W):
                x+=1
                if(x%2==1):
                    print(".",end ="")
                else:
                    print("# ",end ="") 
            print()


# In[ ]:




