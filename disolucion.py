
class Disolucion:

    def __init__(self, nombre, formula, tipo, concentracion, volumen=1.0, temperatura=25.0):
        self.nombre = nombre
        self.formula = formula
        self.tipo = tipo.lower()
        self.concentracion = concentracion
        self.volumen = volumen
        self.temperatura = temperatura

    def validar_datos(self):
        if self.concentracion <= 0:
            return False

        if self.volumen <= 0:
            return False

        if self.temperatura < 0:
            return False

        if self.tipo not in ["acido", "base"]:
            return False

        return True

    def mostrar_datos(self):
        print("\n--- Datos de la disolución ---")
        print("Nombre:", self.nombre)
        print("Fórmula:", self.formula)
        print("Tipo:", self.tipo)
        print("Concentración:", self.concentracion, "M")
        print("Volumen:", self.volumen, "L")
        print("Temperatura:", self.temperatura, "°C")

    def obtener_concentracion(self):
        return self.concentracion

    def obtener_tipo(self):
        return self.tipo
