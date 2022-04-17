from itertools import count
import numpy as np


N = int(input())
A = [int(input()) for i in range(N)]

A_mean = round(np.mean(A),0)
print(int(A_mean))
print(int(np.median(A)))
lena = max(A)-min(A)

count_list = []
bin = []
D = list(set(A))

for i in A:
    count_list.append(A.count(i))

max_count = max(count_list)
# if count_list.count(max_count) >= 2:
#     for i in D :
#         if A.count(i) == max_count:
#             bin.append(i)
#     bin = sorted(bin)
#     if len(b) > 0 :
#     print(bin[1])
# elif len(A)==1:
#     print(A[0]) 
# else: print(A[max(count_list)]) 

if len(A) ==1:
    print(A[0])

else :
    for i in D :
        if A.count(i) == max_count:
            bin.append(i)
    bin = sorted(bin)
    if len(bin) == 1:
        print(bin[0])
    else: 
        print(bin[1])


print(lena)