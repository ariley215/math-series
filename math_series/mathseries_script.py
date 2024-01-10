def fibonacci(n):
  if n <= 1:
    return 1
  
  return fibonacci(n - 2) + fibonacci(n - 1)

def lucas(n):
  if n == 0:
    return 2
  if n == 1:
    return 1
  return lucas(n - 2) + lucas(n - 1)