
class Error():
    def __init__(self, fila, tipo, caracter, columna = 1) -> None:
        self.fila = fila
        self.columna = columna
        self.tipo = tipo
        self.caracter = caracter