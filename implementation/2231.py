N = int(input())
top = []


for i in range(1,N):
    sum = 0 
    A = i
    while A>0:
        sum += A%10
        A = A//10
    if sum+i == N :
        top.append(i)

if len(top) == 0 :
    print(0)
else: print(top[0])
    