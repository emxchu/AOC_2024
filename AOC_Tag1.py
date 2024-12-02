#!/usr/bin/env python
# coding: utf-8

# In[279]:


import re
f = open('AOC_1.txt', 'r')
content = f.read()
number = content.split()
list1 = []
list2 = []
for index, item in enumerate(number):
    if index%2 == 0:
        list1.append(int(item))
    else:
        list2.append(int(item))

list1.sort()
list2.sort()
x = 0
y = 0

for index, item in enumerate(list1):
    x += abs(list1[index]-list2[index])

print(x)
    
for index, item in enumerate(list1):
    y+= list1[index]* list2.count(list1[index])

print(y)
        
get_ipython().system('jupyter nbconvert --to script mycode.ipynb')
with open('mycode.py', 'r') as f:
    lines = f.readlines()
with open('mycode.py', 'w') as f:
    for line in lines:
        if 'nbconvert --to script' in line:
            break
        else:
            f.write(line)    


# In[ ]:





# In[ ]:





# In[ ]:




