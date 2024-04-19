name = input("Como te llamas: ")

altura = input("Cual es tu altura (cm): ")
alt = float(altura)/100

peso = input("Cual es tu peso: ")

genero = input("Genero: ")

imc = round(float(peso)/((alt)*(alt)), 2)
print("Tu IMC es ", imc)