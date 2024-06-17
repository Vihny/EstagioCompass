class Passaro:
    def __init__(self, nome):
        self.nome = nome

    def voar(self):
        print(self.nome, "\nVoando...")

    def emitir_som(self):
        pass

class Pato(Passaro):
    def __init__(self):
        super().__init__("Pato")

    def emitir_som(self):
        super().emitir_som()
        print(self.nome, "emitindo som...\nQuack Quack")

class Pardal(Passaro):
    def __init__(self):
        super().__init__("Pardal")

    def emitir_som(self):
        super().emitir_som()
        print(self.nome, "emitindo som...\nPiu Piu")

pato = Pato()
pato.voar()
pato.emitir_som()

pardal = Pardal()
pardal.voar()
pardal.emitir_som()
