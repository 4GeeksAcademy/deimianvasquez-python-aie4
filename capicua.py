# Hacer un código donde diga si un número es capicúa

# Ejemplo
# 121 
# 12321
# "oso"

while True:
    try:
        print("""
            1.- Capicúa
            0.- Salir
            """)
        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            texto = input("Ingresa un número a evaluar: ")

            if type(texto) == "str": 
                print("Ingresa un número valido (Solo numeros)")
                continue

            
            invertido = texto[::-1]

            if texto == invertido:
                print("Si es capicúa")
            else:
                print("NO es ")
        else:
            print("Gracias por su visita")
            break

    except as exception:
        print("Debe ser un número valido")