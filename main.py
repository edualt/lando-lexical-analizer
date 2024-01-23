import re

token_patterns = [
    ('NUMERO', r'\d+(\.\d*)?'), 
    ('MAIN', r'main'),
    ('ARGS', r'args'), 
    ('IF', r'if'), 
    ('WHILE', r'while'), 
    ('PRINT', r'print'), 
    ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'), 
    ('OPERADORES', r'(\>\=|\<\=|\!\=|\+\+|\-\-|\+|\-|\=|\>|\<|\!)'),
    ('PARENTESIS_IZQ', r'\('), 
    ('PARENTESIS_DER', r'\)'), 
    ('LLAVE_IZQ', r'\{'), 
    ('LLAVE_DER', r'\}'), 
    ('PUNTO_Y_COMA', r';'), 
    ('COMA', r','), 
    ('FUNCION', r'func'), 
    ('DO', r'do'),  
    ('RETURN', r'return'),
    ('COMILLA', r'\"'),
    ('ASIGNACION', r'\:='),
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
            raise Exception("No se pudo analizar el código: {}".format(code))
    return tokens

