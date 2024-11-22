import py16_02

print ("6. Обработка строк")

s = input(">")
print(len(s))
print(s[::-1])


def is_palindrome(s):
  return s == s[::-1]

print(f"Is a string palindrome? {is_palindrome(s)}")

print("5. Проверка на простоту")
xs = list(py16_02.prime_decompose(int(input(">"))))
print(xs)
if len(xs) == 1:
  print("Простое")
else:
  print("Составное")

print("5. Факториал")

def factorial (n):
  if n == 0:
    return 1
  return n * factorial(n-1)
  
n = int(input(">"))
print (factorial(n))
