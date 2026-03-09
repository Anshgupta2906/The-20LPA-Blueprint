array=[64,34,25,12,22,11,90,5]

n=len(array)
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if array[j]<array[min_index]:
            min_index=j
    array[i],array[min_index]=array[min_index],array[i]

print("sorted array:",array)