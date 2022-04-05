def lcm(x,y):
  # Determines which number to add to in the function
  if (x>y):
    n = x
  else:
    n = y
  # Determines if their is a remainder when dividing n by x and y
  while (True):
    if (n % x == 0 and n % y == 0):
      break
    n = n + 1
  return n

def lcmTest():
  # Takes an input from the user of the numbers being put in the LCM function
  try:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    if x < 0 or y < 0:
      raise ValueError
    else:
      print("The Lowest Common Multiple of", x, "and", y, "is", lcm(x,y))
  # Gives and error message if the user puts in invalid numbers for x and/or y
  except ValueError:
    print("Please only input values greater than 0.")
