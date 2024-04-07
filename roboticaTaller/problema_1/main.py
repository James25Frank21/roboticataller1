from problema_1 import Gestión_de_un_Cultivo_de_Papas as gcp

if __name__ == "__main__":
    cultivo = gcp.CultivoDePapas()

    while True:
        gcp.MenuOpciones()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la variedad: ")
            cicloCultivo = int(input("Ingrese el ciclo de cultivo en días: "))
            produccion = float(input("Ingrese la producción por hectárea en toneladas: "))

            variedad = gcp.VariedadDePapa(nombre, cicloCultivo, produccion)
            cultivo.agregarVariedad(variedad)

            print("Variedad agregada correctamente.")
            print("=========================================")

        elif opcion == "2":
            nombre = input("Ingrese el nombre de la variedad a remover: ")

            cultivo.removerVariedad(nombre)

            print("Variedad removida correctamente.")
            print("=========================================")
        elif opcion == "3":
            print("Producción total estimada:", cultivo.calcularProduccion(), "toneladas")
            print("=========================================")
        elif opcion == "4":
            variedadMasCorta = cultivo.variedadCicloMasCorto()
            if variedadMasCorta:
                print("Variedad con ciclo de cultivo más corto:", variedadMasCorta.nombre)
                print("=========================================")
            else:
                print("No hay variedades en el cultivo.")
                print("=========================================")
        elif opcion == "5":

            cultivo.mostrarVariedades()

        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


