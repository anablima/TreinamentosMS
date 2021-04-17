print('\n*********** Bem Vindo(a) ao somador '
      'de kcal diário! ***********\n')

data = input('Qual a data de hoje?\n')
kcal_morn = input('\nQuantas kcal consumiu no café da manhã?\n')
kcal_aftr = input('\nQuantas kcal consumiu no almoço?\n')
kcal_even = input('\nQuantas kcal consumiu no jantar?\n')
kcal_lunc = input('\nQuantas kcal consumiu '
                  'nos lanches durante o dia?\n')

soma_kcal = str(int(kcal_morn) 
                + int(kcal_aftr) 
                + int(kcal_lunc) 
                + int(kcal_even))

print('\nVocê consumiu {soma_kcal} kcal'
      ' em {data}.'.format(soma_kcal=soma_kcal, data=data))
