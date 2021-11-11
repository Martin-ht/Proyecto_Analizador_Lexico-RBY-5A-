import sys
import ply.lex as lex

tokens = (
    # RESERVERD WORDS LIST
    'ALIAS','BREAK','CASE','CLASS','DEF','DEFINED','DO','ELSE','ELSIF','ENSURE',
    'FALSE','TREU','FOR','IF','IN','MODULE','NEXT','NIL','REDO','RESCUE','RETRY',
    'RETURN','SELF','SUPER','THEN','UNDEF','UNLESS','UNTIL','WHEN','WHILE','YIELD',


    # SYMBOLS
    'PLUS','PLUSPLUS','PLUSEQUAL','MINUS','MINUSMINUS','MINUSEQUAL','TIMES',
    'TIMESTIMES','DIVIDE','LESS','LESSEQUAL','GREATER','GREATEREQUAL','EQUAL',
    'DEQUAL','DISTINT','ISEQUAL','SEMI','COMMA','LPAREN','RPAREN','LBRACKET',
    'RBRACKET','LBLOCK','RBLOCK','COLON','AMPERSANT','HASHTAG','DOT','QUOTES',
    'APOSTROPHE','DOT_DOT','PUTS','END','VARINST','NOT','BEGIN','GETS','ENSURE',

    # OTHERS
    'COMMENTS','COMMENTS_C99','VARIABLE','IDVAR','FLOAT','INT','STRING','VOID','OPEN','TIME',
)


t_ignore = " \t"

def t_VOID(t):
    r'VOID|void'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print (chr(27)+"[1;31m"+"\t ERROR: Illegal character"+chr(27)+"[0m")
    print ("\t\tLine: "+str(t.lexer.lineno)+"\t=> " + t.value[0])
    t.lexer.skip(1)


# RE RESERVERD WORDS LIST
def t_OPEN(t):
    r'File.open'
    return t

def t_ENSURE(t):
    r'ensure'
    return t

def t_BEGIN(t):
    r'begin'
    return t
def t_GETS(t):
    r'gets'
    return t

def t_AND(t):
    r'and|AND|\&\&'
    return t

def t_RESCUE(t):
    r'rescue'
    return t

def t_VARINST(t):
    r'([@]|[$])'
    return t    

def t_END(t):
    r'end'
    return t

def t_DEF(t):
    r'def'
    return t

def t_PUTS(t):
    r'puts'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_NOT(t):
    r'[|]'
    return t

def t_CLONE(t):
    r'clone'
    return t

def t_CONST(t):
    r'const'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_DECLARE(t):
    r'declare'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_DIE(t):
    r'die'
    return t

def t_DO(t):
    r'do'
    return t


def t_ELSE(t):
    r'else'
    return t

def t_ELSEIF(t):
    r'elsif'
    return t

def t_FOR(t):
    r'for'
    return t


def t_IF(t):
    r'if'
    return t

def t_NEW(t):
    r'new'
    return t

def t_OR(t):
    r'or|\|\||OR'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_TRY(t):
    r'try'
    return t

def t_WHEN(t):
    r'when'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

# RE SYMBOLS
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_EQUAL     = r'='
t_DISTINT   = r'!'
t_LESS      = r'<'
t_GREATER   = r'>'
t_SEMI      = r';'
t_COMMA     = r','
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_LBLOCK    = r'{'
t_RBLOCK    = r'}'
t_COLON     = r':'
t_AMPERSANT = r'\&'
t_HASHTAG   = r'\#'
t_DOT       = r'\.'
t_QUOTES    = r'\"'
t_APOSTROPHE = r'\''

def t_LESSEQUAL(t):
    r'<='
    return t

def t_GREATEREQUAL(t):
    r'>='
    return t

def t_DEQUAL(t):
    r'!='
    return t

def t_ISEQUAL(t):
    r'=='
    return t

def t_MINUSMINUS(t):
    r'--'
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_TIMESTIMES(t):
    r'\*\*'
    return t

def t_DOT_DOT(t):
    r'::'
    return t


# RE OTHERS


def t_COMMENTS(t):
    r'[#](.)+'
    return t

def t_IDVAR(t):
    r'\$\w+(\d\w)*'
    return t

def t_FLOAT(t):
    r'\d+(\.\d+)'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VARIABLE(t):
    r'\w+(\w\d)*'
    return t

def t_STRING(t):
    r'(("[^"]*")|(\'[^\']*\'))'
    return t


lexer = lex.lex()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        script = sys.argv[1]

        scriptfile = open(script, 'r')
        scriptdata = scriptfile.read()
        #print (scriptdata)
        lexer.input(scriptdata)

        print (chr(27)+"[0;36m"+"INICIA ANALISIS LEXICO"+chr(27)+"[0m")
        i = 1
        print ("|Num       |     Linea del texto                      Dato                     Es        |")
        while True:
            tok = lexer.token()
            if not tok:
                break
            #print (str(i)+" - "+"         Line: "+str(tok.lineno)+"           "+str(tok.type)+"               -->    "+str(tok.value))
            print ('|{:3}-      |       Line:  {:5}        --           {:10}   ---->    {:15}|'.format(str(i),str(tok.lineno),str(tok.type),str(tok.value)))
            i += 1

        print (chr(27)+"[0;36m"+"TERMINA ANALISIS LEXICO"+chr(27)+"[0m")

    else:
        print (chr(27)+"[0;31m"+"Pase el archivo de script ruby como parametro:")
        print (chr(27)+"[0;36m"+"\t$ python php_lexer.py"+chr(27)+"[1;31m"+" <filename>.br"+chr(27)+"[0m")