# Desafio 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

rs = float(input('Quanto de dinheiro você tem? '))
us = rs/5.16

print('Com R${} você pode comprar U${:.2f}.'.format(rs, us))
