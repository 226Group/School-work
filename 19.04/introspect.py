# from inspect import getmembers, ismethod
# import inspect
class Class:
  def method ():
    print ("method")

print (globals())
# создаем всем методам копию-функцию:
modules = (module)
methods = {}
for name, obj in getmembers(globals()):
  if obj.__class__ == Class.__class__:
    print(name)
    methods[name] = obj
print(methods)

folder = "19.04"
def print_gen(generator):
  for i in generator:
    print(i)



def read_lines(filename):
  for line in open(folder+'/'+filename, "r").readlines():
    yield line[:-1]
    
print ("20.")

def write_lines(filename, lines):
    with open(folder+"/"+filename, "w") as file:
        file.writelines(lines)
write_lines("file1", "Hello\nWorld\n")

print_gen(read_lines("file1"))

print ("19.")

write_lines("file2",
"""Hello
This
World""")


# def compare_files(file1, file2):
#   #match : Eq a; [a], [a] -> [(a, a)], [a], [a]
#   def match(xs, ys):
#     res = []
#     while True:
#       x = xs.next()
#       y = ys.next()
#       if x == y:
#         res.append ((x, y))
#       else:
#         break
#     return (res, xs, ys)
#   def compare_strings(old, new):  #: [String], [String] -> String
#     # rstrip
#     old = map (rstrip, old)
#     new = map (rstrip, new)
    
#   with open(file1, "r") as f1, open(file2, "r") as f2:
#     lines1 = f1.readlines()
#     lines2 = f2.readlines()
#     old = enumerate(lines1, 1)
#     new = enumerate(lines2, 1)
                   
#     print(compare_strings(old, new))

# print(compare_files("file1", "file2"))




print (globals()["A"])
print(read_lines.__class__)
print(A.method.__class__)


