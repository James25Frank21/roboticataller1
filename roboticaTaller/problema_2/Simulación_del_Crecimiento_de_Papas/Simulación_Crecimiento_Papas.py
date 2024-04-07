import random

class SimulacionCultivo:
    def __init__(self):
        self.clima = ['sol', 'lluvia', 'sequia']
        self.plagas = False

    def iniciarSimulacion(self):
        diasSimulacion = 0
        climaSimulacion = []
        plagaProbabilidad = []
        total = []

        while diasSimulacion < 120:
            diasSimulacion += 1
            clima_actual = random.choice(self.clima)
            climaSimulacion.append(clima_actual)
            plagaProbabilidad.append(self.RegistrarEfectoClimaProbabilidadPlagas())

        print(
            f"sol: {climaSimulacion.count('sol')}, lluvia: {climaSimulacion.count('lluvia')}, sequia: {climaSimulacion.count('sequia')}.")
        print(
            f"numero de veces que con plaga: {plagaProbabilidad.count('con plaga')}, numero de veces que sin plaga: {plagaProbabilidad.count('sin plaga')}.")

        for clima, plaga in zip(climaSimulacion, plagaProbabilidad):
            if clima == "sol" and plaga == "sin plaga":
                total.append(1)
            elif clima == "sol" and plaga == "con plaga":
                total.append(0.5)
            elif clima == "lluvia" and plaga == "sin plaga":
                total.append(1)
            elif clima == "lluvia" and plaga == "con plaga":
                total.append(0.5)
            elif clima == "sequia" and plaga == "sin plaga":
                total.append(-1)
            elif clima == "sequia" and plaga == "con plaga":
                total.append(-1)
            else:
                print("No hay nada encontrado")
        self.CalcularRendimiento(sum(total),len(total))

    def RegistrarEfectoClimaProbabilidadPlagas(self):
        probabilidad_plagas = random.random()
        if probabilidad_plagas <= 0.3:
            self.plagas = True
            return "con plaga"
        else:
            return "sin plaga"

    def CalcularRendimiento(self, total,tamañoMuestra):

        cal = float((total/tamañoMuestra)*100)
        print(f"el rendimiento en el crecimiento de papa es del: {round(cal, 2)}%")


