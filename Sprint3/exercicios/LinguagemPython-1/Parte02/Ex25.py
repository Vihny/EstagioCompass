class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = "Azul"

    def __str__(self):
        return f"O avião de modelo {self.modelo} possui uma velocidade máxima de {self.velocidade_maxima}, capacidade para {self.capacidade} passageiros e é da cor {self.cor}."

avioes = [
    Aviao("BOIENG456", "1500 km/h", "400 passageiros"),
    Aviao("Embraer Praetor 600", "863km/h", "14 passageiros"),
    Aviao("Antonov An-2", "258 Km/h", "12 passageiros")
]

for aviao in avioes:
    print(aviao)
