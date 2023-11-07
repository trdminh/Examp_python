n = 5
f=[0]*n
a = [1,4,3,5,2]
f[0] = 1

for i in range(1,n):
    m = 0
    for j in range(i):
        if a[j] < a[i]:
            m = f[j]
    f[i] = m+1

print(max(f))