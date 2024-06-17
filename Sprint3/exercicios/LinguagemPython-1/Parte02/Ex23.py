class Calculo:
    def somar(self, x, y):
        return x + y

    def subtrair(self, x, y):
        return x - y

calculo = Calculo()
x = 4
y = 5
soma = calculo.somar(x, y)
subtracao = calculo.subtrair(x, y)

print(f"Somando: {x}+{y} = {soma}")
print(f"Subtraindo: {x}-{y} = {subtracao}")
