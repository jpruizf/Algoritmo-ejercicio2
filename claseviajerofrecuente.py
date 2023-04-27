import csv

#clase viajerofrecuente

class ViajeroFrecuente:
    __numero: int
    __dni: str
    __nombre: str
    __apellido: str
    __acum_millas: int
   
    #Definicion del constructor
    
    def __init__(self,num,dnix,nom,ape,acum_millas):
        self.__numero = num
        self.__dni = dnix
        self.__nombre = nom
        self.__apellido = ape
        self.__acum_millas = acum_millas
    
    #Definicion de la funcion total millas

    def cantidadTotaldeMillas(self):
        return f"El viajero {self.__nombre} {self.__apellido} tiene acumuladas {self.__acum_millas} millas\n"
    
    #Definicion de la funcion acumular millas
    
    def acumularMillas(self,millas:int):
        self.__acum_millas += millas
        return f"Felicidades viajero {self.__nombre} a llegado a un total de  {self.__acum_millas} millas actuales"
    
    #Definicion de la funcion canjear millas
    
    def canjearMillas(self,millas:int):
        if millas > self.__acum_millas:
            print(f"{self.__nombre} No tiene las millas sufientes para el valor ingresado. Sigue intentando!")
        else:
            self.__acum_millas -= millas
            print(f"¡Canjeo exitoso!")
        return f"Millas restantes acumuladas {self.__acum_millas}"
    
    #Definicion de la funcion cargar el archivo csv
    
    def cargar(self):
        archivo = open('Viajeros_nuevos.csv','r')
        reader = csv.reader(archivo, delimiter=';')
        lista_viajeros =[]
        for fila in reader:
            self.__numero = int(fila[0])
            self.__dni = str(fila[1])
            self.__nombre = str(fila[2])
            self.__apellido = str(fila[3])
            self.__acum_millas = int(fila[4])
            viajero = (self.__numero, self.__dni, self.__nombre, self.__apellido, self.__acum_millas)
            lista_viajeros.append(viajero)
        archivo.close()
        for viajero in lista_viajeros:
            print (f"Numero de viajero >> {viajero[0]}")
            print (f"DNI >> {viajero[1]}")
            print(f"Nombre >> {viajero[2]}")
            print(f"Apellido >> {viajero[3]}")
            print(f"Millas acumuladas >> {viajero[4]}")
   
    #Definicion de la funcion menu
   
    def mostrar_menu(self):
        print("1. Ver cantidad total de millas")
        print("2. Acumular millas")
        print("3. Canjear millas")
        print("4. Salir")
        while True:
            opcion = input("Ingrese una opcion: ")
            if opcion == "1":
                
                print(self.cantidadTotaldeMillas())
            elif opcion == "2":
                millas = int(input("Ingrese las millas recorridas"))
                print(self.acumularMillas(millas))
            elif opcion == "3":
                millas = int(input("Ingrese las millas a canjear: "))
                print(self.canjearMillas(millas))
            elif opcion == "4":
                print("Hasta luego!")
                break
            else:
                print("Error :/ opcion inexistente. Ingrese una opcion valida")