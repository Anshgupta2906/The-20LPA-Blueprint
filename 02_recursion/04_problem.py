#WAF to print string even if input is even and odd stng if input is odd
n=int(input())
def value(n):
  if n%2==0:
    print("Even")
  else:
    print("Odd")

value(n)
