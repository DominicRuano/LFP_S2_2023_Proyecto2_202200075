
class Objeto():
    def __init__(self) -> None:
        self.claves = []
        self.registros = []
    
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
        list = []
        index = self.claves.index(columna.lower())
        for fila in self.registros:
            list.append(float(fila[index]))
        return sum(list)/len(list)
    
    def contarsi(self, columna, val):
        contador = 0
        index = self.claves.index(columna.lower())
        for fila in self.registros:
            for char in fila[index]:
                if char == val:
                    contador += 1
        return contador