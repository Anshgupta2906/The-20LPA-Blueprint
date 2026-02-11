#swapped an array by two pointers logic


n=int(input())
arr=[int(x) for x in input().split() ]


def swap_array(l,r,arr):
  if (l>=r):
    return
  arr[l],arr[r]=arr[r],arr[l]
  swap_array(l+1,r-1,arr)
  
swap_array(0,n-1,arr)
print(arr)