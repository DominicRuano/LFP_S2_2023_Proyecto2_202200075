class Objeto():
    def __init__(self) -> None:
        self.claves = []
        self.registros = []
        self.errores = []
    
    def addClaves(self, args):
        for valor in args:
            self.claves.append(valor.lower())
    
    def addRegistros(self, valor):
        self.registros.append([val.lower() for val in valor])
    
    def conteo(self):
        contador = 0
        for columna in self.registros:
            for fila in columna:
                contador += 1
        return contador
    
    def promedio(self, columna):
        try:
            list = []
            index = self.claves.index(columna.lower())
            for fila in self.registros:
                list.append(float(fila[index]))
            return sum(list)/len(list)
        except:
            return -1
    
    def contarsi(self, columna, val):
        try:
            contador = 0
            index = self.claves.index(columna.lower())
            for fila in self.registros:
                for char in fila[index]:
                    if char == val:
                        contador += 1
            return contador
        except:
            return -1
    
    def sumar(self, columna):
        try:
            list = []
            index = self.claves.index(columna.lower())
            for fila in self.registros:
                list.append(float(fila[index]))
            return sum(list)
        except:
            return -1
    
    def max(self, columna):
        try:
            num = 0
            index = self.claves.index(columna.lower())
            for fila in self.registros:
                if float(fila[index]) > num:
                    num = float(fila[index])
            return num
        except:
            return -1
    
    def min(self, columna):
        try:
            valor = True
            index = self.claves.index(columna.lower())
            for fila in self.registros:
                if valor:
                    num = float(fila[index])
                    valor = False
                    continue
                if float(fila[index]) < num:
                    num = float(fila[index])
            return num
        except:
            return -1
    
    def reporte(self, titulo):
        with open("app\\reporte.html", "w") as file:
            file.write("<!DOCTYPE html>\n")
            file.write('<html lang="en">\n')
            file.write("<head>\n")
            file.write('\t<meta charset="UTF-8">\n')
            file.write('\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
            file.write("\t<title>Reporte</title>\n")
            file.write("<style> .center-table { margin: 0 auto; width: 70%; } </style>")
            file.write("</head>\n")
            file.write("<body>\n")
            file.write('\t<table class="center-table" border="1">\n')
            file.write("\t\t<tr>\n")
            try:
                file.write(f'\t\t\t<th colspan="{len(self.registros[0])}" >{titulo}</th>\n')
            except:
                file.write(f'\t\t\t<th>{titulo}</th>\n')
            file.write("\t\t</tr>\n")
            file.write("\t\t<tr>\n")
            for valor in self.claves:
                file.write(f"\t\t\t<th>{valor}</th>\n")
            file.write("\t\t</tr>\n")
            for valor in self.registros:
                file.write("\t\t<tr>\n")
                for registro in valor:
                    file.write(f"\t\t\t<th>{registro}</th>\n")
                file.write("\t\t</tr>\n")
            file.write("\t</table>\n")
            file.write("</body>\n")
            file.write("</html>\n")

    def imprimirErrores(self):
            contador = 1
            with open("app\\reporteErrores.html", "w") as file:
                file.write("<!DOCTYPE html>\n")
                file.write('<html lang="en">\n')
                file.write("<head>\n")
                file.write('\t<meta charset="UTF-8">\n')
                file.write('\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
                file.write("\t<title>Reporte</title>\n")
                file.write("<style> .center-table { margin: 0 auto; width: 70%; } </style>")
                file.write("</head>\n")
                file.write("<body>\n")
                file.write('\t<table class="center-table" border="1">\n')
                file.write("\t\t<tr>\n")
                file.write(f'\t\t\t<th colspan="{5}" > Errores </th>\n')
                file.write("\t\t</tr>\n")
                file.write("\t\t<tr>\n")
                file.write(f"\t\t\t<th>No.</th>\n")
                file.write(f"\t\t\t<th>Tipo</th>\n")
                file.write(f"\t\t\t<th>Caracter/Lexema</th>\n")
                file.write(f"\t\t\t<th>Fila</th>\n")
                file.write(f"\t\t\t<th>Columna</th>\n")
                file.write("\t\t</tr>\n")
                for valor in self.errores:
                    file.write("\t\t<tr>\n")
                    file.write(f"\t\t\t<th>{contador}</th>\n")
                    file.write(f"\t\t\t<th>{valor.tipo}</th>\n")
                    file.write(f"\t\t\t<th>{valor.caracter}</th>\n")
                    file.write(f"\t\t\t<th>{valor.fila}</th>\n")
                    file.write(f"\t\t\t<th>{valor.columna}</th>\n")
                    file.write("\t\t</tr>\n")
                file.write("\t</table>\n")
                file.write("</body>\n")
                file.write("</html>\n")