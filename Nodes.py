id_n = 0
file = open('tree.dot', 'w')
file.write('digraph ast {\n\t')

class programNode():
    def __init__(self):
        self.type = 'program'
        global id_n
        self.id = id_n
        id_n += 1
        self.sons = []

    def visit(self):
        global file
        for son in self.sons:
            file.write(str(self.id) + ' -> ' + str(son.id_1) + ';\n\t')
            son.visit()
        file.write(str(self.id) + ' [label = "Program"];\n')
        file.write('}')


class varDeclarationNode():
    def __init__(self, type_specifier, id, num=None):
        self.type_specifier = type_specifier
        self.id = id
        self.num = num
        global id_n
        self.id_1 = id_n
        id_n += 1

    def visit(self):
        global file
        if self.num is not None:
            file.write(str(self.id_1) + ' [label = "VarDeclar ' + self.type_specifier + ' ' + self.id + '[' + str(
                self.num) + ']"];\n\t')
        else:
            file.write(str(self.id_1) + ' [label = "VarDeclar ' + self.type_specifier + ' ' + self.id + '"];\n\t')

class functionNode():
    def __init__(self, type_specifier, id, params, compound_stmt):
        self.type_specifier = type_specifier
        self.id = id
        self.params = params
        self.compound_stmt = compound_stmt
        global id_n
        self.id_1 = id_n
        id_n += 1

    def visit(self):
        global file
        for param in self.params:
            file.write(str(self.id_1) + ' -> ' + str(param.id_1) + ';\n\t')
            param.visit()
        file.write(str(self.id_1) + ' -> ' + str(self.compound_stmt.id) + ';\n\t')
        self.compound_stmt.visit()
        file.write(str(self.id_1) + ' [label = "Funcion ID = ' + self.id + '"];\n\t')

class paramNode():
    def __init__(self, type_specifier, id=None, is_vector=False):
        self.type_specifier = type_specifier
        self.id = id
        self.is_vector = is_vector
        global id_n
        self.id_1 = id_n
        id_n += 1

    def visit(self):
        global file
        if self.id == None:
            file.write(str(self.id_1) + ' [label = "Param: VOID"];\n\t')
        else:
            if self.is_vector:
                file.write(
                    str(self.id_1) + ' [label = "Param: ' + self.type_specifier + ' ' + self.id + '[]"];\n\t')
            else:
                file.write(str(self.id_1) + ' [label = "Param: ' + self.type_specifier + ' ' + self.id + '"];\n\t')

class compoundStmtNode():
    def __init__(self, local_declarations, statement_list):
        self.local_declarations = local_declarations
        self.statement_list = statement_list
        global id_n
        self.id = id_n
        self.id_1 = id_n
        id_n += 1

    def visit(self):
        global file
        for c in self.local_declarations:
            file.write(str(self.id) + ' -> ' + str(c.id_1) + ';\n\t')
            c.visit()

        for s in self.statement_list:
            file.write(str(self.id) + ' -> ' + str(s.id_1) + ';\n\t')
            s.visit()
        file.write(str(self.id) + ' [label = "COMPOUND STMT"];\n\t')


class selection_stmtNode():
    def __init__(self, expression, statement, is_else = False, else_statement = None):
        self.expression = expression
        self.statement = statement
        self.is_else = is_else
        self.else_statement = else_statement
        global id_n
        self.id = id_n
        self.id_1 = id_n
        id_n += 1

    def visit(self):
        global file
        if self.is_else:
            file.write(str(self.id) + ' -> ' + str(self.expression.id_1) + ';\n\t')
            file.write(str(self.id) + ' -> ' + str(self.statement.id) + ';\n\t')
            file.write(str(self.id) + ' -> ' + str(self.else_statement.id) + ';\n\t')
            self.expression.visit()
            self.statement.visit()
            self.else_statement.visit()
            file.write(str(self.id) + ' [label = "IF ELSE"];\n\t')
        else:
            file.write(str(self.id) + ' -> ' + str(self.expression.id_1) + ';\n\t')
            file.write(str(self.id) + ' -> ' + str(self.statement.id) + ';\n\t')
            self.expression.visit()
            self.statement.visit()
            file.write(str(self.id) + ' [label = "IF"];\n\t')


class iteration_stmtNode():
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement
        global id_n
        self.id = id_n
        self.id_1 = id_n
        id_n += 1

    def visit(self):
        global file
        file.write(str(self.id) + ' -> ' + str(self.expression.id_1) + ';\n\t')
        file.write(str(self.id) + ' -> ' + str(self.statement.id_1) + ';\n\t')
        self.expression.visit()
        self.statement.visit()
        file.write(str(self.id) + ' [label = "WHILE"];\n\t')


class return_stmtNode():
    def __init__(self, thereis_expression = False, expression = None):
        self.thereis_expression = thereis_expression
        self.expression = expression
        global id_n
        self.id = id_n
        self.id_1 = id_n
        id_n += 1

    def visit(self):
        global file
        if self.thereis_expression:
            file.write(str(self.id) + ' -> ' + str(self.expression.id_1) + ';\n\t')
            self.expression.visit()
        file.write(str(self.id) + ' [label = "RETURN"];\n\t')


class varNode():
    def __init__(self, id, is_vec_access=False, expression=None):
        self.id = id
        self.is_vec_access = is_vec_access
        self.expression = expression
        global id_n
        self.id_1 = id_n
        id_n += 1

    def visit(self):
        global file
        if self.is_vec_access:
            file.write(str(self.id_1) + ' -> ' + str(self.expression.id) + ';\n\t')
            if self.expression is not None:
                self.expression.visit()
        file.write(str(self.id_1) + ' [label = "VAR ID = ' + self.id + '"];\n\t')


class emptyNode():
    def __init__(self):
        self.name = 'empty'
        global id_n
        self.id_1 = id_n
        self.id = id_n
        id_n += 1

    def visit(self):
        global file
        file.write(str(self.id) + ' [label = "EMPTY"];\n\t')



class opBinaryNode():
    def __init__(self, left, right, result):
        self.left = left
        self.right = right
        self.result = result
        global id_n
        self.id_1 = id_n
        id_n += 1

    def visit(self):
        global file
        file.write(str(self.id_1) + ' -> ' + str(self.left.id_1) + ';\n\t')
        file.write(str(self.id_1) + ' -> ' + str(self.right.id_1) + ';\n\t')
        self.left.visit()
        self.right.visit()
        file.write(str(self.id_1) + ' [label = "opBinaryNode ' + str(self.result) + '"];\n\t')


class emptyNode():
    def __init__(self):
        self.name = 'empty'
        global id_n
        self.id_1 = id_n
        self.id = id_n
        id_n += 1

    def visit(self):
        global file
        file.write(str(self.id) + ' [label = "EMPTY"];\n\t')


class numNode():
    def __init__(self, num):
        self.num = num
        global id_n
        self.id_1 = id_n
        id_n += 1

    def visit(self):
        global file
        file.write(str(self.id_1) + ' [label = "NUM value = ' + str(self.num) + '"];\n\t')


class assignNode():
    def __init__(self, var, expression):
        self.var = var
        self.expression = expression
        global id_n
        self.id_1 = id_n
        self.id = id_n
        id_n += 1

    def visit(self):
        global file
        file.write(str(self.id) + ' -> ' + str(self.var.id_1) + ';\n\t')
        file.write(str(self.id) + ' -> ' + str(self.expression.id_1) + ';\n\t')
        self.expression.visit()
        self.var.visit()
        file.write(str(self.id) + ' [label = "ASSIGN"];\n\t')

class callNode():
    def __init__(self, id, args):
        self.id = id
        self.args = args
        global id_n
        self.id_1 = id_n
        id_n += 1

    def visit(self):
        global file
        for a in self.args:
            file.write(str(self.id_1) + ' -> ' + str(a.id_1) + ';\n\t')
            a.visit()
