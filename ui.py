import tkinter as tk
from tkinter import scrolledtext
from main import lexer
import ctypes
import re

ctypes.windll.shcore.SetProcessDpiAwareness(True)

root = tk.Tk()
root.title("Lando Analizer")
root.geometry('800x600')

def analizar_codigo():
    codigo_fuente = editArea.get("1.0", tk.END)
    print(codigo_fuente)
    
    tokens = lexer(codigo_fuente)
    
    ventana_resultados = tk.Toplevel(root)
    ventana_resultados.title("Resultados del Análisis Léxico")

    resultado_text = scrolledtext.ScrolledText(ventana_resultados, width=80, height=40)
    resultado_text.pack()
    
    tipos_vistos = set()
    
    for token in tokens:
        tipo, valor = token
        if tipo not in tipos_vistos:
            valores = ','.join([v for t, v in tokens if t == tipo])
            resultado_text.insert(tk.END, "{}: {}\n".format(tipo, valores))
            tipos_vistos.add(tipo)
            

def changes(event=None):
    global previousText

    if editArea.get('1.0', tk.END) == previousText:
        return

    for tag in editArea.tag_names():
        editArea.tag_remove(tag, "1.0", "end")

    i = 0
    for pattern, color in repl:
        for start, end in search_re(pattern, editArea.get('1.0', tk.END)):
            editArea.tag_add(f'{i}', start, end)
            editArea.tag_config(f'{i}', foreground=color)

            i += 1

    previousText = editArea.get('1.0', tk.END)

def search_re(pattern, text, groupid=0):
    matches = []

    text = text.splitlines()
    for i, line in enumerate(text):
        for match in re.finditer(pattern, line):
            matches.append(
                (f"{i + 1}.{match.start()}", f"{i + 1}.{match.end()}")
            )

    return matches

def rgb(rgb):
    return "#%02x%02x%02x" % rgb

previousText = ''

background_color = rgb((40, 42, 54))
normal_color = rgb((248, 248, 242))
keywords_color = rgb((139, 233, 253))
function_color = rgb((255, 184, 108))
string_color = rgb((255, 121, 198))
comments_color = rgb((98, 114, 164))
args_color = rgb((80, 250, 123))
parenthesis_color = rgb((255, 121, 198))
brace_color = rgb((255, 121, 198))
symbol_color = rgb((255, 121, 198))


repl = [
    (r'\bmain\b', keywords_color),
    (r'\bargs\b', args_color),
    (r'\bif\b', keywords_color),
    (r'\bwhile\b', keywords_color),
    (r'\bprint\b', keywords_color),
    (r'\bfunc\b', function_color),
    (r'\bdo\b', keywords_color),
    (r'\".*?\"', string_color),
    (r'\'.*?\'', string_color),
    (r'\#.*?\n', comments_color),
    (r'\#.*?$', comments_color),
    (r'\(', parenthesis_color),
    (r'\)', parenthesis_color),
    (r'\{', brace_color),
    (r'\}', brace_color),
    (r'\breturn\b', keywords_color),
    (r'\>\=', symbol_color),
    (r'\<\=', symbol_color),
    (r'\!\=', symbol_color),
    (r':=', symbol_color),
    (r'\+\+', symbol_color),
    (r'\-\-', symbol_color),
    (r'\+', symbol_color),
    (r'\-', symbol_color),
    (r'\=', symbol_color),
    (r'\>', symbol_color),
    (r'\<', symbol_color),
    (r'\!', symbol_color),
]

editArea = scrolledtext.ScrolledText(
    root,
    background=background_color,
    foreground=normal_color,
    insertbackground=normal_color,
    relief=tk.FLAT,
    borderwidth=30,
    font='Consolas 15'
)

editArea.pack(
    fill=tk.BOTH,
    expand=1
)

editArea.bind('<KeyRelease>', changes)

root.bind('<Control-r>', lambda event: analizar_codigo())

root.mainloop()