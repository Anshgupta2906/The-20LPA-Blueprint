#Given an array of integers nums, 
#return the second-largest element in the array. If the second-largest element does not exist, return -1.
# [8, 8, 7, 6, 5]
array= [8,8,7,6,5]

largest= float("-inf")
second_largest= float("-inf")

for num in array:
    if num>largest:
        second_largest=num
        largest=num
    elif num>second_largest and num!=largest:
        second_largest=num
    
print("Largest",largest)
print("Second Largest",second_largest)


    