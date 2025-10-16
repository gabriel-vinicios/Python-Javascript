# 🚀 Como usar a aplicação Python → JavaScript

## 📋 Pré-requisitos
- Python 3.7+
- Flask (instalado automaticamente)

## 🛠️ Instalação

1. Navegue até o diretório do projeto:
```bash
cd "d:\User\Desktop\Python-Javascript"
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 💻 Modos de uso

### 1. 🌐 Interface Web (Recomendado)

Inicie o servidor:
```bash
python app.py
```

Acesse: http://localhost:5000

**Funcionalidades da interface web:**
- Editor de código com syntax highlighting
- Transpilação em tempo real
- Exemplos pré-carregados
- Cópia do código gerado
- Atalho Ctrl+Enter para transpilar

### 2. ⌨️ Linha de Comando

```bash
python transpiler.py arquivo_entrada.py arquivo_saida.js
```

Exemplo:
```bash
python transpiler.py exemplo.py exemplo.js
```

### 3. 🎯 Demonstração

Execute exemplos pré-definidos:
```bash
python demo.py
```

### 4. 🧪 Testes

Execute os testes unitários:
```bash
python test_transpiler.py
```

## ✨ Funcionalidades Suportadas

### ✅ Básico
- ✅ Variáveis e constantes
- ✅ Funções e chamadas
- ✅ Operações matemáticas (+, -, *, /, %, **)
- ✅ Comparações (==, !=, <, >, <=, >=)
- ✅ Operações booleanas (and, or, not)

### ✅ Estruturas de Controle
- ✅ if/elif/else
- ✅ for loops (range e iteração)
- ✅ while loops

### ✅ Tipos de Dados
- ✅ Números (int, float)
- ✅ Strings e f-strings
- ✅ Listas → Arrays
- ✅ Dicionários → Objetos
- ✅ Booleanos (True/False → true/false)

### ✅ Orientação a Objetos
- ✅ Classes e construtores
- ✅ Métodos de instância
- ✅ Atributos (self.x → this.x)
- ✅ Instanciação de objetos

### ✅ Funções Built-in
- ✅ print() → console.log()
- ✅ len() → .length
- ✅ range() → for loops
- ✅ str(), int(), float()

## 📝 Exemplos de Conversão

### Python:
```python
def calcular_desconto(preco, percentual):
    desconto = preco * (percentual / 100)
    return preco - desconto

produtos = ["notebook", "mouse", "teclado"]
precos = [2000, 50, 150]

for i in range(len(produtos)):
    preco_original = precos[i]
    preco_com_desconto = calcular_desconto(preco_original, 10)
    print(f"{produtos[i]}: R$ {preco_original} → R$ {preco_com_desconto}")
```

### JavaScript Gerado:
```javascript
function calcular_desconto(preco, percentual) {
    let desconto = preco * (percentual / 100);
    return preco - desconto;
}

let produtos = ["notebook", "mouse", "teclado"];
let precos = [2000, 50, 150];

for (let i = 0; i < produtos.length; i++) {
    let preco_original = precos[i];
    let preco_com_desconto = calcular_desconto(preco_original, 10);
    console.log(`${produtos[i]}: R$ ${preco_original} → R$ ${preco_com_desconto}`);
}
```

## 🚫 Limitações Conhecidas

- ❌ Imports e módulos
- ❌ Decoradores
- ❌ Geradores (yield)
- ❌ Context managers (with)
- ❌ Exceções (try/except)
- ❌ Compreensões de lista avançadas
- ❌ Funções lambda complexas
- ❌ Herança de classes

## 🛠️ Personalização

O transpilador pode ser estendido modificando o arquivo `transpiler.py`:

1. Adicione novos visitadores para AST nodes
2. Implemente mapeamentos de funções
3. Adicione suporte para bibliotecas específicas

## 📞 Suporte

Para problemas ou sugestões:
1. Verifique os testes unitários em `test_transpiler.py`
2. Execute `python demo.py` para ver exemplos
3. Consulte os logs do servidor Flask para debugging