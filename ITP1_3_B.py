#!/usr/bin/env python
# coding: utf-8

# In[127]:


i=0
k=0
list=[]
while True:
    x = int(input())
    if(1<=x and x>=10000):
        print("1<=x<=10000の整数を入力してください")
    list.append(x)
    i += 1
    if x ==0:
        break
while True:
    print("Case ",k+1,": ",list[k])
    k+=1
    if k==i-1:
        break


# 5#### 
