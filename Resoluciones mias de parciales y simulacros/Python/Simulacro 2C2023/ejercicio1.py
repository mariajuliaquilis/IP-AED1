"""
Ejercicio 1:
problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
 requiere: {e pertenece a s }
 asegura: {res es la posición de la última aparición de e en s}
}
Por ejemplo, dados
s = [-1,4,0,4,100,0,100,0,-1,-1]
e = 0
se debería devolver res=7
"""
def cant_apariciones(s: list[int], e: int) -> int:
    res: int = 0
    for i in range(len(s)):
        if s[i] == e:
            res+=1
    return res

def ultima_aparicion(s: list[int], e: int) -> int:
    posicion: int = 0
    aparicion: int = 0
    for i in range(len(s)):
        if s[i] == e:
            aparicion+=1
            if aparicion == cant_apariciones(s,e):
                posicion = i
    return posicion