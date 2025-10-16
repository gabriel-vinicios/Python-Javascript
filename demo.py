#!/usr/bin/env python3
"""
Script de demonstração do transpilador Python para JavaScript
"""

from transpiler import transpile_python_to_js

def main():
    print("=== Demonstração do Transpilador Python → JavaScript ===\n")
    
    exemplos = [
        {
            "nome": "Função Simples",
            "codigo": '''def cumprimentar(nome):
    return f"Olá, {nome}!"

print(cumprimentar("Mundo"))'''
        },
        {
            "nome": "Estruturas de Controle",
            "codigo": '''idade = 20
if idade >= 18:
    print("Maior de idade")
    status = "adulto"
else:
    print("Menor de idade")
    status = "jovem"

for i in range(3):
    print(f"Contagem: {i}")'''
        },
        {
            "nome": "Classe e Objetos",
            "codigo": '''class Contador:
    def __init__(self, inicial=0):
        self.valor = inicial
    
    def incrementar(self):
        self.valor += 1
        return self.valor

c = Contador(5)
print(f"Valor: {c.incrementar()}")'''
        },
        {
            "nome": "Lista e Loops",
            "codigo": '''frutas = ["maçã", "banana", "laranja"]
precos = [1.20, 0.80, 1.50]

total = 0
for i in range(len(frutas)):
    print(f"{frutas[i]}: R$ {precos[i]}")
    total += precos[i]

print(f"Total: R$ {total}")'''
        }
    ]
    
    for exemplo in exemplos:
        print(f"📝 {exemplo['nome']}")
        print("=" * 50)
        print("Python:")
        print(exemplo['codigo'])
        print("\nJavaScript:")
        js_code = transpile_python_to_js(exemplo['codigo'])
        print(js_code)
        print("\n" + "="*70 + "\n")
    
    # Demonstração interativa
    print("🔄 Modo Interativo")
    print("Digite seu código Python (digite 'sair' para terminar):")
    print("Pressione Enter duas vezes para transpilar\n")
    
    while True:
        lines = []
        print("Python >>> ", end="")
        
        while True:
            try:
                line = input()
                if line.lower() == 'sair':
                    print("Até logo!")
                    return
                
                if line.strip() == "" and lines:
                    break
                
                lines.append(line)
                if lines:
                    print("... ", end="")
            except KeyboardInterrupt:
                print("\nSaindo...")
                return
        
        if lines:
            python_code = '\n'.join(lines)
            print("\nJavaScript:")
            js_code = transpile_python_to_js(python_code)
            print(js_code)
            print()

if __name__ == "__main__":
    main()