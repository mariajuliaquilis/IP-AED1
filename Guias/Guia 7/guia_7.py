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
def long_mayorASiete(s: list[list[str]])->bool:
     indice = 0
     while indice < len(s):
          if(len(s[indice]) > 7):
               return True
          else:
               indice +=1
     return False
     
#Ejercicio 10:
def es_palindroma(s: list[str])->bool:
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