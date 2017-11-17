# coding: utf-8
import ply.lex as lex

import ply.yacc as yacc

precedence = (
	('left','LT','LEQ','GEQ','EQ','NEQ','GT'),
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE'),
	('left','LPARENT','RPARENT'),
	)

#-------------------------------------------------------------------
#1. program → declaration-list
def p_program(p):
	'''program : declarationList'''
	#print("program")
	p[0] = program(p[1],"program")

#-------------------------------------------------------------------
#2. declaration-list → declaration-list declaration | declaration
def p_declarationList1(p):
	'''declarationList : declarationList declaration'''
	#print("declarationList 1")
	p[0] = declarationList1(p[1],p[2],"declarationList1")
def p_declarationList2(p):
	'''declarationList : declaration'''
	#print("declarationList 2")
	p[0] = declarationList2(p[1],"declarationList2")
#-------------------------------------------------------------------
#3. declaration → var-declaration | fun-declaration
def p_declaration1(p):
	'''declaration : varDeclaration'''
	#print("declaration 1")
	p[0] = declaration1(p[1],"declaration1")
def p_declaration2(p):
	'''declaration : funDeclaration'''
	#print("declaration 2")
	p[0] = declaration2(p[1],"declaration2")

#-------------------------------------------------------------------
#4. var-declaration → type-specifier ID ; | type-specifier ID [ NUM ] ;
def p_varDeclaration1(p):
	'''varDeclaration : typeSpecifier ID SEMMICOLOM'''
	#print("varDeclaration 1")
	p[0] = varDeclaration1(p[1],ID(p[2]),"varDeclaration1")
def p_varDeclaration2(p):
	'''varDeclaration : typeSpecifier ID LBRACKET NUM RBRACKET SEMMICOLOM'''
	#print("varDeclaration 2")
	p[0] = varDeclaration2(p[1],ID(p[2]),NUM(p[4]),"varDeclaration2")
#-------------------------------------------------------------------
#5. type-specifier → int | void
def p_typeSpecifier1(p):
	'''typeSpecifier : INT'''
	#print("typeSpecifier 1")
	p[0] = typeSpecifier1(p[1],"typeSpecifier1")
def p_typeSpecifier2(p):
	'''typeSpecifier : VOID'''
	#print("typeSpecifier 2")
	p[0] = typeSpecifier2(p[1],"typeSpecifier2")

#-------------------------------------------------------------------
#6. fun-declaration → type-specifier ID ( params ) compound-stmt
def p_funDeclaration(p):
	'''funDeclaration : typeSpecifier ID LPARENT params RPARENT compoundStmt'''
	#print("funDeclaration")
	p[0] = funDeclaration(p[1],ID(p[2]),p[4],p[6],"funDeclaration")
#-------------------------------------------------------------------
#7. params → param-list | void
def p_params1(p):
	'''params : paramList'''
	#print("params 1")
	p[0]= params1(p[1],"params1")
def p_params2(p):
	'''params : VOID'''
	#print("params 2")
	p[0] = params2(p[1],"params2")
#-------------------------------------------------------------------
#8. param-list → param-list , param | param
def p_paramList1(p):
	'''paramList : paramList SEMMICOLOM param'''
	#print("paramList 1")
	p[0] = paramList1(p[1],p[3],"paramList1")
def p_paramList2(p):
	'''paramList : param'''
	#print("paramList 2")
	p[0] = paramList2(p[1],"paramList2")
#-------------------------------------------------------------------
#9. param → type-specifier ID | type-specifier ID [ ]
def p_param1(p):
	'''param : typeSpecifier ID'''
	#print("param 1")
	p[0] = param1(p[1],ID(p[2]),"param1")
def p_param2(p):
	'''param : typeSpecifier ID LBRACKET RBRACKET'''
	#print("param 2")
#-------------------------------------------------------------------
#10. compound-stmt → { local-declarations statement-list }
def p_compoundStmt(p):
	'''compoundStmt : LKEY localDeclarations statementList RKEY'''
	#print("compoundStmt")
	p[0] = compoundStmt(p[2],p[3],"compoundStmt")
#-------------------------------------------------------------------
#11. local-declarations → local-declarations var-declaration | empty
def p_localDeclarations1(p):
	'''localDeclarations : localDeclarations varDeclaration'''
	#print("localDeclarations 1")
	p[0] = localDeclarations1(p[1],p[2],"localDeclarations1")
def p_localDeclarations2(p):
	'''localDeclarations : empty'''
	#print("vacio")
	p[0] = Null()
#-------------------------------------------------------------------
#12. statement-list → statement-list statement |empty
def p_statementList1(p):
	'''statementList : statementList statement'''
	#print("statementList 1")
	p[0] = statementList1(p[1],p[2],"statementList1")
def p_statementList2(p):
	'''statementList : empty'''
	#print("vacio")
	p[0] = Null()
#-------------------------------------------------------------------
#13. statement → expression-stmt | compound-stmt | selection-stmt | iteration-stmt | return-stmt
def p_statement1(p):
	'''statement : expressionStmt'''
	#print("statement 1")
	p[0] = statement1(p[1],"statement1")
def p_statement2(p):
	'''statement : compoundStmt'''
	#print("statement 2")
	p[0] = statement2(p[1],"statement2")
def p_statement3(p):
	'''statement : selectionStmt'''
	#print("statement 3")
	p[0] = statement3(p[1],"statement3")
def p_statement4(p):
	'''statement : iterationStmt'''
	#print("statement 4")
	p[0] = statement4(p[1],"statement4")
def p_statement5(p):
	'''statement : returnStmt'''
	#print("statement 5")
	p[0] = statement5(p[1],"statement5")
#-------------------------------------------------------------------
#14. expression-stmt → expression ; | ;
def p_expressionStmt1(p):
	'''expressionStmt : expression SEMMICOLOM'''
	#print("expressionStmt 1")
	p[0] = expressionStmt1(p[1],"expressionStmt1")
def p_expressionStmt2(p):
	'''expressionStmt : SEMMICOLOM'''
	print("PUNTO Y COMA")
	#p[0] = expressionStmt2(SEMMICOLOM(p[1]),"expressionStmt2")
#-------------------------------------------------------------------
#15. selection-stmt → if ( expression ) statement | if ( expression ) statement ELSE statement
def p_selectionStmt1(p):
	'''selectionStmt : IF LPARENT expression RPARENT statement'''
	#print("p_selectionStmt 1")
	p[0] = selectionStmt1(p[3],p[5],"selectionStmt1")
def p_selectionStmt2(p):
	'''selectionStmt : IF LPARENT expression RPARENT statement ELSE statement'''
	#print("p_selectionStmt 2")
	p[0] = selectionStmt2(p[3],p[5],p[7],"selectionStmt2")

#-------------------------------------------------------------------
#16. iteration-stmt → WHILE ( expression ) statement
def p_whileStmt(p):
	'''whileStmt : WHILE LPARENT expression RPARENT statement'''
	#print("whileStmt")
	p[0] = iterationStmt(p[3],p[5],"whileStmt")

#-------------------------------------------------------------------
#17. return-stmt → RETURN ; | RETURN expression ;
def p_returnStmt1(p):
	'''returnStmt : RETURN SEMMICOLOM'''
	print("RETURN PUNTO Y COMA")
	#p[0] = returnStmt1(RETURN(p[1]),"returnStmt1")
def p_returnStmt2(p):
	'''returnStmt : RETURN expression SEMMICOLOM'''
	#print("returnStmt 2")
	p[0] = returnStmt2(p[2],"returnStmt2")

#-----------------------------------------------------
#18. expression → var ::= expression | simple-expression
def p_expression1(p):
	'''expression : var ASSIGN expression'''
	#print("expression 1")
	p[0] = expression1(p[1],ASSIGN(p[2]),p[3],"expression1")
def p_expression2(p):
	'''expression : simpleExpression'''
	#print("expression 2")
	p[0] = expression2(p[1],"expression2")

#-------------------------------------------------------------------
#19. var → ID | ID [ expression ]
def p_var1(p):
	'''var : ID'''
	#print("var 1")
	p[0] = var1(ID(p[1]),"var1")
def p_var2(p):
	'''var : ID LBRACKET expression RBRACKET'''
	#print("var 2")
	p[0] = var2(ID(p[1]),p[3],"var2")

#-------------------------------------------------------------------
#20. simple-expression -> additive-expression relop additive-expression | additive-expression
def p_simpleExpression1(p):
    '''simpleExpression : additiveExpression relop additiveExpression '''
    #print("simpleExpression 1")
    p[0] = simpleExpression1(p[1],p[2],p[3],"simpleExpression1")
def p_simpleExpression2(p):
    '''simpleExpression : additiveExpression'''
    #print("simpleExpression2")
    p[0] = simpleExpression2(p[1],"simpleExpression")

#-------------------------------------------------------------------
#21. relop -> LEQ | LT | GT | GEQ | EQ | NEQ
def p_relop1(p):
    '''relop : LEQ'''
    #print("relop 1")
    p[0] = relop1(LEQ(p[1]),"relop1")
def p_relpo2(p):
    '''relop : LT'''
    #print("relop 2")
    p[0] = relop2(LT(p[1]),"relop2")
def p_relop3(p):
    '''relop : GT'''
    #print("relop 3")
    p[0] = relop3(GT(p[1]),"relop3")
def p_relop4(p):
    '''relop : GEQ'''
    #print("relop 4")
    p[0] = relop4(GEQ(p[1]),"relop4")
def p_relop5(p):
    '''relop : EQ'''
    #print("relop 5")
    p[0] = relop5(EQ(p[1]),"relop5")
def p_relop6(p):
    '''relop : NEQ'''
    #print("relop 6")
    p[0] = relop6(NEQ(p[1]),"relop6")

#---------------------------------------------------------------------
#22. additive-expression -> additive-expression addop term | term
def p_additiveExpression1(p):
    '''additiveExpression : additiveExpression addop term'''
    #print("additiveExpression 1")
    p[0] = additiveExpression(p[1],p[2],p[3],"additiveExpression1")
def p_additiveExpression2(p):
    '''additiveExpression : term'''
    #print("additiveExpression 2")
    p[0] = additiveExpression2(p[1],"additiveExpression2")

#----------------------------------------------------------------------
#23. addop -> + | -
def p_addop1(p):
    '''addop : PLUS'''
    #print("addop 1")
    p[0] = addop1(PLUS(p[1]),"addop1")
def p_addop2(p):
    '''addop : MINUS'''
    #print("addop 2")
    p[0] = addop2(MINUS(p[1]),"addop2")

#-------------------------------------------------------------------------
#24. term -> term mulop factor | factor
def p_term1(p):
    '''term : term mulop factor'''
    #print("term 1")
    p[0] = term1(p[1],p[2],p[3],"term1")
def p_term2(p):
    '''term : factor'''
    #print("term 2")
    p[0] = term2(p[1],"term2")

#------------------------------------------------------------------------------
#25. mulop -> *|/
def p_mulop1(p):
    '''mulop : TIMES'''
    #print("mulop 1")
    p[0] = mulop1(TIMES(p[1]),"mulop1")
def p_mulop2(p):
    '''mulop : DIVIDE'''
    #print("mulop 2)
    p[0] = mulop2(DIVIDE(p[1]),"mulop2")

#------------------------------------------------------------------------------
#26. factor -> ( expression ) | var | call | NUM
def p_factor1(p):
    '''factor : LPARENT expression RPARENT'''
    #print("factor 1")
    p[0] = factor1(p[2],"factor1")
def p_factor2(p):
    '''factor : var'''
    #print("factor 2")
    p[0] = factor2(p[1],"factor2")
def p_factpr3(p):
    '''factor : call'''
    #print("factor 3")
    p[0] = factor3(p[1],"factor3")
def p_factor4(p):
    '''factor : NUM'''
    #print("factor 4)
    p[0] = factor4(NUM(p[1]),"factor4")

#------------------------------------------------------------------------------
#27 call -> ID ( args )
def p_call(p):
    '''call : ID LPARENT args RPARENT'''
    #print("call")
    p[0] = call(ID(p[1]))

#------------------------------------------------------------------------------
#28. args -> arg-list | empty
def p_args1(p):
    '''args : argList'''
	#print("args 1")
	p[0] = args1(p[1],"args1")
def p_args2(p):
	'''args : empty'''
	#print("args 2")
	p[0] = Null()

#---------------------------------------------------------------------------------
#29. arg-list -> arg-list , expression | expression
def p_argList1(p):
	'''argList : argList COMMA expression'''
	#print("args 1")
	p[0] = argList1(p[1],p[3],"argList1")
def p_argsList2(p):
	'''argList : expression'''
	#print("args 2")
	p[0] = argsList2(p[1],"argList2")

#fin sintaxis