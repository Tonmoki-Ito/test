#!/usr/bin/env python
# coding: utf-8

# In[45]:


n= int(input())
scape= None
rank=0
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
i=0
for x in range(13):
    x+=1
    list1.append(x)
for p in range(n):
    scape, rank = input().split()
    rank = int(rank)
    
    if(scape=="S"):
        for x in range(13):
            x+=1
            if x == rank:
                list2.append(rank)
                break
    elif(scape=="H"):
        for x in range(13):
            x+=1
            if x == rank:
                list3.append(rank)
                break
    elif(scape=="C"):
        for x in range(13):
            x+=1
            if x == rank:
                list4.append(rank)
                break
    elif(scape=="D"):
        for x in range(13):
            x+=1
            if x == rank:
                list5.append(rank)
                break
    else:
        print("ちゃんと入力してください")
l1=[]
l1 =set(list1)^set(list2)
for i, word in enumerate(l1):
    print("S",word)

l2=[]
l1 =set(list1)^set(list3)
for i, word in enumerate(l1):
    print("H",word)
    
l3=[]
l1 =set(list1)^set(list4)
for i, word in enumerate(l1):
    print("C",word)

l4=[]
l1 =set(list1)^set(list5)
for i, word in enumerate(l1):
    print("D",word)


# # 
