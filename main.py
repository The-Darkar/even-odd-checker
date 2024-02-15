# Par ou ímpar

  #1 Dê boas-vindas ao usuário e peça-o para inserir um número de 1 a 1000.

  #2 Depois de o usuário informar o número, verifique se ele é par ou ímpar e diga ao usuário.

# Exemplo:

  # Mensagem: Em qual número você pensou?
  # Entrada: 25
  # Saída: Esse é um número ímpar! Gostaria de verificar outro?
#


try:
  num = int(input(
    'Bem vindo ao programa Par ou Ímpar!'
    '\n \n \n'
    'Insira um NÚMERO INTEIRO entre 0 e 1000: '
  ))

  if num in range(0, 1001) and num % 2 == 0:
    print(
      '\n',
      num,
      'é par'
    )   
  elif num in range (0, 1001) and num % 2 != 0:
    print(
      '\n',
      num,
      'é ímpar'
    )   
  else:
    print(
      '\n'
      'ATENÇÃO: O número precisa estar entre 0 e 1000'
  )
    
except ValueError:
  print(
    '\n'
    'ATENÇÃO: Insira um NÚMERO VÁLIDO, entre 0 e 1000'
)


