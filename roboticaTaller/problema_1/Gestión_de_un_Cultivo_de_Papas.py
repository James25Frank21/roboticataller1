class VariedadDePapa:
    def __init__(self, nombre, cicloCultivoDias, produccionHectarea):
        self.nombre = nombre
        self.cicloCultivoDias = cicloCultivoDias
        self.produccionHectarea = produccionHectarea

class CultivoDePapas:
    def __init__(self):
        self.variedadesCultivo = []

    def agregarVariedad(self, variedad):
        self.variedadesCultivo.append(variedad)

    def removerVariedad(self, nombreVariedad):
        nuevasVariedades = []
        for variedad in self.variedadesCultivo:
            if variedad.nombre != nombreVariedad:
                nuevasVariedades.append(variedad)
        self.variedadesCultivo = nuevasVariedades

    def calcularProduccion(self):
        produccionTotal = 0
        for variedad in self.variedadesCultivo:
            produccionTotal += variedad.produccionHectarea
        return produccionTotal

    def variedadCicloMasCorto(self):
        variedadMasCorta = self.variedadesCultivo[0]
        index = 1
        while index < len(self.variedadesCultivo):
            if self.variedadesCultivo[index].cicloCultivoDias < variedadMasCorta.cicloCultivoDias:
                variedadMasCorta = self.variedadesCultivo[index]
            index += 1
        return variedadMasCorta

    def mostrarVariedades(self):
        if self.variedadesCultivo:
            print("No hay variedades en el cultivo.")
            print("Variedades en el cultivo:")
            print("=========================================")
            for variedad in self.variedadesCultivo:
                print(
                    f"Nombre: {variedad.nombre}, Ciclo de cultivo: {variedad.cicloCultivoDias} días, Producción por hectárea: {variedad.produccionHectarea} toneladas")
        else:
            print("No hay variedad en el cultivo")
# Función para mostrar el menú y manejar las opciones
def MenuOpciones():
    print("=========================================")
    print("1. Agregar variedad de papa")
    print("2. Remover variedad de papa")
    print("3. Calcular producción total del cultivo")
    print("4. Mostrar variedad con ciclo de cultivo más corto")
    print("5. Ver cultivo de papas ")
    print("6. Salir")
    print("=========================================")


