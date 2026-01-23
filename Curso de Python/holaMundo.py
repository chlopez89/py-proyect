def presentacion():
    print("Hola Mundo")
    print("Bienvenido al curso de Python")
    Nombre=input("¿Cuál es tu nombre? ")
    Edad=input("¿Cuántos años tienes? ")
    if Edad.isdigit() and int(Edad) < 18:
        print("Por favor, eres menor de edad o no has ingresado un número válido.")
    else:
        print(f"Hola {Nombre}, tienes {Edad} años.")

presentacion()
print(f"fin del programa")