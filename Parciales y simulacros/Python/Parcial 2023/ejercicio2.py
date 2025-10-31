"""
Ejemplo 2) Posición umbral [2 puntos]
Durante una noche en un restaurant pasan varios grupos de diversa cantidad de
personas. Para llevar control de esto, el dueño va anotando en su libreta
cuánta gente entra y sale. Para hacerlo rápido decide que la mejor forma de
llevarlo adelante es escribir un número al lado del otro, usando números
positivos para los grupos que entran y negativos para los que salen. Gracias a
estas anotaciones el dueño es capaz de hacer análisis del flujo de clientes.
Por ejemplo, le interesa saber en qué momento de la noche superó una
determinada cantidad de clientes totales que ingresaron (sin importar cuántos
hay en el momento en el local).

Implementar la función pos_umbral, que dada una secuencia de enteros (puede
haber negativos) devuelve la posición en la cual se supera el valor de umbral,
teniendo en cuenta sólo los elementos positivos. Se debe devolver -1 si el
umbral no se supera en ningún momento

problema pos_umbral (in s: seq<Z>, in u: Z) : Z {
    requiere: {u ≥ 0}
    asegura: {res=-1 si el umbral no se supera en ningún momento }
    asegura: {Si el umbral se supera en algún momento, res es la primera
    posición tal que la sumatoria de los primeros res+1 elementos
    (considerando solo aquellos que son positivos) es estrictamente mayor que
    el umbral u }
Por ejemplo, dadas
s = [1,-2,0,5,-7,3]
u = 5
se debería devolver res = 3
"""

def pos_umbral(s: list[int], u: int) -> int:
    res: int = -1
    sumatoria: int = 0
    for i in range(len(s)):
        if s[i] > 0:
            sumatoria+=s[i]
            if sumatoria > u:
                return i
    return res