#WAP to to do sum of first N numbers
def sum(n,total):
  if (n<1):
    print(total)
    return
  sum(n-1,total+1)
  
sum(4,0)