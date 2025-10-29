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

def contar_traducciones_iguales(ing: dict[str, str], ale: dict[str, str]) -> int:
   contador: int = 0
   for palabra_ing, traduccion_ing in ing.items():
      for palabra_ale, traduccion_ale in ale.items():
         if palabra_ing == palabra_ale and traduccion_ing == traduccion_ale:
            contador+=1
   return contador