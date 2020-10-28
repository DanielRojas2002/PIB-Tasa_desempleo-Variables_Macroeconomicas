import sys 






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