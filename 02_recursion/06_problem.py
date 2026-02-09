#WAP to to do sum of first N numbers by functional way

def calculate_sum(n):
  if n==0:
    return 0
  
  return n + calculate_sum(n-1)
  
n = int(input())
result = calculate_sum(n)
print(result)
