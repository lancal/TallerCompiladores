import ply.lex as lex
import re
import codecs
import os

reservadas = ['ELSE','IF','INT','VOID','RETURN','WHILE']

tokens = reservadas + ['ID','NUM','PLUS','MINUS','TIMES','DIVIDE','ASSIGN','EQ','NEQ','LT','LEQ','GT','GEQ',
                       'LPARENT','RPARENT','LBRACKET','RBRACKET','LKEY','RKEY','COMMA','SEMMICOLOM']
t_ignore = '\t'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_EQ = r'=='
t_NEQ = r'<>'
t_LT = r'<'
t_LEQ = r'<='
t_GT = r'>'
t_GEQ = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LKEY = r'\{'
t_RKEY = r'\}'
t_COMMA = r','
t_SEMMICOLOM = r';'


def t_ELSE(t):
    r'(?i)else'
    # El modificador (?i) es para aceptar mayusculas y minusculas.
    return t

def t_IF(t):
    r'(?i)if'
    # El modificador (?i) es para aceptar mayusculas y minusculas.
    return t

def t_INT(t):
    r'(?i)int'
    # El modificador (?i) es para aceptar mayusculas y minusculas.
    return t

def t_VOID(t):
    r'(?i)void'
    # El modificador (?i) es para aceptar mayusculas y minusculas.
    return t

def t_RETURN(t):
    r'(?i)return'
    # El modificador (?i) es para aceptar mayusculas y minusculas.
    return t

def t_WHILE(t):
    r'(?i)while'
    # El modificador (?i) es para aceptar mayusculas y minusculas.
    return t

def t_ID(t):
    r'([a-zA-Z]){1}([_a-zA-Z0-9])+'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#contador de espacios en blanco
contBK = 0
def t_blankspace(t):
    r'\s+'
    global contBK
    contBK += 1
    pass

# SLCOMMENT es un comentario de UNA linea.
contComment = 0
def t_SLCOMMENT(t):
    r'\!\?+'
    global contComment
    contComment += 1
    pass

def t_ccomment(t):
    r'<\/(.|\n)*?\/>'
    t.lexer.lineno += t.value.count('\n')

    #return t
#t_ignore_cppcomment = r'//.*'

#numeros del 00 - 09
def t_NUM(t):
    r'[0-9]+[0-9]+'
    return t

def t_error(t):
    print("Illegal character '{0}' at line {1}".format(t.value[0], t.lineno))
    # Tratamiento de errores.
    t.lexer.skip(1)

def crearArchivo(tok):
    # C:/Users/harvstr/Documents/comp/TallerCompil/TallerCompiladores/salida
    tok1 = str(tok)
    archi = open('Salida.txt', 'a')
    archi.write(tok1+'\n')
    archi.close()
    pass

def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print(str(cont) + ". " +str(file))
        cont = cont + 1

    global valorTest
    while respuesta == False:
        numArchivo = input('\nNumero del test: ')
        valorTest = numArchivo
        for file in files:
            if file == files[int(numArchivo) - 1]:
                respuesta = True
                break

    print("Has escogido \"%s\" \n" % files[int(numArchivo) - 1])
    return files[int(numArchivo) - 1]

directorio = 'C:/Users/harvstr/Documents/comp/TallerCompil/TallerCompiladores/test/'
archivo = buscarFicheros(directorio)
test = directorio + archivo
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()
analizador = lex.lex()
analizador.input(cadena)

while True:
    tok = analizador.token()
    if not tok: break
    crearArchivo(tok)
    print(tok)

print('\r')
print("Espacios en blanco: '%s'" % contBK)
print("Comentarios de una lina: '%s'" % contComment)

