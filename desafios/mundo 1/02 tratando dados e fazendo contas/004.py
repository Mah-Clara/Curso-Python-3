# Desafio 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

tp = input("Digite algo: ")

print('O tipo primitivo desse valor é ', type(tp))
print('Só tem espaço? ', tp.isspace())
print('É um número? ', tp.isnumeric())
print('É um alfabeto? ', tp.isalpha())
print('É um alfanumérico? ', tp.isalnum())
print('Está em maiúsculas? ', tp.isupper())
print('Está em minúsculas? ', tp.islower())
print('Está capitalizada? ', tp.istitle())
