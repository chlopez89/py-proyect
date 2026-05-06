from datetime import datetime


def presentacion():
    print("Hola Mundo")
    print("Bienvenido al curso de Python")
    nombreUsuario=input("¿Cuál es tu nombre? ")
    annoNacimiento=input("¿En que año naciste? ")
    mesNacimiento=input("¿En que mes naciste?(ingresa el numero de mes) ")
    Hoy=datetime.now()
    if annoNacimiento.isdigit() and mesNacimiento.isdigit():
        edad = Hoy.year - int(annoNacimiento)
        edad -= 1 if (Hoy.month, Hoy.day) < (int(mesNacimiento), 1) else 0
        if edad < 18:
            print("Por favor, eres menor de edad o no has ingresado un número válido.")
        else:
            print(f"Hola {nombreUsuario}, tienes {edad} años.")
    else:
        print("Por favor, ingresa un año de nacimiento válido.")

presentacion()
print(f"fin del programa")