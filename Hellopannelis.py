import sympy

def calculate(expression):
 
  # Check if the expression is valid.

  if not expression:
    raise ValueError("Expression cannot be empty.")

  # Remove all spaces from the expression.

  expression = expression.replace(" ", "")

  # Check if the expression contains any invalid characters.

  for char in expression:
    if char not in "+-*/()0123456789.":
      raise ValueError("Expression contains invalid character: {}".format(char))

  # Check if the expression is balanced.

  parens = 0
  for char in expression:
    if char == "(":
      parens += 1
    elif char == ")":
      parens -= 1

  if parens != 0:
    raise ValueError("Expression is not balanced.")

  # Evaluate the expression.

  result = sympy.sympify(expression)

  # Return the result.

  return result

def main():
  
  # Get the expression from the user.

  expression = input("Enter a mathematical expression: ")

  # Evaluate the expression.

  result = calculate(expression)

  # Print the result.

  print("Result:", result)

if __name__ == "__main__":
  main()