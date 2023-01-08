import random

import numpy as np
list_of_6=[]
ra_list=[]
#diese_zhlen=[27,44,37,23,36,41,33,2,35,36,12,10,16,3]
diese_zhlen_1=[1,10,19,39]
diese_zhlen_2=[3,11,20,11]   #foku
diese_zhlen_3=[20,4,18,8,9]  #hi
diese_zhlen_4=[26,4,19,8,6]  #cher

haufig_3=np.array([6,19,20,22,29,30])
l1=random.choices(diese_zhlen_1,k=1)
l2=random.choices(diese_zhlen_2,k=2)
l3=random.choices(diese_zhlen_3,k=1)
l4=random.choices(diese_zhlen_4,k=2)
#5,9,11,16,23,35

ra_list.append(l1)
ra_list.append(l2)
ra_list.append(l3)
ra_list.append(l4)
li=np.concatenate(ra_list)
listen=list_of_6.append(li)
print(li)
print(list_of_6)
