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



