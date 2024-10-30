from Funciones import *

def ejecutar_menu():

    cantidad_votos = 5 # cantidad asignada en la consigna
    listas = []

    while(True):
        print("Elecciones UTN!!\n1.Cargar votos.\n2.Mostrar Votos.\n3.Ordenar votos turno mañana.\n4.No te voto nadie.\n5.Turno que más fue a votar.\n6.Ballotage.\n7.Realizar segunda vueltar.\n8.Salir")

        opcion = pedir_numero("Su opcion: ","Opcion invalida ingrese números entre 1-8\nSu opcion:",1,8)
        
        if opcion == 1:
            listas = cargar_votos(cantidad_votos)
        elif opcion == 2:
            total_votos = mostrar_votos(listas)
        elif opcion == 3:
            ordenar_votos_manana(listas)
            print("Se ordenaron las listas por votos en el turno mañana.")
        elif opcion == 4:
            total_votos = mostrar_votos(listas)
            listas_bajo_5 = listas_con_menos_5_por_ciento(listas, total_votos)
            print("\nListas con menos del 5% de los votos:")
            if listas_bajo_5:
                 for lista in listas_bajo_5:
                    print(f"N° de Lista: {lista[0]}")
            else:
                print("No hay listas con menos del 5 porciento de los votos.")      
        elif opcion == 5:
            turno, cantidad = turno_mas_votado(listas)
            print(f"\nEl turno que mas voto fue: {turno} con {cantidad} votos.")
        elif opcion == 6:
            total_votos = mostrar_votos(listas)
            if verificar_segunda_vuelta(listas, total_votos):
                print("Hay segunda vuelta.")
            else:
                print("No hubo segunda vuelta.")
        elif opcion == 7:
            total_votos = mostrar_votos(listas)
            if verificar_segunda_vuelta(listas, total_votos):
                realizar_segunda_vuelta(listas)
            else:
                print("No se puede realizar la segunda vuelta.")
        elif opcion == 8:
            break    
        limpiar_consola()
ejecutar_menu()