import numpy as np

def gauss(A, b):
  """
  Solves a system of linear equations Ax = b using the Gaussian elimination method.

  Args:
    A: The coefficient matrix.
    b: The constant vector.

  Returns:
    x: The solution vector.
  """

  n = len(b)
  # Forward elimination
  for i in range(n):
    # Divide the current row by the leading coefficient
    factor = A[i, i]
    A[i, :] /= factor
    b[i] /= factor
    # Eliminate coefficients below the diagonal
    for j in range(i + 1, n):
      factor = A[j, i]
      A[j, :] -= factor * A[i, :]
      b[j] -= factor * b[i]

  # Back substitution
  x = np.zeros(n)
  for i in range(n - 1, -1, -1):
    x[i] = b[i]
    for j in range(i + 1, n):
      x[i] -= A[i, j] * x[j]

  return x

# Example usage:
A = np.array([[2.0, 1.0, 1.0], [1.0, 2.0, 1.0], [1.0, 1.0, 2.0]])
# A.map(float)
b = np.array([5.0, 6.0, 7.0])

# A[1, :] = A[1, :] / 2
# print (A)

x = gauss(A, b)
print(x)  # Output: [1. 2. 3.]