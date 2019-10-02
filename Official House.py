#!/usr/bin/env python
# coding: utf-8

# In[25]:


n= input()
b,f,r,v= map(int,input().split())
a=0
x=0
y=0
z=0
p=0

for x in range(4):
    x+=1
    for y in range(3):
        y+=1
        for z in range (10):
            z+=1
            if(x==b and y==f and z==r):  
                print(v,end=" ")
            else:
                print(0,end =" ") 
        print()
    if y < 4:
        for y in range(20):
            print("#",end="")
        print()


# In[ ]:




