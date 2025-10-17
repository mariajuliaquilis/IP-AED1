import math

#RECORRIDO Y BÚSQUEDA EN SECUENCIAS

#Ejercicio 1:
def pertenece_while(s: list[int], e:int)->bool:
    indice = 0
    while indice < len(s):
         if s[indice] != e:
              indice += 1
         else:
              return True
    return False 

def pertenece_for(s:list[int], e:int)->bool:
     for indice in range (len(s)):
          if s[indice] == e:
               return True
     return False
          
#Ejercicio 2:
def divide_a_todos(s: list[int], e: int)->bool:
     indice = 0
     while indice < len(s):
          if(s[indice] % e != 0):
               return False
          else:
               indice += 1
     return True

#Ejercicio 3:
def suma_total(s: list[int])->int:
     suma = 0
     for i in range(len(s)):
          suma += s[i]
     return suma

#Ejercicio 4:
def maximo(s: list[int])->int:
     indice = 0
     numeroMasGrande = s[indice]
     while indice < len(s):
          if numeroMasGrande < s[indice]:
               numeroMasGrande = s[indice]
               indice += 1
          else:
               indice += 1
     return numeroMasGrande
               
#Ejercicio 5:
def minimo(s: list[int])->int:
     indice = 0
     numeroMasChico = s[indice]
     while indice < len(s):
          if numeroMasChico > s[indice]:
               numeroMasChico = s[indice]
               indice += 1
          else:
               indice += 1
     return numeroMasChico

#Ejercicio 6:
def ordenados(s: list[int])->bool:
     for i in range(len(s)-1):
          if(s[i] >= s[i+1]):
               return False
     return True

#Ejercicio 7:
def pos_maximo(s: list[int])->int:
     for i in range(len(s)):
          if s[i] == maximo(s):
               return i
     return -1
          
#Ejercicio 8:
def pos_minimo(s: list[int])->int:
     indice = len(s)-1
     while indice >= 0:
          if s[indice] == minimo(s):
               return indice
          else:
               indice -=1
     return -1

#Ejercicio 9:
def long_mayorASiete(s: str)->bool:
     indice = 0
     while indice < len(s):
          if(len(s[indice]) > 7):
               return True
          else:
               indice +=1
     return False
     
#Ejercicio 10:
def es_palindroma(s: str)->bool:
     indice = 0
     final = len(s)-1
     while indice <= final:
          if s[indice] == s[final]:
               indice+=1
               final-=1
          else:
               return False
     return True

#Ejercicio 11:
def iguales_consecutivos(s: list[int])->bool:
     for i in range(len(s)-2):
          if(s[i] == s[i+1] and s[i+1] == s[i+2]):
               return True
     return False

#Ejercicio 12:
#HACERLO

#Ejercicio 13:
#HACERLO

#Ejercicio 14:
#HACERLO



#RECORRIDO: FILTRANDO, MODIFICANDO Y PROCESANDO SECUENCIAS
#Ejercicio 2. Implementar las siguientes funciones sobre secuencias pasadas por parámetro

#punto 1)
def CerosEnPosicionesPares(s: list[int])-> None:
     for i in range (len(s)):
          if i % 2 == 0:
               s[i] = 0

lista_1 = [1,2,3,4]
lista_2 = []
lista_3 = [1,2,3]
CerosEnPosicionesPares(lista_1)
CerosEnPosicionesPares(lista_2)
CerosEnPosicionesPares(lista_3)
print(lista_1)
print(lista_2)
print(lista_3)

#punto 2)
def CerosEnPosicionesPares2(s: list[int])->list[int]:
     res: list[int] = []
     for i in range(len(s)):
          if i % 2 == 0:
               res.append(0)
          else:
               res.append(s[i])
     return res

#punto 3) 
#seq<Char> = str
def sin_vocales(s:str)->str:
     res: str = ""
     for i in range(len(s)):
          if s[i] != "a" and s[i] != "e" and s[i] != "i" and s[i] != "o" and s[i] != "u":
               res+=(s[i])
     return res

palabra = "hola"
print(sin_vocales(palabra))

#punto 4)
def reemplaza_vocales(s: str)->str:
     res: str = ""
     for i in range(len(s)):
          if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
               res+="_"
          else:
               res+=s[i]
     return res

palabra = "hola"
print(reemplaza_vocales(palabra))

#punto 5)
def da_vuelta_str(s:str)->str:
     res: str = ""
     for i in range(len(s)-1, -1, -1):
          res+=s[i]
     return res

palabra = "hola"
print(da_vuelta_str(palabra))

#punto 6)
#HACERLO


#EJERCICIO 3
def promedio(notas: list[int])->int:
     suma: int = 0
     for i in range(len(notas)):
          suma+=notas[i]
     return suma/(len(notas))

def son_mayores_a_4(notas: list[int])->bool:
     for i in range(len(notas)):
          if notas[i] < 4:
               return False
     return True

def resultado_materia(notas: list[int])->int:
     res: int = 0
     for i in range(len(notas)):
          if son_mayores_a_4(notas) and promedio(notas) >= 7:
               res = 1
          elif son_mayores_a_4(notas) and (promedio(notas) >= 4 and promedio(notas) < 7):
               res = 2
          else:
               res = 3
     return res

notas_1 = [7,8,9,10]
print(resultado_materia(notas_1))
notas_2 = [7,4,5,4]
print(resultado_materia(notas_2))
notas_3 = [1,8,9,10]
print(resultado_materia(notas_3))

#EJERCICIO 4
def saldo_actual(movimientos: list[tuple[str, int]])->int:
     suma_ingresos: int = 0
     suma_retiros: int = 0
     for i in range(len(movimientos)): 
          if movimientos[i][0] == "I": #con i accedo a los elementos de la lista, y con 0 accedo al primer elemento de la tupla
               suma_ingresos += movimientos[i][1]
          else:
               suma_retiros += movimientos[i][1] #con i accedo a los elementos de la lista, y con 1 accedo al segundo elemento de la tupla
     return suma_ingresos - suma_retiros

movimientos = [("I",2000), ("R", 20), ("R", 1000), ("I", 300)]
print(saldo_actual(movimientos))