"""
def is_pythagorean_triple (a, b, c):
  return a**2 + b**2 == c**2
a = 3
b = 4
c = 5
if is_pythagorean_triple(a, b, c):
  print("its Pythagorean Triple")
else:
  print("Not Pythagorean Triple")
"""
def is_pythagorean_triple(a, b, c):
  """
  This function checks if three numbers form a Pythagorean triple.

  Args:
      a: The first number.
      b: The second number.
      c: The third number.

  Returns:
      True if the numbers form a Pythagorean triple, False otherwise.
  """

  # Validate input types
  if not all(isinstance(x, int) and x > 0 for x in (a, b, c)):
    return False

  return a**2 + b**2 == c**2

# Get user input with validation
while True:
  try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    if a <= 0 or b <= 0 or c <= 0:
      raise ValueError("All numbers must be positive integers")
    break
  except ValueError as e:
    print("Invalid input:", e)
    print("Please enter positive integers only.")

if is_pythagorean_triple(a, b, c):
  print(f"{a}, {b}, and {c} form a Pythagorean triple.")
else:
  print(f"{a}, {b}, and {c} do not form a Pythagorean triple.")
