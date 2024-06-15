'''
for element in range(1, 21):
  print(element)

'''

my_list = [23, 45, 67, 89, 43, 80, 22, 94]
for element in my_list:
  if int(element) % 2 == 0:
    print(f"el elemento: {element} es par")
  else:
    print(f"el elemento: {element} es impar")

my_tuple = ('nico', 'juli', 'santi')
for element in my_tuple:
  print(element)

product = {'name': 'Camisa', 'price': 100, 'stock': 89}

for key in product:
  print(key, '=>', product[key])

print("===== Key and Value =====")
for key, value in product.items():
  print(key, '=>', value, '\n')

print("===== People =====")
people = [{
    'name': 'nico',
    'age': 34
}, {
    'name': 'zule',
    'age': 45
}, {
    'name': 'santi',
    'age': 4
}]

for person in people:
  print('name =>', person['name'])
