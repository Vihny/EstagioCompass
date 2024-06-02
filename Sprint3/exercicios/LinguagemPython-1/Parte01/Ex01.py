from datetime import datetime


nome = "Vinicius"
idade = 20

ano_atual = datetime.now().year

ano_100 = ano_atual + (100 - idade)

print(f"{nome} completará 100 anos no ano {ano_100}.")
