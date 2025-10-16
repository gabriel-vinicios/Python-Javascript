# 🐍➡️📜 Transpilador Educacional Python → JavaScript

Um transpilador completo que converte código Python para JavaScript, desenvolvido como projeto acadêmico para a disciplina de **Teoria da Computação e Compiladores** da **UNISUL**.

## 🎯 Características Principais

- ✅ **Análise Completa**: Utiliza AST nativa do Python para parsing robusto
- ✅ **Conversão Estrutural**: Funções, classes, loops, condicionais
- ✅ **Interface Web Moderna**: Editor com syntax highlighting em tempo real
- ✅ **Código Limpo**: JavaScript idiomático e bem estruturado
- ✅ **100% Testado**: 38 testes automatizados com aprovação total
- ✅ **Educacional**: Código didático e bem documentado

## 🚀 Funcionalidades Suportadas

### Tipos de Dados
- **Números**: `int/float` → `number`
- **Strings**: Incluindo f-strings → template literals
- **Booleanos**: `True/False` → `true/false`
- **Listas**: → Arrays JavaScript
- **Dicionários**: → Objetos JavaScript

### Estruturas de Controle
- **Condicionais**: `if/elif/else`
- **Loops**: `for item in iterable`, `while condition`
- **Funções**: Definição e chamadas (com argumentos padrão)
- **Classes**: Métodos, construtores (`__init__`)

### Operadores
- **Aritméticos**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Relacionais**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Lógicos**: `and`, `or`, `not`

## 💻 Como usar

### 🌐 Interface Web (Recomendado)
```bash
python app.py
```
Acesse: **http://localhost:5000**

### ⌨️ Linha de Comando
```bash
python transpiler.py arquivo.py arquivo.js
```

### 🧪 Executar Testes
```bash
python test_transpiler.py
```

## 📚 Exemplos de Conversão

### Algoritmo Básico
```python
# Python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
```

```javascript
// JavaScript gerado
function fibonacci(n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

for (let i = 0; i < 10; i++) {
    console.log(`F(${i}) = ${fibonacci(i)}`);
}
```

### Programação Orientada a Objetos
```python
# Python
class Calculadora:
    def __init__(self):
        self.resultado = 0
    
    def somar(self, x, y):
        self.resultado = x + y
        return self.resultado

calc = Calculadora()
print(calc.somar(10, 5))
```

```javascript
// JavaScript gerado
class Calculadora {
    constructor() {
        this.resultado = 0;
    }
    
    somar(x, y) {
        this.resultado = x + y;
        return this.resultado;
    }
}

let calc = new Calculadora();
console.log(calc.somar(10, 5));
```

## 📖 Documentação Acadêmica

Este projeto foi desenvolvido como trabalho de conclusão da disciplina de Teoria da Computação e Compiladores. A documentação acadêmica completa está disponível em:

- 📄 **[Trabalho Acadêmico Completo](TRABALHO_ACADEMICO_COMPLETO.md)** - Documento técnico detalhado (formato paper)
- 📋 **[Relatório Acadêmico](RELATORIO_ACADEMICO.md)** - Versão formatada para apresentação
- 📚 **[Como Usar](COMO_USAR.md)** - Guia prático de instalação e uso

## 🏗️ Arquitetura do Sistema

```
┌─────────────────┐    ┌─────────────────┐
│   Interface Web │    │       CLI       │
│  (index.html)   │    │   (terminal)    │
└────────┬────────┘    └────────┬────────┘
         │                      │
         └──────────┬───────────┘
                    │
         ┌──────────▼──────────┐
         │    Flask Server     │
         │      (app.py)       │
         └──────────┬──────────┘
                    │
         ┌──────────▼──────────┐
         │   Transpiler Core   │
         │   (transpiler.py)   │
         └──────────┬──────────┘
                    │
         ┌──────────▼──────────┐
         │    Python AST       │
         │   (ast module)      │
         └─────────────────────┘
```

## 🧪 Testes e Validação

### Estatísticas de Testes
- **38 testes automatizados**: 100% aprovação
- **Cobertura funcional**: 90%+ das construções Python básicas
- **Performance**: Linear O(n), adequada para código educacional
- **Validação**: Programas reais convertidos e executados com sucesso

### Executar Todos os Testes
```bash
# Testes unitários
python test_transpiler.py

# Demonstração interativa
python demo.py

# Exemplo prático
python transpiler.py exemplo.py exemplo.js
```

## 🛠️ Instalação

### Pré-requisitos
- Python 3.11+
- Flask 2.3+ (apenas para interface web)

### Passos
```bash
# 1. Clone o repositório
git clone https://github.com/usuario/python-javascript-transpiler.git
cd python-javascript-transpiler

# 2. Instale dependências (opcional - apenas para interface web)
pip install flask

# 3. Execute
python app.py  # Interface web
# ou
python transpiler.py exemplo.py exemplo.js  # CLI
```

## 📊 Limitações Conhecidas

### Não Implementado (por escolha educacional)
- ❌ Decoradores (`@decorator`)
- ❌ Geradores (`yield`)
- ❌ Context managers (`with`)
- ❌ Imports complexos
- ❌ Exceções avançadas
- ❌ Metaclasses

### Escopo Atual
- ✅ 90% das construções Python básicas
- ✅ Foco em código educacional/introdutório
- ✅ JavaScript moderno e idiomático

## 🤝 Contribuição Acadêmica

Este projeto foi desenvolvido por:
- **Erick Vieira**
- **Patrick Lohn**  
- **Rafael Sonoki**

**Orientação**: Universidade do Sul de Santa Catarina (UNISUL)  
**Disciplina**: Teoria da Computação e Compiladores  
**Data**: Outubro 2025

## 📄 Licença

MIT License - Veja [LICENSE](LICENSE) para detalhes.

## 🔗 Links Úteis

- 📚 [Documentação Python AST](https://docs.python.org/3/library/ast.html)
- 🌐 [MDN JavaScript Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- 🏫 [UNISUL - Universidade do Sul de Santa Catarina](https://www.unisul.br/)

---

> *"Um transpilador não apenas traduz código; ele traduz conhecimento."*

**⭐ Se este projeto foi útil, considere dar uma estrela no GitHub!**