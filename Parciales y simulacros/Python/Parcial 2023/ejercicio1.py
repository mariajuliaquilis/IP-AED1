"""
Ejemplo 1) Acomodar [2 puntos]
El próximo 19 de Noviembre se realizará en Argentina la segunda vuelta de las
elecciones presidenciales. En esta competirán solo 2 listas (Lista UP; Lista
LLA). En la mayor parte del país los salones de las escuelas ofician de cuartos
oscuros. En ellos, las autoridades de mesa colocan las boletas sobre los
pupitres. Dado que esta elección se realizará en una época donde muy
probablemente haga mucho calor, no será raro el caso en el cual las boletas se
vuelen y mezclen a causa de ventiladores prendidos a máxima potencia. Cuando
esto ocurra, las autoridades deberán entrar al cuarto oscuro, juntar todas las
boletas, acomodarlas por partido y volver a distribuirlas en sus lugares.
Implementar una función acomodar que tome una lista con strings que
representan el nombre de lista (UP o LLA) y devuelva una lista con la misma
cantidad de elementos de cada uno de los posibles strings pero agrupadas, las
de Lista UP al principio y las de lista LLA al final.

No está permitido utilizar las funciones sort() y reverse().

problema acomodar (in s: seq<String>) : seq<String> {
    requiere: { Todos los elementos de s son o bien "LLA" o bien "UP"}
    asegura: {|res| = |s|}
    asegura: { Todos los elementos de res son o bien "LLA" o bien "UP"}
    asegura: {res contiene la misma cantidad de elementos "UP" que s}
    asegura: {res contiene todas las apariciones de "UP" antes de las
    apariciones de "LLA"}
}
Por ejemplo, dada
s = ["LLA", "UP", "LLA", "LLA", "UP"]
se debería devolver res = ["UP", "UP", "LLA", "LLA", "LLA"]
"""

def acomodar(s: list[str]) -> list[str]:
    res: list[str] = []
    lista_UP: list[str] = []
    lista_LLA: list[str] = []
    for i in range(len(s)):
        if s[i] == "UP":
            lista_UP.append(s[i])
        else:
            lista_LLA.append(s[i])
    res+=lista_UP
    res+=lista_LLA   
    return res