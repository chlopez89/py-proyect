name = "Christian"
last_name = "Perez"
my_age = 34
print("V3")
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

quote = "I'm Christian "
print(quote)

quote_2 = '->She said "Hello"'
print(quote_2)

# format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name

print(template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)

print("v4", template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"

print("v5", template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name} y mi edad es {my_age} años"

print("v6", template)
