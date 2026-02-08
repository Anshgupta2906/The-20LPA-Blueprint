#WAF to print all factor of N in decreasing order
n=int(input())
def decreasing_factor(n):
  for i in range(n,0,-1):
    if n%i==0:
      print(i, end=" ")
    

decreasing_factor(n)