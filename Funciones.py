import os
import random

def limpiar_consola() -> None:
    input("Ingrese cualquier boton para continuar...")
    os.system('cls')

def validar_numero (numero:str) -> bool: #devuelve true or false
    '''
    Funcion que valida un numero.
    Recibe un valor.
    Devuelve un boleano (si es un numero o no).
    '''
    return numero.isdigit() #se fija si es numero y si es asi devuelve true y que no sea mayor a 3 digitos xd

def validar_rango_min_max (numero: int, min:int, max:int) -> bool: #devuelve true or false si es min o max
    '''
    Funcion que valida el minimo y el maximo.
    Recibe un valor.
    El numero, el minimo  y el maximo.
    Devuelve true si esta en el rango requerido o false si no.
    '''
    retorno = False
    if numero >= min or numero <= max:
        retorno = True
    return retorno 
    
def validar_string(valor):
    '''
    Funcion que valida que sea un string y que no este vacio.
    Recibe un valor que sea un string.
    Devuelve True si es ok, si no, False.
    '''
    return isinstance(valor, str) and len(valor) > 0

def pedir_numero(mensaje: str, mensaje_error: str, min: int, max: int) -> int:
    numero = input(mensaje)
    while not validar_numero(numero) or not (min <= int(numero) <= max):
        numero = input(mensaje_error)
    return int(numero)

def crear_array_bidimensional(filas:int, columnas:int):
    array = [] #
    for i in range(filas): #crear una fila llena de ceros
        fila = [0] * columnas 
        array += [fila] 
    return array

def cargar_votos(num_listas: int) -> list:
    listas = [[0] * 4 for _ in range(num_listas)]  
    for i in range(num_listas):
        listas[i][0] = pedir_numero("Ingrese el numero de lista (3 cifras): ", "Numero invalido. Intente nuevamente: ", 100, 999)
        listas[i][1] = pedir_numero("Ingrese la cantidad de votos (Turno mañana): ", "Cantidad invalida. Intente nuevamente: ", 0, 10000)
        listas[i][2] = pedir_numero("Ingrese la cantidad de votos (Turno tarde): ", "Cantidad invalida. Intente nuevamente: ", 0, 10000)
        listas[i][3] = pedir_numero("Ingrese la cantidad de votos (Turno noche): ", "Cantidad invalida. Intente nuevamente: ", 0, 10000)
    return listas

def mostrar_votos(listas: list):
    print(f"\n{'N° de Lista':<15}{'Votos Mañana':<15}{'Votos Tarde':<15}{'Votos Noche':<15}{'Porcentajes':<15}")
    print("=" * 75) #linea que deja lindo el mostrar 
    total_votos = 0
    for lista in listas:
        total_votos += lista[1] + lista[2] + lista[3]

    for lista in listas: # Mostrar los datos de cada lista
        nro_lista = lista[0]
        votos_manana = lista[1]
        votos_tarde = lista[2]
        votos_noche = lista[3]
        
        total_lista = votos_manana + votos_tarde + votos_noche 
        if total_votos > 0:
            porcentaje = (total_lista / total_votos * 100)
        else:
            porcentaje = 0        
        print(f"{nro_lista:<15}{votos_manana:<15}{votos_tarde:<15}{votos_noche:<15}{porcentaje:.2f}%")
    return total_votos

def ordenar_votos_manana(listas: list):
    n = len(listas) #metodo de burbuja
    for i in range(n):
        for j in range(0, n-i-1):
            if listas[j][1] < listas[j + 1][1]:  #comparar por votos de la mañana
                listas[j], listas[j + 1] = listas[j + 1], listas[j]  #intercambiarlos
    return listas #lista ordenada

def listas_con_menos_5_por_ciento(listas: list, total_votos: int):
    if total_votos == 0:
        return []
    listas_bajo_5 = []  #almacenar las listas que cumplen la condición
    for lista in listas:
        total_lista = lista[1] + lista[2] + lista[3]  #sumar los votos
        porcentaje = total_lista / total_votos  #porcentaje
        if porcentaje < 0.05:  #verificar si es menor al 5%
            listas_bajo_5 += [lista]  
    return listas_bajo_5 

def turno_mas_votado(listas: list):
    total_votos_manana = sum(lista[1] for lista in listas)  
    total_votos_tarde = sum(lista[2] for lista in listas)   
    total_votos_noche = sum(lista[3] for lista in listas) 

    if total_votos_manana >= total_votos_tarde and total_votos_manana >= total_votos_noche:
        turno = "Mañana"
        cantidad = total_votos_manana
    elif total_votos_tarde >= total_votos_manana and total_votos_tarde >= total_votos_noche:
        turno = "Tarde"
        cantidad = total_votos_tarde
    else:
        turno = "Noche"
        cantidad = total_votos_noche

    return turno, cantidad

def verificar_segunda_vuelta(listas:list,total_votos:int):
    if total_votos == 0:
        return False #no hay votos
    hay_segunda_vuelta = True

    for lista in listas:
        total_lista = lista[1] + lista[2] + lista[3]  #sumar los votos
        porcentaje = total_lista / total_votos  #calcular el porcentaje
        
        if porcentaje > 0.5:  #verifico si hay alguien que tiene mas del 50%
            hay_segunda_vuelta = False  #si lo hay, no hay segunda vuelta
            break 
    return hay_segunda_vuelta

def realizar_segunda_vuelta(listas: list):
    candidato1 = None
    candidato2 = None
    max_votos1 = 0
    max_votos2 = 0

    for lista in listas:
        total_votos = lista[1] + lista[2] + lista[3]  #Suma de los votos
        if total_votos > max_votos1:
            max_votos2 = max_votos1  #actualizar el 2 candidato
            candidato2 = candidato1
            max_votos1 = total_votos  #actualizar el max
            candidato1 = lista
        elif total_votos > max_votos2:
            max_votos2 = total_votos  #actualizar el 2 max
            candidato2 = lista

    print(f"Realizando segunda vuelta entre: {candidato1[0]} y {candidato2[0]}")

    votos_turno_manana = pedir_numero("Ingrese la cantidad de votos (Turno mañana) en segunda vuelta: ", "Cantidad invalida. Intente nuevamente: ", 0, 10000)
    votos_turno_tarde = pedir_numero("Ingrese la cantidad de votos (Turno tarde) en segunda vuelta: ", "Cantidad invalida. Intente nuevamente: ", 0, 10000)
    votos_turno_noche = pedir_numero("Ingrese la cantidad de votos (Turno noche) en segunda vuelta: ", "Cantidad invalida. Intente nuevamente: ", 0, 10000)

    #votos aleatorios para el 1
    votos_candidato1 = [
        random.randint(0, votos_turno_manana),
        random.randint(0, votos_turno_tarde),
        random.randint(0, votos_turno_noche)
    ]
    
    #votos restantes para el 2
    votos_candidato2 = [
        votos_turno_manana - votos_candidato1[0],
        votos_turno_tarde - votos_candidato1[1],
        votos_turno_noche - votos_candidato1[2]
    ]

    total1 = sum(votos_candidato1)
    total2 = sum(votos_candidato2)
    print(f"Candidato 1 ({candidato1[0]}): {total1} votos")
    print(f"Candidato 2 ({candidato2[0]}): {total2} votos")
    if total1 > total2:
        print(f"¡Gano la lista {candidato1[0]}!")
    else:
        print(f"¡Gano la lista {candidato2[0]}!")