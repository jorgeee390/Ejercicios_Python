# Solicitamos la edad

edad = int(input("Por favor, ingrese su edad: "))

#Verifica la edad

if edad < 18:
    print("Usted es menor de edad")
else:
    print("Usted es mayor de edad")

# realizamos la calculadora

if edad >=18:
    nombre = input("Introduce su nombre: ")
    #confirmacion = 
    altura = float(input("Introduce su altua (m): "))
    peso = float(input("Introduce tu peso (KG): "))
    IMC = round(peso/(altura**2), 2)
    print(nombre, "tu IMC es de:", IMC)

    if IMC < 15.99:
        print("Delgadez severa")

    elif 16 <= IMC <= 16.99:
        print("Delgadez moderada")

    elif 17 <= IMC <= 18.49:
        print("Delgadez aceptada")

    elif 18.5 <= IMC <= 24.99:
        print("Peso normal")

    elif 25 <= IMC <= 29.99:
        print("Sobre peso")

    elif 30 <= IMC <= 34.99:
        print("Obesidad tipo 1")

    elif 35 <= IMC <= 39.99:
        print("Obesidad tipo 2")

    elif 40 <= IMC <= 49.99:
        print("Obesidad tipo 3")

    else:
        print("Obesidad tipo 4 o extrema")
