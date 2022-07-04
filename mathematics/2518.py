M = int(input())
N = int(input())
A = []
for i in range(M,N+1) :
    C = 1
    for j in range(2,i) : 
        if (i % j) ==  0 :
            C = 0
    if i == 1:
        C = 0
    if C == 1 :
        A.append(i)
    

if len(A) == 0 :
    print(-1)
else : 
    print(sum(A))
    print(min(A))