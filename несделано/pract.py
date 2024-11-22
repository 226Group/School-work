def quicksort_by_key(dict, key):
  if len(dict) <= 1:
      return dict
  pivot = dict[len(dict) // 2]
  left = [patient for patient in dict if patient[key] < pivot[key]]
  middle = [patient for patient in dict if patient[key] == pivot[key]]
  right = [patient for patient in dict if patient[key] > pivot[key]]

  return quicksort_by_key(left, key) + middle + quicksort_by_key(right, key)
  
clients = [
  {'Имя': 'Тимофей', 'Фамилия': 'Антонов', 'Дата рождения': '2007-13-12'},
  {'Имя': 'Максим', 'Фамилия': 'Растер', 'Дата рождения': '1985-05-15'},
  {'Имя': 'Алексей', 'Фамилия': 'Сисадминов', 'Дата рождения': '1992-07-20'},
  {'Имя': 'Дмитрий', 'Фамилия': 'Сисадминов', 'Дата рождения': '1992-07-20'}
]
sorted_by_name = quicksort_by_key(clients, 'Имя')
print("Отсортировано по имени:")
for client in sorted_by_name:
  print(client)
sorted_by_last_name = quicksort_by_key(clients, 'Фамилия')
print("\nОтсортировано по фамилии:")
for client in sorted_by_last_name:
  print(client)


















# "Password"
# while True:
# L = str(input("gute norme: "))
# if 11:
# pu= str(input("Beegete napota: "))
# рас pac
# str(input("Введите список пациентов. Улданные 1 пациента разделяется запятой с пробелом. Унпациенты разделяется между собой точкой с запятой. ("))
# pac.split(":")
# for i in range(len(pac)):
# pac[j] = pac[i].split(", ")
# for i in range(len(pac)):
# pac[1].insert(0, 1 • 1)
# print(pac)
# white Truel
# == int(input("Begate Home Recrean;\n"
# *3 отсортирвать списока"
# if n < 1 or 4:
# print("Degrees.")
# continue
# elif 1
# pa = str(input("Bergete gamme zagresta sepez, zanaty © agodenam: "))
# papa.split(", ")
# pa.insert(x 0, Jen(pac) + 1)
# pac.append(g)
# continue
# elif** 21
# nomint(input("Berarte Home pure A Y: "))
# try:
# pac.pop(non-1)
# for i in range(nom - 1, len(pac)):
# pac[i][0] = 1.1
# print(pac)
# except IndexError:
# print("Ошибка! Введено несуществующее значение")
# elif ** 31
# pointinout("Beate chocos cooтMoon"
# AS 42 168 +"""