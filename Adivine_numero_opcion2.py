import random

counter = 0
num = random.randint(0, 100)
intento = 0
print(num)


try:
    intento = input("Introduce un numero entre 0 y 99: ")
    intento = int(intento)

except:
    print("Intentalo otra vez, sólo son validos los números entre 0 y 99")


while True:
    try:
        intento = input("Vuelve a intentarlo, es entre 0 y 99: ")
        intento = int(intento)

    except:
        print("Sólo son validos los números entre 0 y 99, ambos inclusives")
        intento = 0

    if 1 <= intento <= 99:
        counter += 1
        if intento == num:
            print("Has acertado!, es ", intento,
                  " Has necesitado ", counter, " intentos")
            break
        elif intento < num:
            print("Demasiado pequeño!")
        elif intento > num:
            print("Demasiado grande!")
    else:
        print("El número debe ser entre 0 y 99")
