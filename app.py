import re

#valore finales leidos del archivo
claves = []


#expresiones Regulares
ClavesRE = r'Claves\s*=\s*\[([^\]]*)\]'
ValoresClavesRE = r'"{1}(.*?)",'
ImprimirRE = r'imprimir\("([^"]*)"\);'
ImprimirlnRE = r'imprimirln\("([^"]*)"\);'

def Leer():
    with open("prueba_facilita.bizdata", "r") as file:
        linea = file.readline()
        while linea:

            imprimir = None
            imprimirLN = None
            

            imprimir = re.findall(ImprimirRE, linea)
            imprimirLN = re.findall(ImprimirlnRE, linea)

            if "'''" in linea or '"""' in linea: 
                linea = file.readline()
                while "\'\'\'" not in linea or '"""' in linea:
                    linea = file.readline()
                    continue
                linea = file.readline()
                continue
            elif "#" in linea:
                linea = file.readline()
            elif imprimir:
                print(str(imprimir[0]).replace("/", "\n"), end="")
                linea = file.readline()
                continue
            elif imprimirLN:
                print(imprimirLN[0])
                linea = file.readline()
                continue
            if linea != "\n":
                print("\nXX",linea.replace("\n", ""))
            linea = file.readline()

def main():
    Leer()


#main
main()