#  Esto es un comentario
# Docstring example

# 1.- Variables - convenciones
# snake_case
edad_total = 25
nombre = "Deimian"
# print(edad_total)
# print(type(nombre))

#----------------------------------------------------------
# 2.- Tipos de datos 

entero = 10                 # int
decimal = 10.5              # float
texto = "Hola"              # str
activo = True               # bool
lista = [1, 2, 3]           # list (mutable, ordenada) 
tupla = (1, 2, 3)           # tuple (inmutable, ordenada) 
diccionario = {"clave": "valor"}   # dict (mutable, desordenado)
conjunto = {1, 2, 3, 1}           # set (mutable, desordenado, sin elementos duplicados)
none = None                   # NoneType


# print(type(entero))
# print(type(decimal))
# print(type(texto))
# print(type(activo))
# print(type(lista))
# print(type(tupla))
# print(type(diccionario))
# print(type(conjunto))
# print(type(none))
# print(none)


# 2.1 -- strings

# cadena = "   Hola, mundo    "
# print(cadena[1])
# print(cadena[-1])  # Último carácter
# print(cadena[0:4])  # Subcadena "Hola"
# print(cadena[:4])   # Subcadena "Hola" (inicio implícito)
# print(cadena[7:])   # Subcadena "mundo" (fin implícito)

# print(cadena.upper())  # Convierte a mayúsculas
# print(cadena.lower())  # Convierte a minúsculas
# print(cadena.capitalize())  # Convierte la primera letra a mayúscula
# print(cadena.title())  # Convierte la primera letra de cada palabra a mayúscula
# print(cadena.strip())  # Elimina espacios en blanco al inicio y al final
# print(cadena.replace("Hola", "Adiós"))  # Reemplaza subcadenas
# print(cadena.split(","))  # Divide la cadena en una lista usando el separador ","

cadena_dos = "Hola"
cadena_tres = "Mundo"
nombre_dos = "Deimian"

# print(cadena_dos + " " + cadena_tres + " " + nombre_dos)
# print(f"{cadena_dos} {cadena_tres} {nombre_dos}") # format string

# print("{} {} {} {}".format(cadena_dos, "como estas", cadena_tres, nombre_dos)) # old style format string


numero_uno = 42
numero_dos = 53

# print(numero_uno + numero_dos)
# print(numero_uno - numero_dos)
# print(numero_uno * numero_dos)
# print(numero_uno / numero_dos)
# print(numero_uno // numero_dos)  # División entera
# print(numero_uno % numero_dos)   # Módulo (resto de la división)
# print(numero_uno ** numero_dos)  # Potencia
# print(3**3)


# ------------------------------------------------------------
# 7. Operadores de comparación
# ------------------------------------------------------------
x = 10
y = 20

# print("== Igual:", x == y)           # False
# print("!= Distinto:", x != y)        # True
# print(">  Mayor que:", x > y)        # False
# print("<  Menor que:", x < y)        # True
# print(">= Mayor o igual:", x >= 10)  # True
# print("<= Menor o igual:", y <= 20)  # True



# ------------------------------------------------------------
# 6. Operadores lógicos: and, or, not
# ------------------------------------------------------------
tiene_ticket = True
es_mayor = True
es_vip = False

# print("and (ambas True):", tiene_ticket and es_mayor)   # True
# print("or (al menos una True):", es_mayor or es_vip )    # True
# print("not (niega):", not es_vip)                       # True

# # Caso de clase: ¿puede entrar al concierto?
# puede_entrar = tiene_ticket and es_mayor
# print("¿Puede entrar?", puede_entrar)


# while True:
#     """
#     Bucle infinito que se ejecuta indefinidamente.
#     si quieres salir  marca el número 0
#     """

#     num = input("Ingresa un número (0 para salir): ")
#     if num == "0":
#         break



# Condicionales: if, elif, else

# edad = 17

# if edad < 18:
#     print("Es menor de edad")
# else:
#     print("Es mayor de edad")


# nota = 85

# if nota >=90:
#     print("Excelente")
# elif nota >= 80:
#     print("Muy bien")
# elif nota >= 50:
#     print("Suficiente")
# else:
#     print("Insuficiente")


edad_user = 17
tiene_licencia = True


# if edad_user >= 18:
#     if tiene_licencia:
#         print("Puede conducir")
#     else:
#         print("No tiene licencia")
# else:
#     print("Es menor de edad")

# if edad_user < 18:
#     print("NO puede conducir")
# elif tiene_licencia:
#     print("Puede conducir")
# else:
#     print("NO tiene licencia")


# usuarios de frontend

dicionario = {
    "id": 1,
    "username":"deimian",
    "email":None,
    "password":"123456"
}

users_db = "correo@example.com"

# # ------> None or {
#     "id": 1,
#     "username":"deimian",
#     "email":None,
#     "password":"123456" --> Encriptada --> lknfsokfposbfhoñsudbfosdbfop --> True or False
# }


# if users_db is not None:
#     print("Usuario encontrado:", users_db) # 30 lineas
    
# else:
#     print("No hay usuario en la base de datos") # una linea 


# list_name = ["Alice", "Bob", "Charlie"]

# if "Alice" in list_name:
#     print("Alice está en la lista")
# else:
#     print("Alice no está en la lista")


# contador_global = 100


# def mostrar_contador():
#     print(f"Contador global: {contador_global}")

# mostrar_contador()

# def ejemplo_local():
#     mensaje = "Hola, buenos días"
#     print(mensaje)

# ejemplo_local()

# def cambiar_contador():
#     global contador_global
#     contador_global += 1
#     print(f"Contador global modificado: {contador_global}")
    

# cambiar_contador()


# # pasar de str a num
# numero_str = "123"
# numero_int = int(numero_str)  # Convertir de str a int
# print(numero_int)  # Mostrar el número convertido


# num_int = 55
# num_str = str(num_int)  # Convertir de int a str
# num_float = float(num_int)  # Convertir de int a float
# print(num_int)
# print(num_str)  # Mostrar el número convertido a str
# print(num_float)  # Mostrar el número convertido a float


# num_uno = input("Ingresa un número: ")

# print(type(num_uno))

# num_uno = int(num_uno)
# print(type(num_uno))
# print(num_uno ** 3)