class desempleos:
    def __init__ (self,desempleados,PEA):
        self.__desempleados=desempleados
        self.__PEA=PEA
    
    
    def calculo(self):
        resultado=(self.__desempleados/self.__PEA)*100
        print(f"La tasa de Desempleo es : {resultado}")


#VARIABLES MACROECONOMICAS
def formulas():
    print("*Indice de Precios : "+ "=" +"(NIVEL DE PRECIOS / BASE DE NIVEL DE PRECIOS * 100")
    print("*Inflacion : "+ "=" + "INDICE DE PRECIOS – INDICE DE PRECIOS UNO ATRÁS / INDICE DE PRECIOS UNO ATRÁS * 100")
    print("*PIBR : " + "=" + "PRODUCTO INTERNO BRUTO NOMINAL / INDICE DE PRECIOS * 100")

    
def indice(listaNivel,listaIndice,baseo,listaAño):
    contador=0
    separador=("*"*40)
    for precio in listaNivel:
        z=(precio/(listaNivel[baseo]))*100
        listaIndice.append(z)
    print(separador)
    print("")
    for numero in listaIndice:
        print("INDICE DE PRECIOS : ")
        print(f"El indice de Precios del año {listaAño[contador]} es = {numero}")
        contador=contador+1
        print(separador)
        print("")


def inflacion(listaIndice,listaAño,cuantos,listaInflacion):
    contador=1
    contador2=0
    contadorA=1
    separador=("*"*40)
    
    for numero in range(cuantos-1):
        resultado=(listaIndice[contador]-listaIndice[contador2])/listaIndice[contador2]*100
        contador=contador+1
        contador2=contador2+1
        if resultado!=0:
            listaInflacion.append(resultado)
    
    for numero in listaInflacion:
        print("INFLACION : ")
        print(f"La Inflacion del año {listaAño[contadorA]} es = {numero}")
        contadorA=contadorA+1
        print(separador)
        print("")


def PIBR(listaPIBN,listaIndice,listaPIBR,listaAño,cuantos):
    contador=0
    contadorA=0
    separador=("*"*40)
    for numero in range(cuantos):
        resultado=(listaPIBN[contador]/listaIndice[contador])*100
        listaPIBR.append(resultado)
        contador=contador+1
    
    for numero in listaPIBR:
        print("Producto Interno Bruto Real : ")
        print(f"El Producto Interno Bruto Real del año {listaAño[contadorA]} es = {numero}")
        contadorA=contadorA+1
        print(separador)
        print("")

#--------------------------------------------------------------------------------------------------------------------------------------
# METODO DEL INGRESO
class MetodoDelIngreso:
    def __init__ (self,II,IP,IN,D,BC,R,RT,INFE):
        self.__II=impuestoindirectos
        self.__IP=ingreso_propietario
        self.__IN=intereses
        self.__D=depreciacion
        self.__BC=beneficios_corporativos
        self.__R=renta
        self.__RT=renumeracion
        self.__INFE=ingreso_neto
        
          
    def formulas(self):
        print("-"*40)
        print("IN=(Rt+R+In+Ip+Bc)")
        print("PIB=(IN+IIE+dep+INFE)")
        print("-"*40)

    
    def PIB(self):
        IN=(self.__RT+self.__R+self.__IN+self.__IP+self.__BC)
        pib=(IN+self.__II+self.__D+self.__INFE)
        textoa=str(IN)
        textob=str(pib)
        print("")
        print("¿¿¿RESPUESTAS???:")
        print(f"Ingreso Nacional(IN) = {IN}  ")
        print(f"Producto Interno Bruto(PIB) = {pib} ")
        print("")

#-------------------------------------------------------------------------------------------------------------------------------------
#METODO DEL GASTO
class MetodoDelGasto:
    def __init__(self,ID,INFE,E,D,IM,GG,GCF):
        self.__IN=impuesto_indirectos
        self.__INFE=ingreso_neto
        self.__E=exportaciones
        self.__D=depreciacion
        self.__IM=importaciones
        self.__GG=gasto_gobierno
        self.__GCF=consumo_familia
        
    
    def PIB(self):
        XN=(self.__E-self.__IM)
        pib=(self.__GCF+self.__INFE+self.__GG+XN)
        PIN=(pib-self.__D)
        IN=(PIN-self.__INFE-self.__IN)
        print("")
        print("¿¿¿RESPUESTAS???:")
        print(f"Producto Interno Bruto(PIB) = {pib} ")
        print(f"Producto Interno Neto(PIN) = {PIN}  ")
        print(f"Ingreso Nacional(IN) = {IN}  ")
        print("")
        
    
    def formulas(self):
        print("-"*40)
        print("Estas son las Formulas ")
        print("Xn=(E-I)")
        print("PIB=(C+I+G+Xn)")
        print("IN=(PIN-ingreso neto de los factores-impuestos indirectos)")
        print("-"*40)