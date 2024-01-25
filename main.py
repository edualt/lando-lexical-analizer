import re

token_patterns = [
    ('STRING', r'\".*\"'),
    ('NUMEROS', r'\d+(\.\d*)?'), 
    ('PALABRAS RESERVADAS', r'(if|func|while|print|True|False|return|main|do|args)'),
    ('ASIGNACION', r':='),
    ('COMILLAS', r'\"'),
    ('INCREMENTO', r'(\+\+)'),
    ('DECREMENTO', r'(\-\-)'),
    ('SIGNOS', r'(\+|\-|\*|\=|\>|\<|\!|\&|\:)'),
    ('PARENTESIS', r'(\(|\))'),
    ('LLAVES', r'(\{|\})'),
    ('COMA', r'\,'),
    ('PUNTO Y COMA', r'\;'),
    ('IDENTIFICADOR', r'[a-zA-Z_][a-zA-Z0-9_]*'),
]

def lexer(code):
    tokens = []
    while code:
        for token_name, pattern in token_patterns:
            match = re.match(pattern, code)
            if match:
                value = match.group(0)
                tokens.append((token_name, value))
                code = code[len(value):].lstrip()
                break
        else:
            # agrega a la lista algo como "Simbolo no reconocido: simbolo"
            tokens.append(("Simbolo no reconocido", code[0]))
            code = code[1:].lstrip()

    return tokens

