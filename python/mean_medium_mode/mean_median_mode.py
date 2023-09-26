#mean

list = [3,4,5,6,6,8,9,10]
mean = sum(list)/len(list)
print("Mean of list = ",mean)

#median
list.sort
if len(list) % 2 == 1:
    median = list[len(list)//2]
else :
    m1 = list[len(list)//2]
    m2 = list[len(list)//2 - 1]
    median = (m1 + m2)/2
print("Median of list = ", median)

#mode


frequency = {}
for i in list:
    frequency.setdefault(i, 0)
    frequency[i]+=1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print("Mode of list = ",mode)
