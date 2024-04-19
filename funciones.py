# 1.- Funciones sin argumentos y sin retorno
# Creamos la función
def saludar():
    print("Hola")
# Llamos a la función
saludar()

# 2.- Funciones con argumentos pero sin retorno

def sumar(a, b):
    resultado = a + b
    print("El resultado de la suma es:", resultado)

sumar(6, 9)

# 3.- Funciones con argumento y con retorno

def multiplicar(a, b):
    return a * b

resultado = multiplicar(9, 8)
print("El resultado de la multiplicacion es:", resultado)

# 4.- Funciones con argumentos predeterminados

def saludar(nombre = "Usuario"):
    print("Hola", nombre)

saludar()
saludar("Juan")