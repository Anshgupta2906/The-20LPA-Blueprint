#swapped an array by using one pointers logic


n=int(input())
arr=[int(x) for x in input().split() ]


def swap_array(i,arr,n):
  if i >= n // 2:
    return
  arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
  swap_array(i+1,arr,n)
  
swap_array(0,arr,n)
print(arr)