# 1929 소수 구하기
a,b = map(int,input().split())
list = [i+1 for i in range(1,b)]
while True:
    try:
        c = 1
        for i in len(list):
            print(list[i])
            if list[i]%list[c] == 0 :
                print(list[i],list[c])
                del list[i]
        c += 1

    except:
        break

print(list)