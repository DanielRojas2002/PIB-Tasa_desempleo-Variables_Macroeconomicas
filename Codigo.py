import sys 
from clases import desempleos
from clases import formulas
from clases import indice
from clases import inflacion
from clases import PIBR
from clases import MetodoDelIngreso
from clases import MetodoDelGasto

try:
    opcion=1
    while opcion==1:
        separador=("*"*40)
        print("-"*30 +"MENU PRINCIPAL" + "-"*30)
        print("1-Sacar el PIB por el Metodo del Ingreso\n2-Sacar el PIB por el metodo del Gasto\n3-Sacar el Indice de Precios,Inflacion y Producto Interno Bruto Real")
        print("4-Sacar la Tasa de Desempleo")
        print("-"*30)
        menu=int(input("Ingrese el numero de opcion que desea ejecutar : "))
        print("-"*30)

        if menu==1:
            print("")
            print("*"*30 +"BIENVENIDO AL PROGRAMA" + "*"*30)
            print("Este programa te saca el PIB con el metodo del ingreso :)")
            print("-"*30)
            II=float(input("Dime los Impuestos Indirectos : "))
            IP=float(input("Dime los Ingresos de los Propietarios : "))
            IN=float(input("Dime los Intereses : "))
            D=float(input("Dime la Depreciacion : "))
            BC=float(input("Dime los Beneficios Corporativos : "))
            R=float(input("Dime la Renta : "))
            RT=float(input("Dime la Remuneraciones de los trabajadores : "))
            INFE=float(input("Dime el Ingreso Neto de los Factores Extranjeros : "))
            print("aqui pase")
            objeto=MetodoDelIngreso(II,IP,IN,D,BC,R,RT,INFE)
            print("aqui pase")
            objeto.formulas()
            print("aqui pase")
            objeto.PIB()
            print(separador)
            print("")
            print("1=SI\n2=NO")
            opcion=int(input("Deseas regresar al Menu Principal : "))
            print("")
        
        elif menu==2:
            print("")
            print("*"*30 +"BIENVENIDO AL PROGRAMA" + "*"*30)
            print("Este programa te saca el PIB con el metodo del gasto :)")
            print("-"*30)
            ID=float(input("Dime el impuesto indirecto : "))
            INFEE=float(input("Dime el ingreso neto de los factores extranjeros : "))
            E=float(input("Dime las Exportaciones : "))
            D=float(input("Dime la Depreciacion : "))
            IM=float(input("Dime las Importaciones : "))
            GG=float(input("Dime el Gasto de Gobierno : "))
            GCF=float(input("Dime el Gasto en Consumo de las familias : "))
            objeto=MetodoDelGasto(ID,INFEE,E,D,IM,GG,GCF)
            objeto.formulas()
            objeto.PIB()
            print(separador)
            print("")
            print("1=SI\n2=NO")
            opcion=int(input("Deseas regresar al Menu Principal : "))
            print("")
        
        elif menu==3:
            listaAño=[]
            contador1=1
            listaNivel=[]
            listaPIBN=[]
            listaIndice=[]
            listaInflacion=[]
            listaPIBR=[]
            contador=0
            contadoor=0
            cuantos=int(input("Cuantos Años vas a registrar : "))
            print(separador)
            for año in range(cuantos):
                año=int(input("Ingresa el Año : "))
                listaAño.append(año)
                
            print(separador)
            for año in listaAño:
                print(f"{contador1}-{año}")
                contador1=contador1+1
            base=int(input("Cual es el indice del año base : "))
            baseo=(base-1)
            print(separador)
            
                
            for precio in range(cuantos):
                nivel_precios=float(input(f"Ingresa el Nivel de Precios del Año {listaAño[contador]} :"))
                listaNivel.append(nivel_precios)
                contador=contador+1
            print(separador)
                
            for producto in range(cuantos):
                PIBN=float(input(f"Ingrese el Producto Interno Bruto Nominal del Año {listaAño[contadoor]} : "))
                listaPIBN.append(PIBN)
                contadoor=contadoor+1
            print(separador)
            
            print("")
            print(separador)
            print("Estas son las Formulas :) ")
            formulas()
            print(separador)
            print("")
            
            print(separador)
            indice(listaNivel,listaIndice,baseo,listaAño)
            print(separador)
            print("")
            
            print(separador)
            inflacion(listaIndice,listaAño,cuantos,listaInflacion)
            print("")
            
            print(separador)
            PIBR(listaPIBN,listaIndice,listaPIBR,listaAño,cuantos)
            print("")
            
            print(separador)
            print("")
            print("1=SI\n2=NO")
            opcion=int(input("Deseas regresar al Menu Principal : "))
            print("")
        
        elif menu==4:
            desempleo=int(input("Ingresa los Desempleados o la poblacion no ocupada : "))
            PEA=int(input("Ingresa La Fueza Laboral o PEA : "))
            objeto=desempleos(desempleo,PEA)
            objeto.calculo()
            print(separador)
            print("")
            print("1=SI\n2=NO")
            opcion=int(input("Deseas regresar al Menu Principal : "))
            print("")
        
        elif menu <=0 or menu>4:
            print("Ingresaste el numero de opcion mal , porfavor intentelo de nuevo :)")
            print(separador)
            print("")

except:
    print("*"*30)
    print(f"Ocurrió un problema {sys.exc_info()[1]}")
    print(f"Ocurrió un problema {sys.exc_info()[0]}")
    print(f"Ocurrió un problema {sys.exc_info()[2]}")
    print("Intenta respetar lo que se te pide :) ")
    print("*"*30)
    
finally:
    print("FIN DEL CODIGO ...")
    print("*"*30)