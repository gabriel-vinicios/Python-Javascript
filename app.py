from flask import Flask, render_template, request, jsonify
from transpiler import transpile_python_to_js
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transpile', methods=['POST'])
def transpile():
    try:
        data = request.get_json()
        python_code = data.get('python_code', '')
        
        if not python_code.strip():
            return jsonify({'error': 'Código Python não pode estar vazio'})
        
        js_code = transpile_python_to_js(python_code)
        
        return jsonify({
            'success': True,
            'js_code': js_code
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/examples')
def examples():
    """Retorna exemplos de código Python e JavaScript"""
    examples = [
        {
            'name': 'Função Simples',
            'python': '''def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Maria"))''',
            'javascript': '''function saudacao(nome) {
    return `Olá, ${nome}!`;
}

console.log(saudacao("Maria"));'''
        },
        {
            'name': 'Estruturas de Controle',
            'python': '''idade = 20
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

for i in range(5):
    print(f"Número: {i}")''',
            'javascript': '''let idade = 20;
if (idade >= 18) {
    console.log("Maior de idade");
} else {
    console.log("Menor de idade");
}

for (let i = 0; i < 5; i++) {
    console.log(`Número: ${i}`);
}'''
        },
        {
            'name': 'Lista e Operações',
            'python': '''numeros = [1, 2, 3, 4, 5]
soma = 0

for num in numeros:
    soma += num

print(f"Soma total: {soma}")
print(f"Quantidade: {len(numeros)}")''',
            'javascript': '''let numeros = [1, 2, 3, 4, 5];
let soma = 0;

for (let num of numeros) {
    soma += num;
}

console.log(`Soma total: ${soma}`);
console.log(`Quantidade: ${numeros.length}`);'''
        },
        {
            'name': 'Classe Simples',
            'python': '''class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Eu sou {self.nome}, tenho {self.idade} anos"

p = Pessoa("João", 25)
print(p.apresentar())''',
            'javascript': '''class Pessoa {
    constructor(nome, idade) {
        this.nome = nome;
        this.idade = idade;
    }
    
    apresentar() {
        return `Eu sou ${this.nome}, tenho ${this.idade} anos`;
    }
}

let p = new Pessoa("João", 25);
console.log(p.apresentar());'''
        }
    ]
    
    return jsonify(examples)

if __name__ == '__main__':
    # Criar diretório de templates se não existir
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    print("Servidor iniciado em http://localhost:5000")
    print("Pressione Ctrl+C para parar")
    app.run(debug=True)