# -*- coding: utf-8 -*-


LINHA1 = input() .split(" ")
CODIGO1 = int(LINHA1[0])
QUANTIDADE1 = int(LINHA1[1])
VALOR1 = float(LINHA1[2])

LINHA2 = input() .split(" ")
CODIGO2 = int(LINHA2[0])
QUANTIDADE2 = float(LINHA2[1])
VALOR2 = float(LINHA2[2])
TOTAL = (int(QUANTIDADE1))*float(VALOR1)+(int(QUANTIDADE2)*float(VALOR2))
print('VALOR A PAGAR: R$ %0.2f'%TOTAL)