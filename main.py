import subprocess


#запускаем нужный скрипт
def run (name):
  subprocess.run(["python", name + ".py"])
  # os.system(f"python3 -i {name}.py")


# run ("19.04/files")
# run ("мальтус")
run ("регулярки_24.01")