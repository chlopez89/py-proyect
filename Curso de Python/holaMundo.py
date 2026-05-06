from datetime import datetime


MESES = {
    "enero": 1,
    "febrero": 2,
    "marzo": 3,
    "abril": 4,
    "mayo": 5,
    "junio": 6,
    "julio": 7,
    "agosto": 8,
    "septiembre": 9,
    "setiembre": 9,
    "octubre": 10,
    "noviembre": 11,
    "diciembre": 12,
}

MESES_ORDENADOS = [
    (1, "Enero"),
    (2, "Febrero"),
    (3, "Marzo"),
    (4, "Abril"),
    (5, "Mayo"),
    (6, "Junio"),
    (7, "Julio"),
    (8, "Agosto"),
    (9, "Septiembre"),
    (10, "Octubre"),
    (11, "Noviembre"),
    (12, "Diciembre"),
]


def obtener_numero_mes(mes_texto):
    mes_texto = mes_texto.strip().lower()
    if mes_texto.isdigit():
        numero = int(mes_texto)
        if 1 <= numero <= 12:
            return numero
        return None
    return MESES.get(mes_texto)


def presentacion():
    print("Hola Mundo")
    print("Bienvenido al curso de Python")
    nombreUsuario = input("¿Cuál es tu nombre? ")
    annoNacimiento = input("¿En qué año naciste? ")
    print("Selecciona el mes en que naciste:")
    for numero, nombre in MESES_ORDENADOS:
        print(f"  {numero:2d} - {nombre}")
    mesNacimiento = input("Mes (número o nombre): ")

    numero_mes = obtener_numero_mes(mesNacimiento)
    Hoy = datetime.now()

    if not annoNacimiento.isdigit():
        print("Por favor, ingresa un año de nacimiento válido.")
        return

    if numero_mes is None:
        print("Por favor, ingresa un mes de nacimiento válido (1-12 o nombre del mes).")
        return

    edad = Hoy.year - int(annoNacimiento)
    edad -= 1 if Hoy.month < numero_mes else 0

    if edad < 0:
        print("La fecha de nacimiento no puede ser en el futuro.")
    elif edad < 18:
        print("Por favor, eres menor de edad o no has ingresado un número válido.")
    else:
        print(f"Hola {nombreUsuario}, tienes {edad} años.")


presentacion()
print("fin del programa")