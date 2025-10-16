# Exemplo 1: Função simples
def calcular_area(raio):
    pi = 3.14159
    return pi * raio ** 2

# Exemplo 2: Estrutura condicional
idade = 18
if idade >= 18:
    print("Pode votar")
else:
    print("Não pode votar")

# Exemplo 3: Loop
for i in range(5):
    print(f"Contagem: {i}")

# Exemplo 4: Lista
numeros = [1, 2, 3, 4, 5]
soma = 0
for num in numeros:
    soma += num

print(f"Soma total: {soma}")

# Exemplo 5: Classe
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def acelerar(self):
        return f"{self.marca} {self.modelo} está acelerando!"

meu_carro = Carro("Toyota", "Corolla")
print(meu_carro.acelerar())