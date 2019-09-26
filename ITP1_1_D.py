#!/usr/bin/env python
# coding: utf-8

# In[26]:


print("秒数を入力してください");
s=0;
m=0;
h=0;
s = int(input());
if(0 <= s<= 86400):
    h = s // 3600;
    s= s - h*3600;
    m = s // 60;
    s = s % 60;
    print(h,":",m,":",s);


# In[ ]:




