
class Historial:

    def __init__(self):
        self.registros = []

    def agregar_registro(self, nombre, operacion, resultado):
        registro = {
            "nombre": nombre,
            "operacion": operacion,
            "resultado": resultado
        }

        self.registros.append(registro)

    def mostrar_historial(self):
        if len(self.registros) == 0:
            print("\nTodavia no hay calculos guardados.")
        else:
            print("\n--- HISTORIAL DE CALCULOS ---")

            for i, registro in enumerate(self.registros, start=1):
                print("\nCalculo:", i)
                print("Sustancia:", registro["nombre"])
                print("Operacion:", registro["operacion"])
                print("Resultado:", registro["resultado"])

    def borrar_historial(self):
        self.registros.clear()
        print("\nEl historial ha sido borrado.")

    def cantidad_registros(self):
        return len(self.registros)
