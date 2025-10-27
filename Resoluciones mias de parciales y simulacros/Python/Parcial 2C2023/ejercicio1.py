"""
Ejercicio 1) Índice de la n-ésima aparición [2 puntos]

Guido y Marcela son dos estudiantes de IP, nervioses con el parcial de Python. 
Con el objetivo de tener un rato antes del parcial para preguntarse algunas dudas deciden encontrarse en el colectivo y viajar juntes. 
Para poder coordinar de forma exacta en qué colectivo se tienen que subir, Marcela usa sus habilidades de programación aprendidas en 
IP para acceder de forma poco legítima a la base de datos de colectivos de todas las empresas. 
Con esto, arma una lista de todos los colectivos que van a pasar por la parada de Guido alrededor del horario acordado y le indica a 
Guido que se tiene que subir en el 3er colectivo de la línea 34. Por desgracia, Guido se olvida sus lentes antes de salir y no es capaz 
de distinguir a qué línea pertenece cada colectivo que llega a la parada. Por lo que solo puede contar cantidad total de colectivos que 
pasan.
Implementar la función ind_nesima_aparicion que dada una secuencia de enteros s, y dos enteros n y elem devuelve la posición en la cual 
elem aparece por n-ésima vez en s. En caso de que elem aparezca menos de n veces en s, devolver -1.

problema ind_nesima_aparicion (in s: seq⟨Z⟩, in n: Z, in elem: Z) : Z {
  requiere: {n>0}
  asegura: {Si el elemento aparece menos de n veces en la secuencia, res= -1 }
  asegura: {Si el elemento aparece al menos n veces en la secuencia, s[res] = elem }
  asegura: {Si el elemento aparece al menos n veces en la secuencia, elem aparece n-1 
  veces en s entre las posiciones 0 y res-1 }
}
Por ejemplo, dadas
s = [-1, 1, 1, 5, -7, 1, 3]
n = 2
elem = 1
se debería devolver res = 2
"""