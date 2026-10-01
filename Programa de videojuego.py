# ==========================================
# EL LABERINTO DEL ABISMO
# ==========================================

def bienvenida():
    print("\n************************************************")
    print("*      BIENVENIDO A EL LABERINTO DEL ABISMO     *")
    print("************************************************")
    print("Misión: Reparar la nave y derrotar a la IA Corrupta.")
    print()


def instrucciones():
    print("\n===== INSTRUCCIONES =====")
    print("• Recoge objetos importantes.")
    print("• Usa herramientas especiales.")
    print("• Completa cada prueba para avanzar.")
    print("• Derrota a la IA Corrupta para ganar.")
    input("\nPresione Enter para volver al menú...")


def creditos():
    print("\n===== CRÉDITOS =====")
    print("Desarrollado por Ashley Yhajaira Estrada de León")
    input("\nPresione Enter para volver al menú...")


def jugar():

    vidas = 3
    combustible = 0

    print("\n===== FASE 1 =====")

    # NIVEL 1
    print("\nNIVEL 1: RECUPERAR FUSIBLES")
    fusibles = int(input("¿Cuántos fusibles encontraste?: "))

    if fusibles >= 3:
        print(" Objetivo completado.")
    else:
        print(" No encontraste suficientes fusibles.")
        return

    # NIVEL 2
    print("\nNIVEL 2: PROPULSOR DE PLASMA")
    respuesta = input("¿Activar propulsor? (si/no): ")

    if respuesta.lower() == "si":
        print("Propulsor activado.")
    else:
        print(" No puedes avanzar.")
        return

    # NIVEL 3
    print("\nNIVEL 3: FILTROS DE AIRE")
    filtros = int(input("¿Cuántos filtros conseguiste?: "))

    if filtros >= 2:
        print(" Filtros instalados.")
    else:
        print(" La nave no tiene suficiente aire.")
        return

    # NIVEL 4
    print("\nNIVEL 4: ACTIVAR COMPUTADORA")

    codigo = input("Ingrese el código de activación (ABISMO): ")

    if codigo.upper() == "ABISMO":
        print(" Computadora activada.")
    else:
        print(" Código incorrecto.")
        return

    print("\n FASE 1 COMPLETADA")

    print("\n===== FASE 2 =====")

    # NIVEL 5
    print("\nNIVEL 5: RECOLECTAR COMBUSTIBLE")

    combustible = int(input("¿Cuántas células de combustible conseguiste?: "))

    if combustible >= 50:
        vidas += 1
        print("Vida extra obtenida.")
        print("Vidas actuales:", vidas)
    else:
        print(" Continúas sin vida extra.")

    # NIVEL 6
    print("\nNIVEL 6: ESCUDO DE PROTECCIÓN")

    escudo = input("¿Activar escudo? (si/no): ")

    if escudo.lower() == "si":
        print(" Escudo activado por 3 segundos.")
    else:
        vidas -= 1
        print(" Daño recibido.")
        print("Vidas restantes:", vidas)

    if vidas <= 0:
        print("\n☠ GAME OVER")
        return

    # JEFE FINAL
    print("\n===== JEFE FINAL =====")
    print("IA CORRUPTA")

    print("\nResuelve la prueba para derrotarla.")
    print("¿Cuánto es 8 x 5?")

    respuesta = int(input("Respuesta: "))

    if respuesta == 40:
        print("\n ¡HAS DERROTADO A LA IA CORRUPTA!")
        print("PUNTAJE FINAL: 1000")
    else:
        print("\n☠ GAME OVER")


# PROGRAMA PRINCIPAL

bienvenida()

while True:

    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Jugar")
    print("2. Instrucciones")
    print("3. Créditos")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        jugar()

    elif opcion == "2":
        instrucciones()

    elif opcion == "3":
        creditos()

    elif opcion == "4":
        print("\nGracias por jugar.")
        break

    else:
        print("Opción inválida.")
