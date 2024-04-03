class VariedadDePapa:
    def __init__(self, nombreVariedad, ciclo_de_cultivo, producionEstimada):
        self.nombre = nombreVariedad
        self.ciclo = ciclo_de_cultivo
        self.produccion = producionEstimada

    def __str__(self):
        return f"Nombre: {self.nombre}, Ciclo de cultivo: {self.ciclo}, Producción estimada: {self.produccion}"

class CultivoDePapas(VariedadDePapa):
    def __init__(self):
        self.variedad = []

    def agregarVariedad(self, nombreVariedad, ciclo_de_cultivo, producionEstimada):
        self.variedad.append(VariedadDePapa(nombreVariedad, ciclo_de_cultivo, producionEstimada))



