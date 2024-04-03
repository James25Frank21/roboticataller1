class VariedadDePapa:
    def __init__(self, nombreVariedad, ciclo_de_cultivo, producionEstimada):
        self.nombre = nombreVariedad
        self.ciclo = ciclo_de_cultivo
        self.produccion = producionEstimada

    def __str__(self):
        return f"Nombre: {self.nombre}, Ciclo de cultivo: {self.ciclo}, Producción estimada: {self.produccion}"

class CultivoDePapas(VariedadDePapa):
    def __init__(self, nombreVariedad, ciclo_de_cultivo, producionEstimada, fechaSiembra, fechaCosecha):
        super().__init__(nombreVariedad, ciclo_de_cultivo, producionEstimada)
        self.fechaSiembra = fechaSiembra
        self.fechaCosecha = fechaCosecha

    def __str__(self):
        return f"{super().__str__()}, Fecha de siembra: {self.fechaSiembra}, Fecha de cosecha: {self.fechaCosecha}"