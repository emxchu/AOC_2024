#!/usr/bin/env python
# coding: utf-8

# In[438]:


import re
f = open('AOC_3.txt', 'r')
content = f.read()
result = 0
mul = 'mul'


numbers = re.findall(r"mul\((\d+),(\d+)\)", content)
for i in numbers:
    result += int(i[0]) * int(i[1])


print(result)


result2 = 0
regex = r"don't\(\).*?do\(\)"

numbers_do = re.sub(regex, '', content, flags=re.DOTALL)
numbers2 = re.findall(r"mul\((\d+),(\d+)\)", numbers_do)

for i in numbers2:
    result2 += int(i[0]) * int(i[1])
    
print(result2)


# In[ ]:





# ## 
