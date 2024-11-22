from itertools import count

def reverse (xs):
  ys = []
  while xs:
    x = xs[0]
    xs = xs [1:]
    ys = [x] + ys
  return ys

# if __name__ == "__main__":
xs = [1,2,3,4,5,6,7,8,9,10]
print(f"reverse {xs} = {reverse(xs)}")

is_palindrome = lambda xs: xs == reverse(xs)

print (is_palindrome (xs), is_palindrome(xs + reverse (xs)))

def primes():
  nums = []
  for n in count(2):  #range(2, 99999)
    for i in nums:
      if (n % i) == 0:
        break
    else:
      nums.append(n)
      yield n

prime_nums = primes()
for _ in range(10):
  print(next(prime_nums), end=" ")
print()

#Nat -> [Nat]
def prime_decompose (n):
  primes_ = primes()
  i = next(primes_)
  while n != 1:
    if n % i == 0:
      n//= i
      yield i
    else:
      i = next(primes_)
        
prime_nums = primes()
for i in prime_decompose (6):
  print(i, end=" ")