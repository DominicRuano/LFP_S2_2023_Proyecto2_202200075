import re
from objeto import Objeto

#valore finales leidos del archivo
claves = []
obj = Objeto()

#expresiones Regulares
ClavesRE = r'Claves\s*=\s*\['
ClavesRE2 = r'^\s*\]\s*$'
ValoresClavesRE = r'"{1}(.*?)",{0,1}'

ImprimirRE = r'imprimir\("([^"]*)"\);'
ImprimirlnRE = r'imprimirln\("([^"]*)"\);'

RegistrosRE = r'Registros\s*=\s*\['
RegistrosRE2 = r'^\s*\]\s*$'
ValoresRegistrosRE = r'\{([^}]+)\}'

ConteoRE = r'conteo\(\);'

PromedioRE = r'promedio\("([^"]*)"\);'

ContarSiRE = r'contarsi\((.*?)\);'
ValoresContarSiRE = r'\{([^}]+)\}'

DatosRE = r'datos\(\);'

SumarRE = r'sumar\("([^"]*)"\);'

MaxRE = r'max\("([^"]*)"\);'

MinRE = r'min\("([^"]*)"\);'

ReporteRE = r'exportarReporte\("([^"]*)"\);'



def Leer():
    with open("prueba_facilita.bizdata", "r") as file:
        linea = file.readline()
        while linea:

            imprimir = None
            imprimirLN = None
            claves = None
            registro = None
            conteo = None
            promedio = None
            contarsi = None
            datos = None
            sumar = None
            maxi = None
            mini = None
            reporte = None

            imprimir = re.findall(ImprimirRE, linea)
            imprimirLN = re.findall(ImprimirlnRE, linea)
            claves = re.findall(ClavesRE, linea)
            registro = re.findall(RegistrosRE, linea)
            conteo = re.findall(ConteoRE, linea)
            promedio = re.findall(PromedioRE, linea)
            contarsi = re.findall(ContarSiRE, linea)
            datos = re.findall(DatosRE, linea)
            sumar = re.findall(SumarRE, linea)
            maxi = re.findall(MaxRE, linea)
            mini = re.findall(MinRE, linea)
            reporte = re.findall(ReporteRE, linea)

            if "'''" in linea or '"""' in linea: 
                linea = file.readline()
                while "\'\'\'" not in linea or '"""' in linea:
                    linea = file.readline()
                    continue
                linea = file.readline()
                continue
            elif "#" in linea:
                linea = file.readline()
                continue
            elif imprimir:
                print(str(imprimir[0]).replace("/", "\n"), end="")
                linea = file.readline()
                continue
            elif imprimirLN:
                print(imprimirLN[0].replace("/", "\n"))
                linea = file.readline()
                continue
            elif claves:
                linea = file.readline()
                extraer = re.findall(ValoresClavesRE, linea)
                while extraer:
                    obj.addClaves(extraer)
                    linea = file.readline()
                    extraer = re.findall( ValoresClavesRE, linea)
                extraer = None
                extraer = re.findall(ClavesRE2, linea)
                if extraer:
                    linea = file.readline()
                    continue
                print("error en claves")
            elif registro:
                linea = file.readline()
                extraer = re.findall(ValoresRegistrosRE, linea)
                while extraer:
                    obj.addRegistros(extraer[0].replace(" ","").replace('"', "").split(","))
                    linea = file.readline()
                    extraer = re.findall(ValoresRegistrosRE, linea)
                extraer = None
                extraer = re.findall(RegistrosRE2, linea)
                if extraer:
                    linea = file.readline()
                    continue
                print("error en Registros")
            elif conteo:
                print(f"el conteo es: {obj.conteo()}")
                linea = file.readline()
                continue
            elif promedio:
                print(f"El promedio de {promedio[0]} es: {obj.promedio(promedio[0])}")
                linea = file.readline()
                continue
            elif contarsi:
                var = contarsi[0].replace(" ","").replace('"', "").split(",")
                if len(var) == 2:
                    print(f"El valor de contasi es: {obj.contarsi(var[0], var[1])}")
                    linea = file.readline()
                    continue
            elif datos:
                obj.datos()
                linea = file.readline()
                continue
            elif sumar:
                print(obj.sumar(sumar[0]))
                linea = file.readline()
                continue
            elif maxi:
                print(obj.max(maxi[0]))
                linea = file.readline()
                continue
            elif mini:
                print(obj.min(mini[0]))
                linea = file.readline()
                continue
            elif reporte:
                obj.reporte(reporte[0])
                linea = file.readline()
                continue
            if linea != "\n":
                print("XX",linea.replace("\n", ""))
            linea = file.readline()

def main():
    Leer()


#main
main()