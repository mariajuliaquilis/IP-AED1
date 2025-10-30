"""
Ejemplo 3) Columnas repetidas [3 puntos]
Implementar la función columnas_repetidas, que dada una matriz no vacía de m
columnas (con m par y m ≥ 2) devuelve True si las primeras m/2 columnas son
iguales que las últimas m/2 columnas. Definimos a una secuencia de secuencias
como matriz si todos los elementos de la primera secuencia tienen la misma
longitud.

problema columnas_repetidas(in mat:seq<seq<Z>>) : Bool {
    requiere: {|mat| > 0}
    requiere: {todos los elementos de mat tienen igual longitud m, con m > 0
    (los elementos de mat son secuencias)}
    requiere: {todos los elementos de mat tienen longitud par (la cantidad de
    columnas de la matriz es par)}
    asegura: {(res = true) <=> las primeras m/2 columnas de mat son iguales a
    las últimas m/2 columnas}
}

Por ejemplo, dada la matriz
m = [[1,2,1,2],[-5,6,-5,6],[0,1,0,1]]
se debería devolver res = true
TIP: para dividir un número entero x por 2 y obtener como resultado un número
entero puede utilizarse la siguiente instrucción: int(x/2)
"""