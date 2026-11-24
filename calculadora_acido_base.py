
import math

class CalculadoraAcidoBase:

    def __init__(self):
        self.resultados = []

    def calcular_ph_acido(self, concentracion):
        if concentracion <= 0:
            return None

        ph = -math.log10(concentracion)
        return ph

    def calcular_poh_base(self, concentracion, iones=1):
        if concentracion <= 0 or iones <= 0:
            return None

        oh = concentracion * iones
        poh = -math.log10(oh)
        return poh

    def calcular_hidrogeno(self, ph):
        return 10 ** (-ph)

    def calcular_hidroxilo(self, poh):
        return 10 ** (-poh)

    def calcular_ph_desde_poh(self, poh):
        return 14 - poh

    def calcular_poh_desde_ph(self, ph):
        return 14 - ph

    def clasificar_disolucion(self, ph):
        if ph < 0 or ph > 14:
            return "Fuera del rango de clasificación"

        if ph < 7:
            return "Ácida"
        elif ph > 7:
            return "Básica"
        else:
            return "Neutra"

    def guardar_resultado(self, resultado):
        self.resultados.append(resultado)
