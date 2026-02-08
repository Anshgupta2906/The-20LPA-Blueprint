#print number 1 to n

def number(i,n):
  if i>n:
    return
  print(i)
  number(i+1,n)
  
number(1,10)