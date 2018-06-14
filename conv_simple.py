base_in = input('Insira a base inicial (8 ou 16):')
num = int(input('Insira um valor para converter:'), base=base_in)
print('Número resultante é: ', oct(num) if base_in == '16' else hex(num))
#print('Número resultante é: ', oct(num)[2:] if base_in == '16' else hex(num)[2:])