#!usr/bin/env python3
# -*- coding: utf-8 -*-

hex_digit = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

base_in = int(input('Insira a base da qual você deseja converter um número (entre 2 e 16):'))
num = int(input('Insira um valor para converter:'), base=base_in)
base_out = int(input('Insira a base para qual você deseja converter o número (entre 2 e 16):'))

list_conv = []
while num > 0:
    mod = num % base_out
    list_conv.insert(0, hex_digit[mod] if mod in hex_digit else str(mod))
    num //= base_out

print('Número resultante é: ', ''.join(list_conv))