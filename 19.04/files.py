import itertools

folder = "19.04"
def print_gen(generator):
  for i in generator:
    print(i)
    
def read_lines(filename):
  with open(folder+'/'+filename, "r") as file:
    for line in file.readlines():
      yield line.rstrip() #[:-1]
    
print ("20.")

def write_lines(filename, lines):
  with open(folder+"/"+filename, "w") as file:
    file.writelines(lines)
write_lines("file1", """Hello
World""")

print_gen(read_lines("file1"))

print ("19.")

write_lines("file2",
"""Hello
This
World
""")

def compare_files(file1, file2):
    lines1 = read_lines(file1)
    lines2 = read_lines(file2)
    for i, (line1, line2) in enumerate(itertools.zip_longest(lines1, lines2)):
      if line1 != line2:
        print(f"{i + 1})")
        print(f"  File 1: {line1.rstrip() if line1 else '(empty)'}")
        print(f"  File 2: {line2.rstrip() if line2 else '(empty)'}")

compare_files("file1", "file2")

print ("18.")

lines = list (read_lines("files.py")) [:7]
for i, line in enumerate(lines):
  print(f"{i+1} | {line}")
