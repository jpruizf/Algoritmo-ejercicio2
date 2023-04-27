
from claseviajerofrecuente import ViajeroFrecuente
#Algoritmo principal

if __name__ == '__main__':
    auxnum = int(input("Ingrese numero de viajero: "))
    auxdni = input("DNI: ")
    auxnom = input("Nombre: ")
    auxapellido = input("Apellido: ")
    auxmillas = int(input("Ingrese las millas acumuladas: "))
    Nuevo = ViajeroFrecuente(auxnum,auxdni,auxnom,auxapellido,auxmillas)
    print(Nuevo.cantidadTotaldeMillas())
    auxm = int(input("Ingrese la millas recorridas -> "))
    print(Nuevo.acumularMillas(auxm))
    auxcanje = int(input("Ingrese las millas a canjear >> "))
    print(Nuevo.canjearMillas(auxcanje))
    print(Nuevo.mostrar_menu())
    print(Nuevo.cargar())