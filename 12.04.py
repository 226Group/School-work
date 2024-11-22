print ("стр 38 №3")
#3. Известны данные о количестве мальчиков и девочек в нескольких классах. Отсортировать названия классов по возрастанию процента мальчиков, определить количество классов, к которых мальчиков больше, чем девочек и вывести названия этих классов отдельно.

classes = [  #1 мальчики, 2 девочки
  ["1А", 10, 12],
  ["2Б", 14, 10],
  ["3В", 15, 9],
  ["4Г", 18, 7],
  ["5Д", 16, 8],
]
people = lambda class_data: class_data[1] + class_data[2]

sorted_classes = sorted(classes, key=lambda class_data: class_data[1] / people (class_data))

classes_with_more_boys = [class_data[0] for class_data in classes if class_data[1] > class_data[2]]

print("Sorted classes by percentage of boys:")
print (sorted_classes)

print(f"\nClasses where the number of boys is greater than the number of girls: {classes_with_more_boys}")
print(f"Таких классов {len(sorted_classes)} штук")




print ("стр 38 №4")
# 4. Решить задачу, связанную с оценкой экономической деятельности группы предприятий на основе известных данных.
enterprises = [
  ["Предприятие 1", 100, 90],
  ["Предприятие 2", 200, 180],
  ["Предприятие 3", 300, 270],
  ["Предприятие 4", 400, 390],
  ["Предприятие 5", 500, 450]]

plan_percent = {}
print('Процент выполнения плана каждым предприятием:')
for enterprise in enterprises:
  percent = enterprise[2] / enterprise[1] * 100
  plan_percent[enterprise[0]] = percent
print (plan_percent)

num_underperformed = 0
for enterprise in plan_percent.items():
  if enterprise[1] <= 90:
    num_underperformed += 1
print(f'Количество недовыполнивших план на 10% и более: {num_underperformed}')

min_plan = min(enterprise[1] for enterprise in enterprises)
print(f'Наименьший плановый товарооборот: {min_plan}')

print('Предприятия, упорядоченные по убыванию планового товарооборота:')
enterprises.sort(key=lambda enterprise: enterprise[1], reverse=True)
print (enterprises)
