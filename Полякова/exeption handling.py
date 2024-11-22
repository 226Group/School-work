# 16.3.* Напишите пользовательскую функцию avg(x, y), которая должна принимать в качестве аргументов два положительных целых или вещественных числа, а возвращать их среднее геометрическое (z = pow(x*y, 0.5)). В случае передачи недопустимых значений функция должна возбуждать исключение ValueError. После того, как функция будет готова, используйте ее в скрипте, который будет запрашивать у пользователя два числа, обрабатывать ввод и выдавать либо среднее геометрическое чисел, либо сообщение об ошибке. Для решения задачи используйте в теле функции инструкцию raise, а в скрипте try/except. 


def geom_avg(x, y):
  if x < 0 or y < 0:
    raise ValueError ("X and Y must be non-negative")
  return pow(x * y, 0.5)

x = int (input("Enter x: "))
y = int (input("Enter y: "))

try:
  result = geom_avg(x, y)
except ValueError as e:
  print(e)
else:
  print(f"Geometric avg of {x} and {y} is {result}")

# 16.2.* Напишите пользовательскую функцию write_file(f_obj, s), которая должна принимать в качестве аргумента объект открытого файла f_obj и пытаться записать в него строку s. В случае успешного завершения операции функция должна выводить на экран сообщение «Файл записан!». В противном случае должно выводиться соответствующее сообщение об ошибке. При любом исходе функция должна закрывать файловый объект перед завершением вызова и выводить сообщение «Файл закрыт!». Проверьте работу функции. Для этого создайте в папке скрипта пустой файл nums.py и запишите туда строку '1 2 3'. Далее откройте файл на чтение и попытайтесь записать в него строку '4 5 6'. Для решения задачи используйте в теле функции полную инструкцию try/except/else/finally. 

def write_file(f_obj, s):
  try:
    f_obj.write(s)
    print("Файл записан!")
  except Exception as e:
    print(f"Ошибка записи: {e}")
  finally:
    f_obj.close()
    print("Файл закрыт!")

with open("nums.py", "w") as f:
  write_file(f, "1 2 3")

with open("nums.py", "r") as f:
  write_file(f, "4 5 6")



# 16.1.* Напишите пользовательскую функцию pow3_func(x), которая должна принимать в качестве аргумента число x и возводить его в куб. В случае успешных вычислений функция должна выводить на экран сообщение в формате «x^3 = res» и возвращать res. В противном случае должно выводиться соответствующее сообщение об ошибке и возвращаться None. Проверьте функцию, вызвав ее с аргументами 5 и '5'.
print ("16.1.")

def pow3_func(x):
    try:
        res = x**3
        print(f"{x}^3 = {res}")
        return res
    except:
        print("Incorrect input")
        return None

print (pow3_func(5))
print (pow3_func('5'))




# 16.4.* Не используя возможности модуля abc стандартной библиотеки, создайте абстрактный класс геометрической фигуры Shape с конструктором, принимающим длину стороны и высоту, проведенную к этой стороне. Определите в классе абстрактный метод area(), который будет использоваться подклассами для расчета площади соответствующих им геометрических фигур. Для реализации абстрактности метода используйте возбуждение исключения NotImplementedError. Далее создайте классы Triangle и Rectangle, наследующие суперкласс Shape и реализующие его абстрактный метод под свои нужды. Продемонстрируйте использование созданных классов для нахождения площади треугольника и прямоугольника по известным значениям длины стороны и высоты, проведенной к этой стороне. Закомментируйте в одном из классов переопределяемый метод area(), использовав вместо него инструкцию pass, и повторно запустите скрипт. Объясните результат. Еще раз посмотрите решение задачи 13.11.
print ("16.4.")
class Shape:
  def __init__(self, side, height):
    if side <= 0 or height <= 0:
      raise ValueError("Side and height must be positive")
    self.side = side
    self.height = height
  def area(self):
    raise NotImplementedError()

class Triangle(Shape):
  def area(self):
    return 0.5 * self.side * self.height
class Rectangle(Shape):
  def area(self):
    return self.side * self.height

# Test Shape (abstract class)
try:
  shape = Shape(10, 5)
  print(f"Shape area: {shape.area()}")
except NotImplementedError as e:
  print(e)
# Test Triangle
triangle = Triangle(10, 5)
print(f"Triangle area: {triangle.area()}")
# Test Rectangle
rectangle = Rectangle(10, 5)
print(f"Rectangle area: {rectangle.area()}")