# Definimos las duncionalidades

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: no se puede dividir entre 0"

# Mostrando las opciones

print("Bienvenidos a la calculadora de python. Elija un número asociado a una operación para continuar: ")
print("1. sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

# Selección de operación

opcion = int(input("seleccione una opción del 1 al 4: "))

# Selección de números

numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese un número: "))

# Lógica

if opcion == 1:
    resultado = suma(numero1, numero2)

elif opcion == 2:
    resultado = resta(numero1, numero2)

elif opcion == 3:
    resultado = multiplicar(numero1, numero2)

elif opcion == 4:
    resultado = division(numero1, numero2)

else:
    resultado = "Opción no valida"

# Mostramos el resultado

print("El resultaido de su operación es:", resultado)