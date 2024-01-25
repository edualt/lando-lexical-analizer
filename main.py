import re

token_patterns = [
    ('STRING', r'\".*\"'),
    ('NUMERO', r'\d+(\.\d*)?'), 
    ('PALABRA_RESERVADA', r'(if|func|while|print|True|False|return|main|do|args)'),
    ('IDENTIFICADOR', r'[a-zA-Z_][a-zA-Z0-9_]*'), 
    ('OPERADORES', r'(\>\=|\<\=|\!\=|\+\+|\-\-|\+|\-|\=|\>|\<|\!)'), 
    ('SIMBOLOS', r'(\{|\}|\(|\)|\,|\;|\:|\=|\")'),
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

