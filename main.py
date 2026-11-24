
from disolucion import Disolucion
from calculadora_acido_base import CalculadoraAcidoBase
from historial import Historial


calculadora = CalculadoraAcidoBase()
historial = Historial()


def mostrar_menu():
    print("\n================================")
    print("   CALCULADORA DE ACIDOS Y BASES")
    print("================================")
    print("1. Calcular pH de un acido fuerte")
    print("2. Calcular pOH de una base fuerte")
    print("3. Calcular concentracion de H+")
    print("4. Calcular concentracion de OH-")
    print("5. Clasificar una disolucion")
    print("6. Mostrar historial")
    print("7. Salir")
    print("================================")


def pedir_concentracion():
    while True:
        try:
            concentracion = float(input("Ingresa la concentracion (M): "))

            if concentracion <= 0:
                print("La concentracion debe ser mayor que cero.")
            else:
                return concentracion

        except ValueError:
            print("Ingresa un numero valido.")


def ejecutar_programa():
    while True:
        mostrar_menu()

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            concentracion = pedir_concentracion()
            resultado = calculadora.calcular_ph_acido(concentracion)

            print("El pH es:", round(resultado, 2))

            historial.agregar_registro(
                "Acido fuerte", "Calculo de pH", round(resultado, 2)
            )

        elif opcion == "2":
            concentracion = pedir_concentracion()
            resultado = calculadora.calcular_poh_base(concentracion)

            print("El pOH es:", round(resultado, 2))

            historial.agregar_registro(
                "Base fuerte", "Calculo de pOH", round(resultado, 2)
            )

        elif opcion == "3":
            ph = float(input("Ingresa el valor del pH: "))
            resultado = calculadora.calcular_hidrogeno(ph)

            print("Concentracion de H+:", resultado)

            historial.agregar_registro(
                "Disolucion", "Concentracion de H+", resultado
            )

        elif opcion == "4":
            poh = float(input("Ingresa el valor del pOH: "))
            resultado = calculadora.calcular_hidroxilo(poh)

            print("Concentracion de OH-:", resultado)

            historial.agregar_registro(
                "Disolucion", "Concentracion de OH-", resultado
            )

        elif opcion == "5":
            ph = float(input("Ingresa el valor del pH: "))
            resultado = calculadora.clasificar_disolucion(ph)

            print("La disolucion es:", resultado)

            historial.agregar_registro(
                "Disolucion", "Clasificacion", resultado
            )

        elif opcion == "6":
            historial.mostrar_historial()

        elif opcion == "7":
            print("Gracias por utilizar el programa.")
            break

        else:
            print("Opcion incorrecta. Intenta nuevamente.")


if __name__ == "__main__":
    ejecutar_programa()
