def isort (list_of_dict, key):
  new_list = []
  
  for dict in list_of_dict:
    left = 0
    right = len(new_list)
    while left < right:
      mid = (left + right) // 2
      if dict[key] > new_list[mid][key]:
        left = mid + 1
      else:
        right = mid
    new_list.insert(left, dict)
  return new_list

patients = [
    {"name": "John", "surname": "Doe", "illness": "Flu"},
    {"name": "David", "surname": "Copperfield", "illness": "Migraine"},
    {"name": "Jane", "surname": "Doe", "illness": "Cold"},
    {"name": "Charlie", "surname": "Brown", "illness": "Allergies"},
    {"name": "Frank", "surname": "Sinatra", "illness": "Bronchitis"},
    {"name": "Peter", "surname": "Pan", "illness": "Chickenpox"},
    {"name": "Emily", "surname": "Dickinson", "illness": "Asthma"},
    {"name": "Alice", "surname": "Wonderland", "illness": "Common Cold"},
    {"name": "Bob", "surname": "Builder", "illness": "Pneumonia"},
    {"name": "Grace", "surname": "Kelly", "illness": "Sinusitis"},
]

sorted_by_name = isort(patients, 'name')
print("Отсортировано по имени:")
for client in sorted_by_name:
  print(client)
sorted_by_last_name = isort(patients, 'surname')
print("\nОтсортировано по фамилии:")
for client in sorted_by_last_name:
  print(client)