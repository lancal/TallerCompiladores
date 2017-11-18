#Scanner C-
import ply.lex as lex


reserved = ['ELSE','IF','INT','VOID','RETURN','WHILE']

tokens = reserved + ['ID','NUM','PLUS','MINUS','TIMES','DIVIDE','ASSIGN','EQ','NEQ','LT','LEQ','GT','GEQ',
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
    if t.value.upper() in reserved:
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
    print("Caracter Ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


def leX(num):

    arch = open("prueba" + str(num) + ".cm", "r")
    code = arch.read()

    lexer.input(code)

    result = open("result" + str(num) + ".txt", "w")

    while True:
        tok = lexer.token()
        if not tok:
            break
        result.write(str(tok) + "\n")
        print(tok)


    result.close()

lexer = lex.lex()

def main():

    leX(1)

if __name__ == '__main__':
    main()