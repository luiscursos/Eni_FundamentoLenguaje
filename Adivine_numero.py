import random

counter = 0
num = random.randint(0,100)
print(num)

while True:
    try:
        user=int(input("Introduce un numero entre 0 y 99: "))
        counter +=1
        
    except:
        print("Intentalo otra vez, sólo son validos los números entre 0 y 99")
    
    else:
        if user == num:
            print("Has acertado!, es ", user, " Has necesitado ",counter, " intentos")
            break
        if 1 <= user <= 99:
            if user < num:
                print("Vuelve a intentarlo te has quedado corto")
            elif user > num:
                print("Vuelve a intentarlo te has pasado")
        else:
            print("El numero debe ser entre 0 y 99")


    

