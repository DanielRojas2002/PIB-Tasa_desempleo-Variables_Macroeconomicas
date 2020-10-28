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
        archivoA=open("./archivos/datos.txt" , 'a')

        if menu==1:
            print("")
            print("*"*30 +"BIENVENIDO AL PROGRAMA" + "*"*30)
            print("Este programa te saca el PIB con el metodo del ingreso :)")
            print("-"*30)
            impuestos_indirectos=float(input("Dime los Impuestos Indirectos : "))
            ingreso_propietario=float(input("Dime los Ingresos de los Propietarios : "))
            intereses=float(input("Dime los Intereses : "))
            depreciacion=float(input("Dime la Depreciacion : "))
            beneficios_corporativos=float(input("Dime los Beneficios Corporativos : "))
            renta=float(input("Dime la Renta : "))
            renumeracion=float(input("Dime la Remuneraciones de los trabajadores : "))
            ingreso_neto=float(input("Dime el Ingreso Neto de los Factores Extranjeros : "))
            objeto=MetodoDelIngreso(impuestos_indirectos,ingreso_propietario,intereses,depreciacion,beneficios_corporativos,renta,renumeracion,ingreso_neto)
            objeto.formulas()
            objeto.PIB()
            print(separador)
            print("")
            print("1=SI\2=NO")
            opcion=int(input("Deseas regresar al Menu Principal : "))
            print("")
        
        elif menu==2:
            print("")
            print("*"*30 +"BIENVENIDO AL PROGRAMA" + "*"*30)
            print("Este programa te saca el PIB con el metodo del gasto :)")
            print("-"*30)
            impuesto_indirectos=float(input("Dime el impuesto indirecto : "))
            ingreso_neto=float(input("Dime el ingreso neto de los factores extranjeros : "))
            exportaciones=float(input("Dime las Exportaciones : "))
            depreciacion=float(input("Dime la Depreciacion : "))
            importaciones=float(input("Dime las Importaciones : "))
            gasto_gobierno=float(input("Dime el Gasto de Gobierno : "))
            consumo_familia=float(input("Dime el Gasto en Consumo de las familias : "))
            objeto=MetodoDelGasto(impuesto_indirectos,ingreso_neto,exportaciones,depreciacion,importaciones,gasto_gobierno,consumo_familia)
            objeto.formulas()
            objeto.PIB()
            print(separador)
            print("")
            print("1=SI\2=NO")
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
            inflacion(listaIndice,listaAño)
            print("")
            
            print(separador)
            PIBR(listaPIBN,listaIndice,listaPIBR,listaAño)
            print("")
            
            print(separador)
            print("")
            print("1=SI\2=NO")
            opcion=int(input("Deseas regresar al Menu Principal : "))
            print("")
        
        elif menu==4:
            desempleo=int(input("Ingresa los Desempleados o la poblacion no ocupada : "))
            PEA=int(input("Ingresa La Fueza Laboral o PEA : "))
            objeto=desempleos(desempleo,PEA)
            objeto.calculo()
            print(separador)
            print("")
            print("1=SI\2=NO")
            opcion=int(input("Deseas regresar al Menu Principal : "))
            print("")
        
        elif menu <=0 or menu>4:
            print("Ingresaste el numero de opcion mal , porfavor intentelo de nuevo :)")
            print(separador)
            print("")

except:
    print("*"*30)
    print(f"Ocurrió un problema {sys.exc_info()[1]}")
    print("Intenta respetar lo que se te pide :) ")
    print("*"*30)
    
finally:
    print("FIN DEL CODIGO ...")
    print("*"*30)