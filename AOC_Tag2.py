#!/usr/bin/env python
# coding: utf-8

# In[279]:


import re

numbers = []
with  open('AOC_2.txt', 'r') as f:
    for line in f:
        numbers_a = [int(n) for n in line.split()]
        numbers.append(numbers_a)


safe_lines = 0      
non_safe_lines = 0

def check_if_line_is_safe(list, safe_lines,non_safe_lines):
    for i in list:
        if i == sorted(i) or i == sorted(i, reverse=True):
            if all(abs(i[index]-i[index+1]) <= 3 and abs(i[index]-i[index+1]) > 0 for index in range(len(i)-1)):
                safe_lines+=1
                continue
        for l in range(len(i)):
         new_list = i.copy()    
         new_list.pop(l)
         if new_list == sorted(new_list) or new_list == sorted(new_list, reverse=True):
            if all(abs(new_list[index]-new_list[index+1]) <= 3 and abs(new_list[index]-new_list[index+1]) > 0 for index in range(len(new_list)-1)):
                safe_lines+=1
                non_safe_lines+=1
                break

    print(safe_lines)
                    
 
                


check_if_line_is_safe(numbers, safe_lines,non_safe_lines)
print(safe_lines)







