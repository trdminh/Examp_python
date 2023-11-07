
n,k = map(int,input().split())

time = 240
time = time - k

time_cnt = 0
i = 0
while time_cnt <= time:
    i = i+1
    time_cnt = time_cnt + 5*i
    
if (i-1) >= n:
    print(n)
else:
    print(i-1)