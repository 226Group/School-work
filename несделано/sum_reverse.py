#124 Количество разложения числа на слогаемые

#splits : Nat -> {[Nat]}
  
# def add_gen (gen, x):
#   yield x
#   for i in gen:
#     yield i
    
# def nat_sum_reverse(n):
#   if n == 0:
#    return [[0]]
#   elif n == 1:
#     return [[1]]
  
#   splits = nat_sum_reverse(n-1)
#   for split in splits:
#     split = split + [0]  #important!
#     for i in range(0, len(split)):
#       res = split[:]
#       res[i] += 1
#       yield res
    

# def show_gen(gen):
#   for i in gen:
#     print (i)

# for i in range (5):
#   splits = list(nat_sum_reverse(i))
#   print (i, len(splits))
#   print(splits)
#   print()

# (m>=n) => (n:Nat) -> (m:Nat) -> [Nat](sum = n) -> [Nat](sum = m)
def transform (n, m, xs):
  dif = m - n
  return xs + [dif]


def nat_set_sum_reverse(m):

    # базовый случай

    if m == 1:
        return [[1]]

    partitions = [[]] #[[m]] #[[Nat]]

    for n in range(1, m):
      # print(i)
      # count += nat_set_sum_reverse(i)
      partitions+= (transform (n, m, xs) for xs in nat_set_sum_reverse(n))
        

    return partitions


def nat_set_sum_reverse_ (m):
  
  # базовый случай
  
  if m == 0:
      return []
  
  partitions = [[]] #[[Nat]]
  
  for n in range(1, m+1):
    
    dif = m-n
    partitions+= (xs + [dif] for xs in nat_set_sum_reverse(m - n))
  
  
  return partitions
  
  #sum $ map (\i -> count_sum(n - i)) [1..n-1]
  #sum $ map (\i -> (n - i)) [1..n]  
  
# основная программа

N = int(input())

count = nat_set_sum_reverse_(N)

print (count)