import fileinput
import math
from Hash import transformacion

#Menu de navegación
if __name__ == "__main__":
    while True:
        print("¿Qué desea realizar?")
        print("1. Hash archivo")
        print("2. Hash texto")
        print("3. Calculo entropia")
        print("4. Salir")
        opcion = input()
        if opcion=="1":
            archivo=input("Ingrese el nombre del archivo (Ej:10.txt): \n")
            try:
                for line in fileinput.input(archivo):
                    transformacion(line.rstrip())
            except:
                print("Archivo invalido")
        elif opcion=="2":
            texto=input("Ingrese texto a hashear: \n")
            transformacion(texto)
        elif opcion=="3":
            # Formula:  H= Largo* log2 (Base), Para esto se definio la base correspondiente a todos los caracteres ASCII
            texto=input("Ingrese el texto a calcular: \n")
            entropia= len(texto)*math.log(128,2) 
            print("Texto:",texto," |  Entropia:",entropia)
        elif opcion=="4":
            break
        else:
            print("Entrada invalida")


