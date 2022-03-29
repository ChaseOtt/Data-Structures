def lcm(x,y):
  if (x>y):
    n = x
  else:
    n = y
  while (True):
    if (n % x == 0 and n % y == 0):
      break
    n = n + 1
  return n

def lcmTest():
  try:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    if x < 0 or y < 0:
      raise ValueError
    else:
      print(lcm(x,y))
  except ValueError:
    print("Please only input values greater than 0.")
