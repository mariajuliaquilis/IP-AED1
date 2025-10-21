from queue import Queue as Cola


def orden_de_atencion(urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
    """
    requiere: {no hay elementos repetidos en urgentes}
    requiere: {no hay elementos repetidos en postergables}
    requiere: {la intersección entre postergables y urgentes es vacía}
    requiere: {|postergables| = |urgentes|}

    asegura: {no hay repetidos en res }
    asegura: {res es permutación de la concatenación de urgentes y postergables}
    asegura: {Si urgentes no es vacía, en tope de res hay un elemento de urgentes}
    asegura: {En res no hay dos seguidos de urgentes}
    asegura: {En res no hay dos seguidos de postergables}
    asegura: {Para todo c1 y c2 de tipo "urgente" pertenecientes a urgentes si c1 aparece antes que c2 en urgentes entonces c1 aparece antes que c2 en res}
    asegura: {Para todo c1 y c2 de tipo "postergable" pertenecientes a postergables si c1 aparece antes que c2 en postergables entonces c1 aparece antes que c2 en res}
    """ 
    res, conservar_urg, conservar_post = crear_colas()

    while not urgentes.empty():
        agregar_elem_a_resultado_y_recordar(urgentes, res, conservar_urg)
        agregar_elem_a_resultado_y_recordar(postergables, res, conservar_post)
        
    reconstruir_colas_originales(urgentes, postergables, conservar_urg, conservar_post)

    return res

def crear_colas():
    res: Cola[int] = Cola()
    conservar_urg: Cola[int] = Cola()
    conservar_post: Cola[int] = Cola()
    return res,conservar_urg,conservar_post

def reconstruir_colas_originales(urgentes, postergables, conservar_urg, conservar_post):
    while (not conservar_urg.empty()):   
        urgentes.put(conservar_urg.get())
        postergables.put(conservar_post.get())

def agregar_elem_a_resultado_y_recordar(cola_entrada, resultado, cola_conservar):
    urg = cola_entrada.get()
    cola_conservar.put(urg)
    resultado.put(urg)






def alarma_epidemiologica(registros: list[tuple[int, str]], infecciosas: list[str], umbral: float) -> dict[str, float]:
    """
    requiere: {0 < umbral < 1}
    asegura: {claves de res pertenecen a infecciosas}
    asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa enfermedad sobre el total de registros es mayor o igual al umbral, entonces res[enfermedad] = porcentaje}
    asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa enfermedad sobre el total de registros es menor que el umbral, entonces enfermedad no aparece en res}
    """
    cantidad_registros: int = len(registros)
    registros_por_enfermedad, res = crear_diccionarios()

    contar_registros_infecciosos_por_enfermedad(registros, infecciosas, registros_por_enfermedad)

    for enfermedad in registros_por_enfermedad.keys():
        porcentaje = calcular_porcentaje_de_registros(cantidad_registros, registros_por_enfermedad, enfermedad)
        agregar_enfermedad_si_supera_umbral(umbral, res, enfermedad, porcentaje)

    return res

def crear_diccionarios():
    registros_por_enfermedad: dict[str, int] = {}
    res: dict[str, float] = {}
    return registros_por_enfermedad,res

def calcular_porcentaje_de_registros(cantidad_registros:int, registros_por_enfermedad: dict[str, int], enfermedad:str):
    porcentaje: float = registros_por_enfermedad[enfermedad] / cantidad_registros
    return porcentaje

def agregar_enfermedad_si_supera_umbral(umbral:float, res: dict[str, float], enfermedad:str, porcentaje:float):
    if porcentaje >= umbral:
        res[enfermedad] = porcentaje

def contar_registros_infecciosos_por_enfermedad(registros:list[tuple[int, str]], infecciosas: list[str], registros_por_enfermedad:dict[str, int]):
    for _, enfermedad in registros:
        if (enfermedad in infecciosas):
            if (enfermedad not in registros_por_enfermedad):
                registros_por_enfermedad[enfermedad] = 0
            registros_por_enfermedad[enfermedad] += 1







def empleados_del_mes(horas: dict[int, list[int]]) -> list[int]:
    """
    requiere: {No hay valores en horas que sean listas vacías}
    asegura: {Si ID pertence a res entonces ID pertence a las claves de horas}
    asegura: {Si ID pertenece a res, la suma de sus valores de horas es el máximo de la suma de elementos de horas de todos los otros IDs}
    asegura: {Para todo ID de claves de horas, si la suma de sus valores es el máximo de la suma de elementos de horas de los otros IDs, entonces ID pertences a res}
    """
    suma_horas: dict[int, int] = {}
    max_horas_trabajadas: int = 0
    res: list[int] = []

    for id_empleado, horas_trabajadas in horas.items():
        sumar_horas_empleado(suma_horas, id_empleado, horas_trabajadas)
        max_horas_trabajadas = recordar_si_es_nuevo_maximo(suma_horas, max_horas_trabajadas, id_empleado)

    construir_diccionario_con_empleados_con_horas_maximas(suma_horas, max_horas_trabajadas, res)

    return res

def construir_diccionario_con_empleados_con_horas_maximas(suma_horas, max_horas_trabajadas, res):
    for id_empleado, horas_trabajadas in suma_horas.items():
        if horas_trabajadas == max_horas_trabajadas:
            res.append(id_empleado)

def recordar_si_es_nuevo_maximo(suma_horas, max_horas_trabajadas, id_empleado):
    if suma_horas[id_empleado] > max_horas_trabajadas:
        max_horas_trabajadas = suma_horas[id_empleado]
    return max_horas_trabajadas

def sumar_horas_empleado(suma_horas, id_empleado, horas_trabajadas):
    suma_horas[id_empleado] = 0
    for h in horas_trabajadas:
        suma_horas[id_empleado] += h




def nivel_de_ocupacion(pisos: list[list[bool]]) -> list[float]:
    """
    requiere: {Todos los pisos tienen la misma cantidad de camas.}
    requiere: {Hay por lo menos 1 piso en el hospital.}
    requiere: {Hay por lo menos una cama por piso.}
    asegura: {|res| = |camas_por_piso|}
    asegura: {Para todo 0<= i < |res| se cumple que res[i] es igual a la cantidad de camas ocupadas del piso i dividido el total de camas del piso i)} 
    """
    res: list[float] = []
    for piso in pisos:
        ocupacion: float = 0
        for cama in piso:
            if cama: # Chequeamos si la cama está ocupada.
                ocupacion += 1
        ocupacion /= len(piso) # Calculamos el porcentaje acá.
        res.append(ocupacion)
    return res
