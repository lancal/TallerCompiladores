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