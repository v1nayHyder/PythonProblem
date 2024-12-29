def factorial(n):
    if len(n)==0:
      return n
    return factorial(n[1:])+n[0]

n="hari"
print(factorial(n))