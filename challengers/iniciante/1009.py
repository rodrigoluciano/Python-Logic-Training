# -*- coding: utf-8 -*-

NOME = str(input())
SALARIO = float(input())
VENDAS = float(input())
COMISSAO = VENDAS*0.15
TOTAL = SALARIO+COMISSAO
print('TOTAL = R$ %0.2f'%TOTAL)