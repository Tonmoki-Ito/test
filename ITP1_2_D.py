#!/usr/bin/env python
# coding: utf-8

# In[15]:


print("W(長方形の横),H（長方形の縦）,x（円の中心のx座標）,y(円の中心のy座標),r（半径）の順番に入力");
w,h,x,y,r = input().split();
if(-100 <= int(x),int(y) <= 100 and 0 < int(w),int(h),int(r)<=100):
    if(0 <= int(x) - int(r) and int(x) + int(r) <= int(w) and 0 <= int(y) - int(r) and y + r <= h):
        print("Yes");
    else:
        print("No");


# In[ ]:




