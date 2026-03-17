#Given an array of integers nums, return the value of the largest element in the array
# [3, 3, 6, 1]

array=[3,3,6,1]
n=len(array)
largest=array[0]
for i in range(0,n):
    if array[i]>largest:
        largest=array[i]
print(largest)
#-----------------------------------------------------------------------------------------------------------------
array = [3, 3, 6, 1]
largest = array[0]

for num in array:          # num directly element hai, index nahi
    if num > largest:
        largest = num

print(largest)   # 6