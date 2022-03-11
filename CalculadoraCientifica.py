#########################################################################
###ANALISIS###
#########################################################################
#Para hacer que inicie la calculadora deberemos crear un def=menu.
#Y crear un menu que muestre diferentes opciones matematicas.
#Esto lo haremos con un print por cada linea del menu.
#El menú tiene que tener suma, resta , multiplicación, división, resto,
#potencia, raiz cuadrada, factorial, valor absoluto, informe de actividad
#(numero de operaciones realizadas).
#También necesitará una línea para finalizar el programa.
#Cuando se haga una operación nos saltara un mensaje de que si quiere continuar con el programa o finalizar.
#########################################################################
###DISEÑO###
#########################################################################
#Tendremos que hacer una función def para menu (def menu():).
#Generar menu con todas las opciones de operaciones.
#
#
#
#
#
#
#########################################################################
import math
import os
#Aquí importamos las librerías
 
 
def Menu():
 
    print("                       |-----------------------------------------|")
    print("                       |:: CALCULADORA TOMÁS CABELLO FERNÁNDEZ ::|")
    print("                       |---------------------------------------  |")
    print("                       |                                         |")
    print("                       |  1. SUMA                                |")
    print("                       |  2. RESTA                               |")
    print("                       |  3. MULTIPLICACIÓN                      |")
    print("                       |  4. DIVISION                            |")
    print("                       |  5. RESTO                               |")
    print("                       |  6. POTENCIA                            |")
    print("                       |  7. RAÍZ CUADRADA                       |")
    print("                       |  8. FACTORIAL                           |")
    print("                       |  9. VALOR ABSOLUTO                      |")
    print("                       |  10. INFORME DE ACTIVIDAD               |")
    print("                       |  11. SALIR                              |")
    print("                       |                                         |")
    print("                       |-----------------------------------------|")
    print("")
 
def Calculadora():
 
    Menu()
 
    opc = int(input("Selecione nº de Opción: "))
 
    while (opc >0 and opc <24):
 
        if (opc==1):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
            print ('La Suma es:', num1+num2)
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 1
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 1
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
 
        elif(opc==2):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
            print ('La Resta es:',num1-num2)
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 2
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 2
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==3):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
            print ('La Multiplicacion es:', num1*num2)
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 3
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 3
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==4):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
 
            try:
              print ('La Division es:', num1/num2)
              print("")
              Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
              if Continuar == "s" or Continuar == "S":
                opc = 4
 
              elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
              else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 4
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
            except ZeroDivisionError:
              print ('No se Permite la Division Entre 0')
              print("")
              Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
              if Continuar == "s" or Continuar == "S":
                opc = 4
 
              elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
              else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 4
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==5):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
            print ('El Resto es:', num1%num2)
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 5
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 5
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==6):
            print("")
            base = int(input("Ingrese Base: "))
            print("")
            exponente = int(input("Ingrese Exponente: "))
            print("")
            print('La Potencia es:', base**exponente)
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 6
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 6
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==7):
            print("")
            num = int(input("Ingrese Número: "))
            print("")
            print("La raíz cuadrada de {} es {}".format(num, math.sqrt(num)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 7
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("SSelecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 7
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==8):
            print("")
            radianes = int(input("Ingrese Radianes: "))
            print("")
            print("El seno de {} es {}".format(radianes, math.sin(radianes)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 8
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
 
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 8
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
        elif(opc==10):
            print("")
            radianes = int(input("Ingrese Radianes: "))
            print("")
            print("El coseno de {} es {}".format(radianes, math.cos(radianes)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 10
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 10
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==11):
            print("")
            radianes = int(input("Ingrese Radianes: "))
            print("")
            print("El arcocoseno de {} es {}".format(radianes, math.acos(radianes)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 11
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 11
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==12):
            print("")
            radianes = int(input("Ingrese Radianes: "))
            print("")
            print("La tangente de {} es {}".format(radianes, math.tan(radianes)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 12
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 12
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==13):
            print("")
            radianes = int(input("Ingrese Radianes: "))
            print("")
            print("La arcotangente de {} es {}".format(radianes, math.atan(radianes)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 13
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 13
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
 
        elif(opc==14):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
            print("El M.C.M. entre "+str(num1)+" y "+str(num2)+" es: "+str(mcm(num1, num2)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 14
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 14
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==15):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
            print("El M.C.D. entre "+str(num1)+" y "+str(num2)+" es: "+str(mcd(num1, num2)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 15
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 15
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==9):
            print("")
            num = int(input("Ingrese Número: "))
            print("")
            print("El valor absoluto de {} es {}".format(num, math.fabs(num)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 17
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("SSelecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 17
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
        elif(opc==11):
            exit(0)
    while(opc <1 or opc >11 ):
        print("")
        print("Opción no Encontrada")
        print("")
        opc = int(input("Selecione nº de Opción: "))
 
Calculadora()