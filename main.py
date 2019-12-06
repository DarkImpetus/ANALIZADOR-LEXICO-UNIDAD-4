# -*- coding: utf-8 -*-
# desarollo de aanalizardor lexico

import ply.lex as lex  # inportacion de librerias necesarias
import re

resultado_lexema = []

tokens = [
    # inicio y final
    #'TAGINICIO', 'TAG_FINAL',

    'IDENTIFICADOR', 'ENTERO', 'ASIGNAR', 'SUMA', 'RESTA', 'MULT', 'DIV', 'POTENCIA', 'MODULO',
    'MINUSMINUS', 'PLUSPLUS','PUNTOYCOMA','PUNTO','COMA','DECIMAL', 'INICIOBLOQUE',
    #'VARIABLE',
    'COMENTARIO', 'SIGNOCOMENTARIO',
    # Condiones
    'SI', 'SINO', 'EN',
    # Ciclos
    'MIENTRAS', 'PARA', 'CADENA',
    # logica
    'AND', 'OR', 'NOT', 'MENORQUE', 'MENORIGUAL', 'MAYORQUE', 'MAYORIGUAL', 'IGUAL', 'DISTINTO',
    # Symbolos
    'PARIZQ', 'PARDER', 'CORIZQ', 'CORDER', 'LLAIZQ', 'LLADER', 'RETURN', 'VOID', 'DEFINIR', 'GLOBAL', 'INTENTAR', 'EXCEPCION' 
]

# Reglas de Expresiones Regualres para token de Contexto simple
#t_PUNTO = r'[+,-]?[[0-9]*[.]]?[0-9]+'
#[+,-]?[[0-9]*[.]]?[0-9]+t__COMA = r'\,'
t_PUNTOYCOMA = r';'
t_SUMA = r'\+'
t_RESTA = r'-'
t_MINUSMINUS = r'\-\-'
#t_PUNTO = r'\.'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*{2} | \^)'
t_ASIGNAR = r'='
# Expresiones
t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'{'
t_LLADER = r'}'

