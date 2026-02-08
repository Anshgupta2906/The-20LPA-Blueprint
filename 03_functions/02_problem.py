#to print all factor of N 

n=int(input())
def factor(n):
  for i in range(1,n+1):
    if n%i==0:
      print(i, end=" ")
    
  
factor(n)