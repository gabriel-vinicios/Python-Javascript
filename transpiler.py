import ast
import re
from typing import List, Dict, Any

class PythonToJSTranspiler:
    def __init__(self):
        self.indentation_level = 0
        self.indent_size = 4
        
    def get_indent(self) -> str:
        return " " * (self.indentation_level * self.indent_size)
    
    def transpile(self, python_code: str) -> str:
        """Converte código Python para JavaScript"""
        try:
            tree = ast.parse(python_code)
            js_code = self.visit_node(tree)
            return js_code
        except SyntaxError as e:
            return f"// Erro de sintaxe Python: {e}"
    
    def visit_node(self, node: ast.AST) -> str:
        """Visita um nó da AST e retorna o código JavaScript correspondente"""
        method_name = f"visit_{type(node).__name__}"
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)
    
    def generic_visit(self, node: ast.AST) -> str:
        """Visitante genérico para nós não implementados"""
        return f"// Não implementado: {type(node).__name__}"
    
    def visit_AugAssign(self, node: ast.AugAssign) -> str:
        """Converte atribuição aumentada (+=, -=, etc.)"""
        target = self.visit_node(node.target)
        value = self.visit_node(node.value)
        
        op_mapping = {
            ast.Add: '+=',
            ast.Sub: '-=',
            ast.Mult: '*=',
            ast.Div: '/=',
            ast.Mod: '%=',
            ast.Pow: '**='
        }
        
        operator = op_mapping.get(type(node.op), '+=')
        
        if isinstance(node.op, ast.Pow):
            return f"{target} = Math.pow({target}, {value});"
        
        return f"{target} {operator} {value};"
    
    def visit_Attribute(self, node: ast.Attribute) -> str:
        """Converte acesso a atributos (obj.attr)"""
        value = self.visit_node(node.value)
        
        # Tratar 'self' especialmente
        if isinstance(node.value, ast.Name) and node.value.id == 'self':
            return f"this.{node.attr}"
        
        return f"{value}.{node.attr}"
    
    def visit_Module(self, node: ast.Module) -> str:
        """Visita o módulo principal"""
        statements = []
        for stmt in node.body:
            result = self.visit_node(stmt)
            if result.strip():
                statements.append(result)
        return "\n".join(statements)
    
    def visit_FunctionDef(self, node: ast.FunctionDef) -> str:
        """Converte definição de função"""
        args = [arg.arg for arg in node.args.args]
        args_str = ", ".join(args)
        
        function_body = []
        self.indentation_level += 1
        
        for stmt in node.body:
            result = self.visit_node(stmt)
            if result.strip():
                function_body.append(self.get_indent() + result)
        
        self.indentation_level -= 1
        
        body_str = "\n".join(function_body)
        return f"function {node.name}({args_str}) {{\n{body_str}\n}}"
    
    def visit_Return(self, node: ast.Return) -> str:
        """Converte statement de return"""
        if node.value:
            value = self.visit_node(node.value)
            return f"return {value};"
        return "return;"
    
    def visit_Assign(self, node: ast.Assign) -> str:
        """Converte atribuição de variável"""
        target = self.visit_node(node.targets[0])
        value = self.visit_node(node.value)
        
        # Se o target é um atributo (self.x), não usar 'let'
        if isinstance(node.targets[0], ast.Attribute):
            return f"{target} = {value};"
        
        return f"let {target} = {value};"
    
    def visit_Name(self, node: ast.Name) -> str:
        """Converte nome de variável"""
        return node.id
    
    def visit_Constant(self, node: ast.Constant) -> str:
        """Converte constantes (números, strings, etc.)"""
        if isinstance(node.value, str):
            # Converte f-strings para template literals
            if hasattr(node, 'kind') and node.kind == 'f':
                return self.convert_fstring(node.value)
            return f'"{node.value}"'
        elif isinstance(node.value, bool):
            return str(node.value).lower()
        elif node.value is None:
            return "null"
        return str(node.value)
    
    def visit_JoinedStr(self, node: ast.JoinedStr) -> str:
        """Converte f-strings para template literals"""
        parts = []
        for value in node.values:
            if isinstance(value, ast.Constant):
                parts.append(value.value)
            elif isinstance(value, ast.FormattedValue):
                expr = self.visit_node(value.value)
                parts.append(f"${{{expr}}}")
        
        result = "".join(str(part) for part in parts)
        return f"`{result}`"
    
    def visit_Call(self, node: ast.Call) -> str:
        """Converte chamadas de função"""
        func_name = self.visit_node(node.func)
        args = [self.visit_node(arg) for arg in node.args]
        args_str = ", ".join(args)
        
        # Mapeamento de funções Python para JavaScript
        function_mapping = {
            'print': 'console.log',
            'len': 'length',
            'str': 'String',
            'int': 'parseInt',
            'float': 'parseFloat'
        }
        
        if func_name in function_mapping:
            if func_name == 'len':
                return f"{args[0]}.length"
            func_name = function_mapping[func_name]
        
        # Tratar chamadas de método (obj.method())
        if isinstance(node.func, ast.Attribute):
            obj = self.visit_node(node.func.value)
            method = node.func.attr
            
            # Tratar casos especiais
            if isinstance(node.func.value, ast.Name) and node.func.value.id == 'self':
                return f"this.{method}({args_str})"
            
            return f"{obj}.{method}({args_str})"
        
        # Chamada de construtor de classe (sem new)
        if func_name[0].isupper():
            return f"new {func_name}({args_str})"
        
        return f"{func_name}({args_str})"
    
    def visit_If(self, node: ast.If) -> str:
        """Converte estrutura if/else"""
        test = self.visit_node(node.test)
        
        # Corpo do if
        if_body = []
        self.indentation_level += 1
        for stmt in node.body:
            result = self.visit_node(stmt)
            if result.strip():
                if_body.append(self.get_indent() + result)
        self.indentation_level -= 1
        
        result = f"if ({test}) {{\n" + "\n".join(if_body) + "\n}"
        
        # Else if ou else
        if node.orelse:
            if len(node.orelse) == 1 and isinstance(node.orelse[0], ast.If):
                # elif
                else_part = self.visit_node(node.orelse[0])
                result += f" else {else_part}"
            else:
                # else
                else_body = []
                self.indentation_level += 1
                for stmt in node.orelse:
                    else_result = self.visit_node(stmt)
                    if else_result.strip():
                        else_body.append(self.get_indent() + else_result)
                self.indentation_level -= 1
                result += f" else {{\n" + "\n".join(else_body) + "\n}"
        
        return result
    
    def visit_For(self, node: ast.For) -> str:
        """Converte loop for"""
        target = self.visit_node(node.target)
        iter_obj = self.visit_node(node.iter)
        
        # Corpo do for
        for_body = []
        self.indentation_level += 1
        for stmt in node.body:
            result = self.visit_node(stmt)
            if result.strip():
                for_body.append(self.get_indent() + result)
        self.indentation_level -= 1
        
        body_str = "\n".join(for_body)
        
        # Diferentes tipos de iteração
        if isinstance(node.iter, ast.Call) and isinstance(node.iter.func, ast.Name):
            if node.iter.func.id == 'range':
                args = [self.visit_node(arg) for arg in node.iter.args]
                if len(args) == 1:
                    return f"for (let {target} = 0; {target} < {args[0]}; {target}++) {{\n{body_str}\n}}"
                elif len(args) == 2:
                    return f"for (let {target} = {args[0]}; {target} < {args[1]}; {target}++) {{\n{body_str}\n}}"
        
        # Iteração sobre array/objeto
        return f"for (let {target} of {iter_obj}) {{\n{body_str}\n}}"
    
    def visit_While(self, node: ast.While) -> str:
        """Converte loop while"""
        test = self.visit_node(node.test)
        
        while_body = []
        self.indentation_level += 1
        for stmt in node.body:
            result = self.visit_node(stmt)
            if result.strip():
                while_body.append(self.get_indent() + result)
        self.indentation_level -= 1
        
        body_str = "\n".join(while_body)
        return f"while ({test}) {{\n{body_str}\n}}"
    
    def visit_Compare(self, node: ast.Compare) -> str:
        """Converte operações de comparação"""
        left = self.visit_node(node.left)
        
        # Mapeamento de operadores
        op_mapping = {
            ast.Eq: '===',
            ast.NotEq: '!==',
            ast.Lt: '<',
            ast.LtE: '<=',
            ast.Gt: '>',
            ast.GtE: '>=',
            ast.Is: '===',
            ast.IsNot: '!==',
            ast.In: 'in',
            ast.NotIn: '!in'
        }
        
        result = left
        for op, comparator in zip(node.ops, node.comparators):
            operator = op_mapping.get(type(op), str(type(op).__name__))
            right = self.visit_node(comparator)
            
            if isinstance(op, ast.In):
                result = f"{right}.includes({result})"
            elif isinstance(op, ast.NotIn):
                result = f"!{right}.includes({result})"
            else:
                result = f"{result} {operator} {right}"
        
        return result
    
    def visit_BinOp(self, node: ast.BinOp) -> str:
        """Converte operações binárias"""
        left = self.visit_node(node.left)
        right = self.visit_node(node.right)
        
        op_mapping = {
            ast.Add: '+',
            ast.Sub: '-',
            ast.Mult: '*',
            ast.Div: '/',
            ast.FloorDiv: '/',
            ast.Mod: '%',
            ast.Pow: '**'
        }
        
        operator = op_mapping.get(type(node.op), str(type(node.op).__name__))
        
        if isinstance(node.op, ast.FloorDiv):
            return f"Math.floor({left} / {right})"
        elif isinstance(node.op, ast.Pow):
            return f"Math.pow({left}, {right})"
        
        return f"{left} {operator} {right}"
    
    def visit_UnaryOp(self, node: ast.UnaryOp) -> str:
        """Converte operações unárias"""
        operand = self.visit_node(node.operand)
        
        op_mapping = {
            ast.UAdd: '+',
            ast.USub: '-',
            ast.Not: '!',
            ast.Invert: '~'
        }
        
        operator = op_mapping.get(type(node.op), str(type(node.op).__name__))
        return f"{operator}{operand}"
    
    def visit_BoolOp(self, node: ast.BoolOp) -> str:
        """Converte operações booleanas"""
        values = [self.visit_node(value) for value in node.values]
        
        if isinstance(node.op, ast.And):
            return " && ".join(values)
        elif isinstance(node.op, ast.Or):
            return " || ".join(values)
        
        return " ".join(values)
    
    def visit_List(self, node: ast.List) -> str:
        """Converte listas Python para arrays JavaScript"""
        elements = [self.visit_node(elem) for elem in node.elts]
        return f"[{', '.join(elements)}]"
    
    def visit_Dict(self, node: ast.Dict) -> str:
        """Converte dicionários Python para objetos JavaScript"""
        pairs = []
        for key, value in zip(node.keys, node.values):
            key_str = self.visit_node(key)
            value_str = self.visit_node(value)
            pairs.append(f"{key_str}: {value_str}")
        return f"{{{', '.join(pairs)}}}"
    
    def visit_Expr(self, node: ast.Expr) -> str:
        """Converte expressões standalone"""
        result = self.visit_node(node.value)
        return f"{result};"
    
    def visit_ClassDef(self, node: ast.ClassDef) -> str:
        """Converte definição de classe"""
        class_body = []
        self.indentation_level += 1
        
        for stmt in node.body:
            if isinstance(stmt, ast.FunctionDef):
                if stmt.name == '__init__':
                    # Construtor
                    args = [arg.arg for arg in stmt.args.args[1:]]  # Remove 'self'
                    args_str = ", ".join(args)
                    
                    constructor_body = []
                    self.indentation_level += 1
                    for body_stmt in stmt.body:
                        result = self.visit_node(body_stmt)
                        if result.strip():
                            constructor_body.append(self.get_indent() + result)
                    self.indentation_level -= 1
                    
                    constructor = f"{self.get_indent()}constructor({args_str}) {{\n"
                    constructor += "\n".join(constructor_body) + "\n"
                    constructor += f"{self.get_indent()}}}"
                    class_body.append(constructor)
                else:
                    # Método normal - remover 'self' dos argumentos
                    args = [arg.arg for arg in stmt.args.args[1:]]  # Remove 'self'
                    args_str = ", ".join(args)
                    
                    method_body = []
                    self.indentation_level += 1
                    for body_stmt in stmt.body:
                        result = self.visit_node(body_stmt)
                        if result.strip():
                            method_body.append(self.get_indent() + result)
                    self.indentation_level -= 1
                    
                    method = f"{self.get_indent()}{stmt.name}({args_str}) {{\n"
                    method += "\n".join(method_body) + "\n"
                    method += f"{self.get_indent()}}}"
                    class_body.append(method)
        
        self.indentation_level -= 1
        
        body_str = "\n".join(class_body)
        return f"class {node.name} {{\n{body_str}\n}}"


def transpile_python_to_js(python_code: str) -> str:
    """Função principal para transpilar código Python para JavaScript"""
    transpiler = PythonToJSTranspiler()
    return transpiler.transpile(python_code)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 3:
        print("Uso: python transpiler.py input.py output.js")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            python_code = f.read()
        
        js_code = transpile_python_to_js(python_code)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(js_code)
        
        print(f"Código transpilado com sucesso: {input_file} -> {output_file}")
    
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {input_file}")
    except Exception as e:
        print(f"Erro: {e}")