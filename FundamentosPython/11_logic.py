# and
print('AND')
print('True and True =>', True and True)
print('True and False =>', True and False)
print('False and True =>', False and True)
print('False and False =>', False and False)

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

stock = input('Ingrese el numero de stock => ')
stock = int(stock)

print(stock >= 100 and stock <= 1000)

print('OR')
print('True or True =>', True or True)
print('True or False =>', True or False)
print('False or True =>', False or True)
print('False or False =>', False or False, '\n')

role = input('Digita el rol => ')

if (role == 'admin' or role == 'seller'):
  print(f'El rol {role} es valido', '\n')
  print(f'Puede ingresar al sistema como {role} ==>')
else:
  print(f'El rol {role} no es valido')
