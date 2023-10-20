
class Objeto():
    def __init__(self) -> None:
        self.claves = []
    
    def addClaves(self, *args):
        for valor in args:
            self.claves.append(valor)