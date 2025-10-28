"""
Ejercicio 3:
Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
palabras que tienen la misma traducción en inglés y en alemán.

problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
   requiere: -
   asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
}
Por ejemplo, dados los diccionarios
aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
se debería devolver res=2
"""