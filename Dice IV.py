#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a=0;
n= int(input())
r, c = map(int, input().split())
mask = {'N':(1, 5, 2, 3, 0, 4), 'E':(3, 1, 0, 5, 4, 2), 'S':(4, 0, 2, 3, 5, 1), 'W':(2, 1, 5, 0, 4,3)} 
#1(S)→6,1(W)→3,1(E)→4,1(N)→2,2(S)→6,2(W)→3,2(E)→4,2(N)→6 
#3(S)→5,3(W)→6,3(E)→1,3(N)→2,4(S)→5,4(W)→1,4(E)→6,4(N)→2 
#5(S)→6,5(W)→3,5(E)→4,5(N)→1,6(S)→5,6(W)→3,6(E)→4,6(N)→2

for i in range(n):
    a = tuple([int x for x in input().split()])
    if r!= and c!=:
        print('Yes')
    else:
        print("No")

