import re

#valore finales leidos del archivo
claves = []


#expresiones Regulares
ClavesRE = r'Claves\s*=\s*\['
ClavesRE2 = r'^\s*\]\s*$'
ValoresClavesRE = r'"{1}(.*?)",'
ImprimirRE = r'imprimir\("([^"]*)"\);'
ImprimirlnRE = r'imprimirln\("([^"]*)"\);'

def Leer():
    with open("prueba_facilita.bizdata", "r") as file:
        linea = file.readline()
        while linea:

            imprimir = None
            imprimirLN = None
            claves = None

            imprimir = re.findall(ImprimirRE, linea)
            imprimirLN = re.findall(ImprimirlnRE, linea)
            claves = re.findall(ClavesRE, linea)

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
            elif claves:
                linea = file.readline()
                extraer = re.findall(ValoresClavesRE, linea)
                if extraer:
                    print(f"Claves = {extraer}")
                    linea = file.readline()
                    extraer = None
                    extraer = re.findall(ClavesRE2, linea)
                    if extraer:
                        linea = file.readline()
                        continue
                print("error en claves")
            if linea != "\n":
                print("XX",linea.replace("\n", ""))
            linea = file.readline()

def main():
    Leer()


#main
main()