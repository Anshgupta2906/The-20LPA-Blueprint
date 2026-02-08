#print number n to 1

def number(i,n):
  if i<1:
    return
  print(i)
  number(i-1,n)
  
number(10,0)