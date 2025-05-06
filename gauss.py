import numpy as np

# max_index = lambda xs: max(enumerate(0),key=lambda x: x[1])[0] xs

def gauss(A, b):
  """
  Solves a system of linear equations Ax = b using the Gaussian elimination method.

  Args:
    A: The coefficient matrix.
    b: The constant vector.

  Returns:
    x: The solution vector.
  """
  # swap_for_max_pivot(A)

  n = len(b)
  # Forward elimination
  for i in range(n):
    # Divide the current row by the leading coefficient
    factor = A[i, i]
    A[i, :] /= factor
    b[i] /= factor
    # Eliminate coefficients except the diagonal
    assert A[i, i] == 1
    
    for j in range(n):
      if j == i:
        continue
      factor = A[j, i]
      
      A[j, :] -= factor * A[i, :]
      b[j] -= factor * b[i]

  return b

def swap_for_max_pivot (A):
  pass
  # for i in range(len(A)):
  #   max_pivot = index(max(A[:, i]))
    

# # Example usage:
# A = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
# # A.map(float)
# b = np.array([5.0, 6.0, 7.0])


# Get matrix dimensions from user
n = int(input("Enter the number of equations: "))
A = np.zeros((n, n))
b = np.zeros(n)

# Get matrix coefficients from user
print("Enter the coefficients of the matrix, row by row. Separate elements by spaces.")
for i in range(n):
  row = list(map(float, input(f"Enter row {i+1}: ").split()))
  A[i, :] = row

# Get constant vector from user
print("Enter the constants of the vector, separated by spaces.")
b = list(map(float, input().split()))
b = np.array(b)

# Solve the system of equations
x = gauss(A, b)
print("Solution:", x)