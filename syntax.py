# # coding: utf-8
# import ply.lex as lex
#
# import ply.yacc as yacc
#
# precedence = (
# 	('left','LT','LEQ','GEQ','EQ','NEQ','GT'),
# 	('left','PLUS','MINUS'),
# 	('left','TIMES','DIVIDE'),
# 	('left','LPARENT','RPARENT'),
# 	)
#
# #-------------------------------------------------------------------
# #1. program → declaration-list
# def p_program(p):
# 	'''program : declarationList'''
# 	#print("program")
# 	p[0] = program(p[1],"program")
#
# #-------------------------------------------------------------------
# #2. declaration-list → declaration-list declaration | declaration
# def p_declarationList1(p):
# 	'''declarationList : declarationList declaration'''
# 	#print("declarationList 1")
# 	p[0] = declarationList1(p[1],p[2],"declarationList1")
# def p_declarationList2(p):
# 	'''declarationList : declaration'''
# 	#print("declarationList 2")
# 	p[0] = declarationList2(p[1],"declarationList2")
# #-------------------------------------------------------------------
# #3. declaration → var-declaration | fun-declaration
# def p_declaration1(p):
# 	'''declaration : varDeclaration'''
# 	#print("declaration 1")
# 	p[0] = declaration1(p[1],"declaration1")
# def p_declaration2(p):
# 	'''declaration : funDeclaration'''
# 	#print("declaration 2")
# 	p[0] = declaration2(p[1],"declaration2")
#
# #-------------------------------------------------------------------
# #4. var-declaration → type-specifier ID ; | type-specifier ID [ NUM ] ;
# def p_varDeclaration1(p):
# 	'''varDeclaration : typeSpecifier ID SEMMICOLOM'''
# 	#print("varDeclaration 1")
# 	p[0] = varDeclaration1(p[1],ID(p[2]),"varDeclaration1")
# def p_varDeclaration2(p):
# 	'''varDeclaration : typeSpecifier ID LBRACKET NUM RBRACKET SEMMICOLOM'''
# 	#print("varDeclaration 2")
# 	p[0] = varDeclaration2(p[1],ID(p[2]),NUM(p[4]),"varDeclaration2")
# #-------------------------------------------------------------------
# #5. type-specifier → int | void
# def p_typeSpecifier1(p):
# 	'''typeSpecifier : INT'''
# 	#print("typeSpecifier 1")
# 	p[0] = typeSpecifier1(p[1],"typeSpecifier1")
# def p_typeSpecifier2(p):
# 	'''typeSpecifier : VOID'''
# 	#print("typeSpecifier 2")
# 	p[0] = typeSpecifier2(p[1],"typeSpecifier2")
#
# #-------------------------------------------------------------------
# #6. fun-declaration → type-specifier ID ( params ) compound-stmt
# def p_funDeclaration(p):
# 	'''funDeclaration : typeSpecifier ID LPARENT params RPARENT compoundStmt'''
# 	#print("funDeclaration")
# 	p[0] = funDeclaration(p[1],ID(p[2]),p[4],p[6],"funDeclaration")
# #-------------------------------------------------------------------
# #7. params → param-list | void
# def p_params1(p):
# 	'''params : paramList'''
# 	#print("params 1")
# 	p[0]= params1(p[1],"params1")
# def p_params2(p):
# 	'''params : VOID'''
# 	#print("params 2")
# 	p[0] = params2(p[1],"params2")
# #-------------------------------------------------------------------
# #8. param-list → param-list , param | param
# def p_paramList1(p):
# 	'''paramList : paramList SEMMICOLOM param'''
# 	#print("paramList 1")
# 	p[0] = paramList1(p[1],p[3],"paramList1")
# def p_paramList2(p):
# 	'''paramList : param'''
# 	#print("paramList 2")
# 	p[0] = paramList2(p[1],"paramList2")
# #-------------------------------------------------------------------
# #9. param → type-specifier ID | type-specifier ID [ ]
# def p_param1(p):
# 	'''param : typeSpecifier ID'''
# 	#print("param 1")
# 	p[0] = param1(p[1],ID(p[2]),"param1")
# def p_param2(p):
# 	'''param : typeSpecifier ID LBRACKET RBRACKET'''
# 	#print("param 2")
# #-------------------------------------------------------------------
# #10. compound-stmt → { local-declarations statement-list }
# def p_compoundStmt(p):
# 	'''compoundStmt : LKEY localDeclarations statementList RKEY'''
# 	#print("compoundStmt")
# 	p[0] = compoundStmt(p[2],p[3],"compoundStmt")
# #-------------------------------------------------------------------
# #11. local-declarations → local-declarations var-declaration | empty
# def p_localDeclarations1(p):
# 	'''localDeclarations : localDeclarations varDeclaration'''
# 	#print("localDeclarations 1")
# 	p[0] = localDeclarations1(p[1],p[2],"localDeclarations1")
# def p_localDeclarations2(p):
# 	'''localDeclarations : empty'''
# 	#print("vacio")
# 	p[0] = Null()
# #-------------------------------------------------------------------
# #12. statement-list → statement-list statement |empty
# def p_statementList1(p):
# 	'''statementList : statementList statement'''
# 	#print("statementList 1")
# 	p[0] = statementList1(p[1],p[2],"statementList1")
# def p_statementList2(p):
# 	'''statementList : empty'''
# 	#print("vacio")
# 	p[0] = Null()
# #-------------------------------------------------------------------
# #13. statement → expression-stmt | compound-stmt | selection-stmt | iteration-stmt | return-stmt
# def p_statement1(p):
# 	'''statement : expressionStmt'''
# 	#print("statement 1")
# 	p[0] = statement1(p[1],"statement1")
# def p_statement2(p):
# 	'''statement : compoundStmt'''
# 	#print("statement 2")
# 	p[0] = statement2(p[1],"statement2")
# def p_statement3(p):
# 	'''statement : selectionStmt'''
# 	#print("statement 3")
# 	p[0] = statement3(p[1],"statement3")
# def p_statement4(p):
# 	'''statement : iterationStmt'''
# 	#print("statement 4")
# 	p[0] = statement4(p[1],"statement4")
# def p_statement5(p):
# 	'''statement : returnStmt'''
# 	#print("statement 5")
# 	p[0] = statement5(p[1],"statement5")
# #-------------------------------------------------------------------
# #14. expression-stmt → expression ; | ;
# def p_expressionStmt1(p):
# 	'''expressionStmt : expression SEMMICOLOM'''
# 	#print("expressionStmt 1")
# 	p[0] = expressionStmt1(p[1],"expressionStmt1")
# def p_expressionStmt2(p):
# 	'''expressionStmt : SEMMICOLOM'''
# 	print("PUNTO Y COMA")
# 	#p[0] = expressionStmt2(SEMMICOLOM(p[1]),"expressionStmt2")
# #-------------------------------------------------------------------
# #15. selection-stmt → if ( expression ) statement | if ( expression ) statement ELSE statement
# def p_selectionStmt1(p):
# 	'''selectionStmt : IF LPARENT expression RPARENT statement'''
# 	#print("p_selectionStmt 1")
# 	p[0] = selectionStmt1(p[3],p[5],"selectionStmt1")
# def p_selectionStmt2(p):
# 	'''selectionStmt : IF LPARENT expression RPARENT statement ELSE statement'''
# 	#print("p_selectionStmt 2")
# 	p[0] = selectionStmt2(p[3],p[5],p[7],"selectionStmt2")
#
# #-------------------------------------------------------------------
# #16. iteration-stmt → WHILE ( expression ) statement
# def p_whileStmt(p):
# 	'''whileStmt : WHILE LPARENT expression RPARENT statement'''
# 	#print("whileStmt")
# 	p[0] = iterationStmt(p[3],p[5],"whileStmt")
#
# #-------------------------------------------------------------------
# #17. return-stmt → RETURN ; | RETURN expression ;
# def p_returnStmt1(p):
# 	'''returnStmt : RETURN SEMMICOLOM'''
# 	print("RETURN PUNTO Y COMA")
# 	#p[0] = returnStmt1(RETURN(p[1]),"returnStmt1")
# def p_returnStmt2(p):
# 	'''returnStmt : RETURN expression SEMMICOLOM'''
# 	#print("returnStmt 2")
# 	p[0] = returnStmt2(p[2],"returnStmt2")
#
# #-----------------------------------------------------
# #18. expression → var ::= expression | simple-expression
# def p_expression1(p):
# 	'''expression : var ASSIGN expression'''
# 	#print("expression 1")
# 	p[0] = expression1(p[1],ASSIGN(p[2]),p[3],"expression1")
# def p_expression2(p):
# 	'''expression : simpleExpression'''
# 	#print("expression 2")
# 	p[0] = expression2(p[1],"expression2")
#
# #-------------------------------------------------------------------
# #19. var → ID | ID [ expression ]
# def p_var1(p):
# 	'''var : ID'''
# 	#print("var 1")
# 	p[0] = var1(ID(p[1]),"var1")
# def p_var2(p):
# 	'''var : ID LBRACKET expression RBRACKET'''
# 	#print("var 2")
# 	p[0] = var2(ID(p[1]),p[3],"var2")
#
# #-------------------------------------------------------------------
# #20. simple-expression -> additive-expression relop additive-expression | additive-expression
# def p_simpleExpression1(p):
#     '''simpleExpression : additiveExpression relop additiveExpression '''
#     #print("simpleExpression 1")
#     p[0] = simpleExpression1(p[1],p[2],p[3],"simpleExpression1")
# def p_simpleExpression2(p):
#     '''simpleExpression : additiveExpression'''
#     #print("simpleExpression2")
#     p[0] = simpleExpression2(p[1],"simpleExpression")
#
# #-------------------------------------------------------------------
# #21. relop -> LEQ | LT | GT | GEQ | EQ | NEQ
# def p_relop1(p):
#     '''relop : LEQ'''
#     #print("relop 1")
#     p[0] = relop1(LEQ(p[1]),"relop1")
# def p_relpo2(p):
#     '''relop : LT'''
#     #print("relop 2")
#     p[0] = relop2(LT(p[1]),"relop2")
# def p_relop3(p):
#     '''relop : GT'''
#     #print("relop 3")
#     p[0] = relop3(GT(p[1]),"relop3")
# def p_relop4(p):
#     '''relop : GEQ'''
#     #print("relop 4")
#     p[0] = relop4(GEQ(p[1]),"relop4")
# def p_relop5(p):
#     '''relop : EQ'''
#     #print("relop 5")
#     p[0] = relop5(EQ(p[1]),"relop5")
# def p_relop6(p):
#     '''relop : NEQ'''
#     #print("relop 6")
#     p[0] = relop6(NEQ(p[1]),"relop6")
#
# #---------------------------------------------------------------------
# #22. additive-expression -> additive-expression addop term | term
# def p_additiveExpression1(p):
#     '''additiveExpression : additiveExpression addop term'''
#     #print("additiveExpression 1")
#     p[0] = additiveExpression(p[1],p[2],p[3],"additiveExpression1")
# def p_additiveExpression2(p):
#     '''additiveExpression : term'''
#     #print("additiveExpression 2")
#     p[0] = additiveExpression2(p[1],"additiveExpression2")
#
# #----------------------------------------------------------------------
# #23. addop -> + | -
# def p_addop1(p):
#     '''addop : PLUS'''
#     #print("addop 1")
#     p[0] = addop1(PLUS(p[1]),"addop1")
# def p_addop2(p):
#     '''addop : MINUS'''
#     #print("addop 2")
#     p[0] = addop2(MINUS(p[1]),"addop2")
#
# #-------------------------------------------------------------------------
# #24. term -> term mulop factor | factor
# def p_term1(p):
#     '''term : term mulop factor'''
#     #print("term 1")
#     p[0] = term1(p[1],p[2],p[3],"term1")
# def p_term2(p):
#     '''term : factor'''
#     #print("term 2")
#     p[0] = term2(p[1],"term2")
#
# #------------------------------------------------------------------------------
# #25. mulop -> *|/
# def p_mulop1(p):
#     '''mulop : TIMES'''
#     #print("mulop 1")
#     p[0] = mulop1(TIMES(p[1]),"mulop1")
# def p_mulop2(p):
#     '''mulop : DIVIDE'''
#     #print("mulop 2)
#     p[0] = mulop2(DIVIDE(p[1]),"mulop2")
#
# #------------------------------------------------------------------------------
# #26. factor -> ( expression ) | var | call | NUM
# def p_factor1(p):
#     '''factor : LPARENT expression RPARENT'''
#     #print("factor 1")
#     p[0] = factor1(p[2],"factor1")
# def p_factor2(p):
#     '''factor : var'''
#     #print("factor 2")
#     p[0] = factor2(p[1],"factor2")
# def p_factpr3(p):
#     '''factor : call'''
#     #print("factor 3")
#     p[0] = factor3(p[1],"factor3")
# def p_factor4(p):
#     '''factor : NUM'''
#     #print("factor 4)
#     p[0] = factor4(NUM(p[1]),"factor4")
#
# #------------------------------------------------------------------------------
# #27 call -> ID ( args )
# def p_call(p):
#     '''call : ID LPARENT args RPARENT'''
#     #print("call")
#     p[0] = call(ID(p[1]))
#
# #------------------------------------------------------------------------------
# #28. args -> arg-list | empty
# def p_args1(p):
#     '''args : argList'''
# 	#print("args 1")
# 	p[0] = args1(p[1],"args1")
# def p_args2(p):
# 	'''args : empty'''
# 	#print("args 2")
# 	p[0] = Null()
#
# #---------------------------------------------------------------------------------
# #29. arg-list -> arg-list , expression | expression
# def p_argList1(p):
# 	'''argList : argList COMMA expression'''
# 	#print("args 1")
# 	p[0] = argList1(p[1],p[3],"argList1")
# def p_argsList2(p):
# 	'''argList : expression'''
# 	#print("args 2")
# 	p[0] = argsList2(p[1],"argList2")
#
# #fin sintaxis

import ply.lex as lex
from Nodes import *
from lex import *
import ply.yacc as yacc



def p_program(p):
    'program : declaration-list'
    p[0] = programNode()
    if isinstance(p[1], list):
        p[0].hijos = p[1]
    else:
        p[0].hijos = [p[1]]


def p_declaration_list_dl(p):
    'declaration-list : declaration-list declaration'
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[2], list):
        p[0].extend(p[2])
    else:
        p[0].extend([p[2]])


def p_declaration_list_d(p):
    'declaration-list : declaration'
    p[0] = p[1]


def p_declaration_var(p):
    'declaration : var-declaration'
    p[0] = p[1]


def p_declaration_num(p):
    'declaration : fun-declaration'
    p[0] = p[1]


def p_var_declaration_id(p):
    'var-declaration : type-specifier ID SEMMICOLOM'
    p[0] = varDeclarationNode(p[1], p[2])


def p_var_declaration_brack(p):
    'var-declaration : type-specifier ID LBRACKET NUM RBRACKET SEMMICOLOM'
    p[0] = varDeclarationNode(p[1], p[2], num=p[4])


def p_type_specifier_int(p):
    'type-specifier : INT'
    p[0] = p[1]


def p_type_specifier_void(p):
    'type-specifier : VOID'
    p[0] = p[1]


def p_fun_declaration(p):
    'fun-declaration : type-specifier ID LPARENT params RPARENT compound-stmt'
    p[0] = functionNode(p[1], p[2], p[4], p[6])


def p_params_pl(p):
    'params : param-list'
    p[0] = p[1]


def p_params_void(p):
    'params : VOID'
    p[0] = [paramNode(p[1])]


def p_param_list_c(p):
    'param-list : param-list COMMA param'
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[3], list):
        p[0].extend(p[3])
    else:
        p[0].extend([p[3]])


def p_param_list_param(p):
    'param-list : param'
    p[0] = p[1]


def p_param_id(p):
    'param : type-specifier ID'
    p[0] = paramNode(p[1], p[2])


def p_param_id_br(p):
    'param : type-specifier ID LBRACKET RBRACKET'
    p[0] = paramNode(p[1], p[2], is_vector=True)


def p_compound_stmt(p):
    'compound-stmt : LKEY local-declarations statement-list RKEY'
    p[0] = compoundStmtNode(p[2], p[3])


def p_local_declarations(p):
    'local-declarations : local-declarations var-declaration'
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[2], list):
        p[0].extend(p[2])
    else:
        p[0].extend([p[2]])


def p_local_declarations_e(p):
    'local-declarations : empty'
    p[0] = [p[1]]


def p_statement_list(p):
    'statement-list : statement-list statement'
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[2], list):
        p[0].extend(p[2])
    else:
        p[0].extend([p[2]])


def p_statement_list_e(p):
    'statement-list : empty'
    p[0] = [p[1]]


def p_statement_expression(p):
    'statement : expression-stmt'
    p[0] = p[1]


def p_statement_compound(p):
    'statement : compound-stmt'
    p[0] = p[1]


def p_statement_selection(p):
    'statement : selection-stmt'
    p[0] = p[1]


def p_statement_iteration(p):
    'statement : iteration-stmt'
    p[0] = p[1]


def p_statement_return(p):
    'statement : return-stmt'
    p[0] = p[1]


def p_expression_stmt(p):
    'expression-stmt : expression SEMMICOLOM'
    p[0] = p[1]


def p_expression_stmt_pc(p):
    'expression-stmt : SEMMICOLOM'
    p[0] = p[1]


def p_selection_stmt_if(p):
    'selection-stmt : IF LPARENT expression RPARENT statement'
    p[0] = selection_stmtNode(p[3], p[5])


def p_selection_stmt_else(p):
    'selection-stmt : IF LPARENT expression RPARENT statement ELSE statement'
    p[0] = selection_stmtNode(p[3], p[5], is_else=True, else_statement=p[7])


def p_iteration_stmt(p):
    'iteration-stmt : WHILE LPARENT expression RPARENT statement'
    p[0] = selection_stmtNode(p[3], p[5])


def p_return_stmt(p):
    'return-stmt : RETURN SEMMICOLOM'
    p[0] = return_stmtNode()


def p_return_expr(p):
    'return-stmt : RETURN expression SEMMICOLOM'
    p[0] = return_stmtNode(hay_expression=True, expression=p[2])


def p_expression_var(p):
    'expression : var ASSIGN expression'
    p[0] = nodoAssign(p[1], p[3])


def p_expression_simple(p):
    'expression : simple-expression'
    p[0] = p[1]


def p_var(p):
    'var : ID'
    p[0] = nodoVarVec(p[1])


def p_var_expr(p):
    'var : ID LBRACKET expression RBRACKET'
    p[0] = nodoVarVec(p[1], is_vec_access=True, expression=p[3])


def p_simple_expr_relop(p):
    'simple-expression : additive-expression relop additive-expression'
    p[0] = nodoBinOp(p[1], p[3], resultado=p[2])


def p_simple_expr_ae(p):
    'simple-expression : additive-expression'
    p[0] = p[1]


def p_relop_mi(p):
    'relop : LEQ'
    p[0] = p[1]


def p_relop_m(p):
    'relop : LT'
    p[0] = p[1]


def p_relop_mo(p):
    'relop : GT'
    p[0] = p[1]


def p_relop_moe(p):
    'relop : GEQ'
    p[0] = p[1]


def p_relop_assign(p):
    'relop : EQ'
    p[0] = p[1]


def p_relop_noteq(p):
    'relop : NEQ'
    p[0] = p[1]


def p_additive_expression_addop(p):
    'additive-expression : additive-expression addop term'
    if p[2] == '+':
        p[0] = nodoBinOp(p[1], p[3], '+')
    if p[2] == '-':
        p[0] = nodoBinOp(p[1], p[3], '-')


def p_additive_expression_term(p):
    'additive-expression : term'
    p[0] = p[1]


def p_addop_mas(p):
    'addop : PLUS'
    p[0] = p[1]


def p_addop_menos(p):
    'addop : MINUS'
    p[0] = p[1]


def p_term_mulop(p):
    'term : term mulop factor'
    if p[2] == '*':
        p[0] = nodoBinOp(p[1], p[3], '*')
    if p[2] == '-':
        p[0] = nodoBinOp(p[1], p[3], '/')


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_mulop_mul(p):
    'mulop : TIMES'
    p[0] = p[1]


def p_mulop_div(p):
    'mulop : DIVIDE'
    p[0] = p[1]


def p_factor_expr(p):
    'factor : LPARENT expression RPARENT'
    p[0] = p[2]


def p_factor_var(p):
    'factor : var'
    p[0] = p[1]


def p_factor_call(p):
    'factor : call'
    p[0] = p[1]


def p_factor_num(p):
    'factor : NUM'
    p[0] = nodoNUM(p[1])


def p_call(p):
    'call : ID LPARENT args RPARENT'
    p[0] = nodoCall(p[1], p[3])


def p_args(p):
    'args : arg-list'
    p[0] = p[1]


def p_args_e(p):
    'args : empty'
    p[0] = [p[1]]


def p_arg_list(p):
    'arg-list : arg-list COMMA expression'
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[3], list):
        p[0].extend(p[3])
    else:
        p[0].extend([p[3]])


def p_arg_list_expr(p):
    'arg-list : expression'
    p[0] = [p[1]]


def p_empty(p):
    'empty :'
    p[0] = nodoEmpty()
    pass


def p_error(p):
    print('Syntax error input!')


def main():

    parser = yacc.yacc(debug=True,start='program')

    option = input ("Please give a Option between 1 and 7: ")

    if (option == 1 or option == 2 or option == 3

        or option == 4 or option == 5 or option == 6 or option == 7

        ):

        file = open('test' + str(option.argv[1]) + '.cm', 'r')
        s = file.read()
        lexer.input(s)

        try:
            result = parser.parse(s)
            result.visit()
        except AttributeError:
            print( 'Found it a error in Syntax!')

if __name__ == '__main__':
    main()

