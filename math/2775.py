T = int(input())

for i in range(T):
    K = int(input())
    N = int(input())

    A = [i for i in range(1,N+1)]
    for i in range(K):
        for i in range(1,N):
            A[i] += A[i-1]

    print(A[-1])
