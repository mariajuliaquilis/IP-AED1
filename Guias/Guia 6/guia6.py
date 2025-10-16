import math

#Ejercicio 1. 
#punto 1:
def imprimir_hola_mundo():
    print("¡Hola mundo!")

imprimir_hola_mundo()

#punto 2:
def imprimir_un_verso():
    print("aaaaa \naaaaa")

imprimir_un_verso()

#punto 3:
def raizDe2()->float:
    return round(math.sqrt(2), 4)

print(raizDe2())

#punto 4:
def factorial_de_dos()->int:
    return math.factorial(2)

print(factorial_de_dos())
  
#punto 5:
def perimetro()->float:
    return 2*(math.pi)

print(perimetro())

#Ejercicio 2.
#punto 1:
def imprimir_saludo(nombre: str): 
    print("¡Hola " + nombre + "!")

imprimir_saludo("María Julia")

#punto 2:
def raiz_cuadrada_de(numero:int)->float:
    return math.sqrt(numero)

print(raiz_cuadrada_de(5))

#punto 3:
def fahrenheit_a_celsius(temp_far: float)->float:
    return ((temp_far - 32)*5)/9

print(fahrenheit_a_celsius(88.0))

#punto 4
def imprimir_dos_veces(estribillo: str):
    print(2 * estribillo)

imprimir_dos_veces("abc")

#punto 5                       
def es_multiplo_de(n: int, m: int)->bool:
    return n % m == 0

#punto 6
def es_par(numero: int)->bool:
    return es_multiplo_de(numero, 2)

#punto 7
def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int)->int:
    return math.ceil((comensales*min_cant_de_porciones)/8)

#Ejercicio 3.
#punto 1 
def alguno_es_0(numero1: float, numero2: float)->bool:
    return numero1 == 0 or numero2 == 0

#punto 2
def ambos_son_0(numero1: float, numero2: float)->bool:
    return numero1 == 0 and numero2 == 0

#punto 3
def es_nombre_largo(nombre: str)->bool:
    return 3 <= len(nombre) and len(nombre) <= 8 

#punto 4
def es_bisiesto(año: int)->bool:
    return es_multiplo_de(año, 400) or (es_multiplo_de(año, 4) and not(es_multiplo_de (año, 100)))

#Ejercicio 4.
#punto 1
def peso_pino(altura: int)-> int:
    peso_kg = 0
    for num in range(1, altura+1, 1):
        if num <= 3:
            peso_kg = num*100*3
        else:
            primeros_tres_metros = 3
            diferencia = (altura-primeros_tres_metros)
            peso_kg = primeros_tres_metros*100*3 + diferencia*100*2
    return peso_kg

#punto 2
def es_peso_util(peso: int)->bool:
    return peso >= 400 and peso <= 1000

#punto 3 y 4
def sirve_pino(metros: int)->bool:
    return es_peso_util(peso_pino(metros))

#Ejercicio 5.
#punto 1
def devolver_el_doble_si_es_par(numero: int)->int:
    if numero % 2 == 0:
        return numero*2
    else:
        return numero

#punto 2
def devolver_valor_si_es_par_sino_el_que_sigue(numero: int)-> int:
    if numero % 2 != 0:
        return numero+1
    else:
        return numero

#punto 3
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int)->int:
    if numero % 3 == 0:
        return numero*2
    elif numero % 9 == 0:
        return numero*3
    else:
        return numero

#punto 4
def lindo_nombre(nombre: str)->str:
    if len(nombre) >= 5:
        return "Tu nombre tiene muchas letras!"
    else:
        return "Tu nombre tiene menos de 5 caracteres"

#punto 5
def elRango(numero: int):
    if numero < 5:
        print("El número es menor a 5")
    elif numero >= 10 and numero <= 20:
        print("Entre 10 y 20")
    else:
        print("Mayor a 20")

elRango(4)
elRango(12)
elRango(40)

#punto 6
def te_toca_trabajar(sexo: str, edad: int)->str:
    if((sexo == "F" and (edad >= 60 or edad < 18)) or (sexo == "M" and (edad >= 65 or edad < 18))):
        return "Andá de vacaciones"
    else:
        return "Te toca trabajar"

#Ejercicio 6
#punto 1
def imprimir_numeros_del_1_al_10():
    indice = 1
    while indice <=10:
        print(indice)
        indice +=1

imprimir_numeros_del_1_al_10()

#punto 2
def imprimir_numeros_pares_entre_10_y_40():
    indice = 10
    while indice <= 40:
        if indice % 2 == 0:
            print(indice)
            indice+=1
        else:
            indice+=1

imprimir_numeros_pares_entre_10_y_40()

#punto 3
def imprimir_eco_10_veces():
    indice = 1
    while indice <=10:
        print("eco")
        indice+=1

imprimir_eco_10_veces()

#punto 4
def cuenta_regresiva(numero: int):
    while numero >= 1:
        print(numero)
        numero-=1
    print("Despegue!")

cuenta_regresiva(7)

#punto 5
def viaje_en_el_tiempo(partida: int, llegada: int):
    while partida >= llegada:
        print("Viajó un año al pasado, estamos en el año: " + str(partida))
        partida-=1

viaje_en_el_tiempo(2025, 2020)

#punto 6
def conocer_a_Aristoteles(partida: int):
    while partida >= -384:
        print("Viajó veinte años al pasado, estamos en el año: " + str(partida))
        partida-=20

conocer_a_Aristoteles(80)

#Ejercicio 7
#punto 1
def imprimir_numeros_del_1_al_10_ej_7():
    for num in range(1,11,1):
        print(num)

imprimir_numeros_del_1_al_10_ej_7()

#punto 2
def imprimir_numeros_pares_entre_10_y_40_ej_7():
    for num in range(10, 41, 1):
        if num % 2 == 0:
            print(num)

imprimir_numeros_pares_entre_10_y_40_ej_7()

#punto 3
def imprimir_eco_10_veces_ej_7():
    for num in range(1,11,1):
        print("eco")

imprimir_eco_10_veces_ej_7()

#punto 4
def cuenta_regresiva_ej_7(numero: int):
    for num in range(numero, 0, -1):
        print(num)
    print("Despegue!")

cuenta_regresiva_ej_7(5)

#punto 5
def viaje_en_el_tiempo_ej_7(partida: int, llegada: int):
    for num in range(partida, llegada -1, -1):
        print("Viajó un año al pasado, estamos en el año: " + str(num))

viaje_en_el_tiempo_ej_7(2025, 2020)

#punto 6
def conocer_a_Aristoteles_ej_7(partida: int):
    for num in range(partida, -384, -20):
        print("Viajó veinte años al pasado, estamos en el año: " + str(num))

conocer_a_Aristoteles_ej_7(79)