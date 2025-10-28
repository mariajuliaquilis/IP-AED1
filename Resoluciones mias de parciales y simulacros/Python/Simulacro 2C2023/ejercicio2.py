"""
Ejercicio 2:
problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
  requiere: -
  asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
  asegura: {res no tiene elementos repetidos }
}
Por ejemplo, dados
s = [-1,4,0,4,3,0,100,0,-1,-1]
t = [0,100,5,0,100,-1,5]
se debería devolver res = [3,4,5] ó res = [3,5,4] ó res = [4,3,5] ó res = [4,5,3] 
ó res = [5,3,4] ó res = [5,4,3]
"""