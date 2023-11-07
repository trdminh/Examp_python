t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if a + b < 4:
        print('0')
    else:
        min_text = min(a,b)
        mid_text = abs(a-b)
        max_text = min_text + (mid_text//2)
        print(max_text)