from queue import LifoQueue as Pila

#ejercicio 1
def subsecuencias_que_suman(s: list[int], n: int) -> list[list[int]]:
    subsecuenciasQueSumanPorAhora:list[list[int]] = []
    for índiceActual in range (len(s)):
        AgregarSiNoEsVacía(subsecuenciaQueSumaDesde(s, índiceActual, n), subsecuenciasQueSumanPorAhora)
    return subsecuenciasQueSumanPorAhora

def AgregarSiNoEsVacía(listaAAgregar: list[int], listaDestino:list[list[int]]) :
    if len(listaAAgregar) > 0:
        listaDestino.append(listaAAgregar)

def subsecuenciaQueSumaDesde(lista: list[int], desde: int, sumaObjetivo: int) -> list[int]:
    sumaPorAhora: int = 0
    subsecuenciaQueSumanPorAhora: list[int] = []
    
    while desde < len(lista) and sumaPorAhora < sumaObjetivo:
        sumaPorAhora += lista[desde]
        subsecuenciaQueSumanPorAhora.append(lista[desde])
        desde += 1

    BorrarListaSi(subsecuenciaQueSumanPorAhora, sumaPorAhora != sumaObjetivo)
    return subsecuenciaQueSumanPorAhora

def BorrarListaSi(lista: list[int], condición: bool):
    if condición:
        lista.clear()

#ejercicio 2
def buscar_cliente_prioritario (clientes: Pila[tuple[str, str, int]]) -> str:
    pilaInvertida: Pila[tuple[str, str, int]] = Pila()
    MoverContenidoPila(clientes, pilaInvertida)

    MoverContenidoPilaHastaClientePrioritario(pilaInvertida, clientes)

    nombreClientePrioritario:str = nombreCliente(pilaInvertida.get())

    MoverContenidoPila(pilaInvertida, clientes)
    return nombreClientePrioritario

def pagaConBitcoinYTieneMásDe100(cliente: tuple[str, str, int]) -> bool:
    return medioDePagoCliente(cliente) == "bitcoin" and cantidadCliente(cliente) > 100

def nombreCliente(cliente: tuple[str, str, int]) -> str:
    return cliente[0]

def medioDePagoCliente(cliente: tuple[str, str, int]) -> str:
    return cliente[1]

def cantidadCliente(cliente: tuple[str, str, int]) -> int:
    return cliente[2]

def MoverContenidoPila(fuente: Pila[tuple[str, str, int]], destino: Pila[tuple[str, str, int]]):
    while not fuente.empty():
        destino.put(fuente.get())

def MoverContenidoPilaHastaClientePrioritario(fuente: Pila[tuple[str, str, int]], destino: Pila[tuple[str, str, int]]):
    while not pagaConBitcoinYTieneMásDe100(topeDePila(fuente)):
        destino.put(pilaInvertida.get())

def topeDePila(pila: Pila[tuple[str, str, int]]) -> tuple[str, str, int]:
    elTope = pila.get()
    pila.put(elTope)
    return elTope

#ejercicio 3
def eliminar_fila_que_mas_suma(A: list[list[int]]) -> list[list[int]]:
    matrizSinFilaQueMásSumaPorAhora:list[list[int]] = []
    for filaOriginal in A:
        AgregarFilaSi(A, filaOriginal, not esLaFilaQueMásSuma(A, filaOriginal))

    return matrizSinFilaQueMásSumaPorAhora

def AgregarFilaSi(matriz: list[list[int]], filaAAgregar: list[int], condición: bool):
    if condición:
        matriz.append(filaAAgregar)

def esLaFilaQueMásSuma(matriz: list[list[int]], filaCandidata: list[int]) -> bool:
    índiceFilaActual = 0
    while índiceFilaActual < len(matriz) and sumaFila(filaCandidata) >= sumaFila(matriz[índiceFilaActual]):
        índiceFilaActual += 1
    return índiceFilaActual == len(matriz)

def sumaFila(fila: list[int]) -> int:
    sumaPorAhora:int = 0
    for elementoActual in fila:
        sumaPorAhora += elementoActual
    return sumaPorAhora

#ejercicio 4
def peliculas_mas_vistas(favoritas_por_cliente: dict[str, str], n: int) -> dict[str, int]:
    vistasPorPelículaPorAhora:dict[str, int] = {}
    for nombrePelícula in películasConMásdDeNVistas(favoritas_por_cliente, n):
        vistasPorPelículaPorAhora[nombrePelícula] = cantidadDeVistas(nombrePelícula, favoritas_por_cliente)
    return vistasPorPelículaPorAhora

def películasConMásdDeNVistas(favoritas_por_cliente: dict[str, str], n: int) -> list[str]:
    películasConMásdDeNVistasPorAhora:list[str] = []
    for nombrePelícula in todasLasPelículas(favoritas_por_cliente):
        AgregarAListaSi(nombrePelícula, películasConMásdDeNVistasPorAhora, cantidadDeVistas(nombrePelícula, favoritas_por_cliente) > n)
    return películasConMásdDeNVistasPorAhora

def todasLasPelículas(favoritas_por_cliente: dict[str, str]) -> list[str]:
    películasPorAhora:list[str] = []
    for nombrePelícula in favoritas_por_cliente.values():
        AgregarAListaSi(nombrePelícula, películasPorAhora, not (nombrePelícula in películasPorAhora))
    return películasPorAhora

def cantidadDeVistas(nombrePelícula: str, favoritas_por_cliente: dict[str, str]) -> int:
    cantidadDeVistasPorAhora = 0
    for otroNombrePelícula in favoritas_por_cliente.values():
        cantidadDeVistasPorAhora += unoSiCeroSiNo(nombrePelícula == otroNombrePelícula)
    return cantidadDeVistasPorAhora

def AgregarAListaSi(elementoAAgregar: str, listaDestino: list[str], condición: bool):
    if condición:
        listaDestino.append(elementoAAgregar)