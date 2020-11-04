from django.test import TestCase

# Create your tests here.
# l = []
# if not l:
#     print(1111)

import random
initial_list32 = [i for i in range(1,36)]
initial_list12 = [j for j in range(1,13)]
final_list5 = []
for rn in range(0,5):
    inlist_index = random.randint(0,len(initial_list32)-1)
    final_list5.append(initial_list32.pop(inlist_index))
final_list5 = sorted(final_list5)
final_list2 = []
for rn in range(0,2):
    inlist_index = random.randint(0,len(initial_list12)-1)
    final_list2.append(initial_list12.pop(inlist_index))
final_list2 = sorted(final_list2)
print(final_list5,final_list2)
print(final_list2)