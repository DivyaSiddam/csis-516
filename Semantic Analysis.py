import re

# Symbol Table to track variables and their types
class SymbolTable:
    def __init__(self):
        self.table = {}
    
    def declare(self, var_name, var_type, value=None):
        self.table[var_name] = {'type': var_type, 'value': value}
    
    def lookup(self, var_name):
        return self.table.get(var_name, None)
    
    def __repr__(self):
        return "Symbol Table:\n" + "\n".join(f"{var}: {info['type']} = {info['value']}" for var, info in self.table.items())

# AST Nodes
class ASTNode:
    pass

class AssignmentNode(ASTNode):
    def __init__(self, var_name, expr, var_type=None):
        self.var_name = var_name
        self.expr = expr
        self.var_type = var_type

class BinaryOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class VariableNode(ASTNode):
    def __init__(self, name):
        self.name = name

class LiteralNode(ASTNode):
    def __init__(self, value, var_type):
        self.value = value
        self.var_type = var_type

class PrintNode(ASTNode):
    def __init__(self, expr):
        self.expr = expr

# Semantic Analyzer
class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()

    def analyze(self, node):
        if isinstance(node, AssignmentNode):
            expr_type = self.analyze(node.expr)
            self.symbol_table.declare(node.var_name, expr_type, node.expr.value if isinstance(node.expr, LiteralNode) else None)
        elif isinstance(node, BinaryOpNode):
            left_type = self.analyze(node.left)
            right_type = self.analyze(node.right)
            if left_type != right_type:
                raise TypeError(f"Type mismatch: {left_type} {node.op} {right_type} not allowed")
            return left_type
        elif isinstance(node, VariableNode):
            symbol = self.symbol_table.lookup(node.name)
            if not symbol:
                raise NameError(f"Error: '{node.name}' used before declaration.")
            return symbol['type']
        elif isinstance(node, LiteralNode):
            return node.var_type
        elif isinstance(node, PrintNode):
            return self.analyze(node.expr)
        return None

# Parser (Simplified for basic assignments and expressions)
def parse(tokens):
    ast_nodes = []
    i = 0
    while i < len(tokens):
        if tokens[i] == 'print':
            expr = parse_expression(tokens[i+1:])
            ast_nodes.append(PrintNode(expr))
            break
        elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', tokens[i]) and tokens[i+1] == '=':
            var_name = tokens[i]
            expr = parse_expression(tokens[i+2:])
            ast_nodes.append(AssignmentNode(var_name, expr))
            break
        i += 1
    return ast_nodes

# Helper function to parse expressions
def parse_expression(tokens):
    if len(tokens) == 1:
        if tokens[0].isdigit():
            return LiteralNode(int(tokens[0]), 'int')
        elif tokens[0].startswith('"') and tokens[0].endswith('"'):
            return LiteralNode(tokens[0], 'str')
        else:
            return VariableNode(tokens[0])
    elif len(tokens) == 3:
        return BinaryOpNode(parse_expression([tokens[0]]), tokens[1], parse_expression([tokens[2]]))
    return None

# Example Test Cases
code_snippets = [
    "x = 5", 
    "y = \"hello\"", 
    "print(x + y)" # Type mismatch error
]

tokens_list = [code.split() for code in code_snippets]
parsed_nodes = [parse(tokens) for tokens in tokens_list]

semantic_analyzer = SemanticAnalyzer()

try:
    for nodes in parsed_nodes:
        for node in nodes:
            semantic_analyzer.analyze(node)
    print(semantic_analyzer.symbol_table)
except Exception as e:
    print(e)
