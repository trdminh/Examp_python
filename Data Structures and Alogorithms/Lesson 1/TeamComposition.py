t = int(input())

for i in range(0,t-1):
    a,b = map(int,input().split())
    if a == b:
        print((a+b)//4)
    elif a > b:
        d = a-b
        a -= d
        print((a+b)//4)

            
                
    