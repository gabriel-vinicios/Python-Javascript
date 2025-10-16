import unittest
from transpiler import transpile_python_to_js

class TestTranspiler(unittest.TestCase):
    
    def setUp(self):
        """Setup para cada teste"""
        pass
    
    def test_simple_function(self):
        """Teste de função simples"""
        python_code = """
def soma(a, b):
    return a + b
"""
        expected = """function soma(a, b) {
    return a + b;
}"""
        result = transpile_python_to_js(python_code).strip()
        self.assertIn("function soma(a, b)", result)
        self.assertIn("return a + b", result)
    
    def test_variable_assignment(self):
        """Teste de atribuição de variável"""
        python_code = "x = 42"
        result = transpile_python_to_js(python_code)
        self.assertIn("let x = 42", result)
    
    def test_print_function(self):
        """Teste de função print"""
        python_code = 'print("Hello World")'
        result = transpile_python_to_js(python_code)
        self.assertIn('console.log("Hello World")', result)
    
    def test_if_statement(self):
        """Teste de estrutura if"""
        python_code = """
if x > 5:
    print("Maior que 5")
"""
        result = transpile_python_to_js(python_code)
        self.assertIn("if (x > 5)", result)
        self.assertIn('console.log("Maior que 5")', result)
    
    def test_for_loop_range(self):
        """Teste de loop for com range"""
        python_code = """
for i in range(5):
    print(i)
"""
        result = transpile_python_to_js(python_code)
        self.assertIn("for (let i = 0; i < 5; i++)", result)
    
    def test_list_creation(self):
        """Teste de criação de lista"""
        python_code = "lista = [1, 2, 3]"
        result = transpile_python_to_js(python_code)
        self.assertIn("let lista = [1, 2, 3]", result)
    
    def test_fstring(self):
        """Teste de f-string"""
        python_code = 'nome = "João"\nprint(f"Olá, {nome}!")'
        result = transpile_python_to_js(python_code)
        self.assertIn("console.log(`Olá, ${nome}!`)", result)
    
    def test_class_definition(self):
        """Teste de definição de classe"""
        python_code = """
class MinhaClasse:
    def __init__(self, valor):
        self.valor = valor
    
    def metodo(self):
        return self.valor
"""
        result = transpile_python_to_js(python_code)
        self.assertIn("class MinhaClasse", result)
        self.assertIn("constructor(valor)", result)
    
    def test_comparison_operators(self):
        """Teste de operadores de comparação"""
        python_code = "resultado = x == y"
        result = transpile_python_to_js(python_code)
        self.assertIn("x === y", result)
    
    def test_boolean_operations(self):
        """Teste de operações booleanas"""
        python_code = "resultado = True and False"
        result = transpile_python_to_js(python_code)
        self.assertIn("true && false", result)
    
    def test_while_loop(self):
        """Teste de loop while"""
        python_code = """
while x < 10:
    x += 1
"""
        result = transpile_python_to_js(python_code)
        self.assertIn("while (x < 10)", result)
    
    def test_dictionary(self):
        """Teste de dicionário"""
        python_code = 'dados = {"nome": "João", "idade": 25}'
        result = transpile_python_to_js(python_code)
        self.assertIn('{"nome": "João", "idade": 25}', result)
    
    def test_len_function(self):
        """Teste da função len"""
        python_code = "tamanho = len(lista)"
        result = transpile_python_to_js(python_code)
        self.assertIn("lista.length", result)
    
    def test_multiple_statements(self):
        """Teste de múltiplas declarações"""
        python_code = """
x = 1
y = 2
z = x + y
print(z)
"""
        result = transpile_python_to_js(python_code)
        self.assertIn("let x = 1", result)
        self.assertIn("let y = 2", result)
        self.assertIn("let z = x + y", result)
        self.assertIn("console.log(z)", result)
    
    def test_nested_if(self):
        """Teste de if aninhado"""
        python_code = """
if x > 0:
    if x < 10:
        print("Entre 0 e 10")
"""
        result = transpile_python_to_js(python_code)
        self.assertIn("if (x > 0)", result)
        self.assertIn("if (x < 10)", result)

if __name__ == '__main__':
    unittest.main()