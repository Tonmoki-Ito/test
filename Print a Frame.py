#!/usr/bin/env python
# coding: utf-8

# In[22]:


H,W = input("縦の長さと横の長さを入力してください").split()
H=int(H)
W=int(W)
if(3<= H <= 300 and 3<= W <= 300):
    for y in range(H):
        y+=1
        x=0
        for x in range (W):
            x+=1
            if(y==1 or x==1 or y==H or x==W):
                print("＃",end ="")
            else:
                print(". ",end ="") 
        print()


# In[ ]:




