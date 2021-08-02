from random import randint
lista = list()
jogos = list()
print('-' * 30)
print('      LOTERIA      ')
print('-' * 30)
quant = int(input('Informe o numero de apostas: '))
tot = 1
while tot <= quant:
  cont = 0
  while True:
    num = randint(1, 60)      #Intervalo de valores de dezenas
    if num not in lista:
      lista.append(num)
      cont += 1
    if cont >= 6:     #Numero de dezenas sorteadas
      break
  lista.sort()
  jogos.append(lista[:])
  lista.clear()
  tot +=1
print('-=' * 3, f'Numeros {quant} Jogos', '-=' * 3)
for i, l in enumerate(jogos):
  print(f'jogo {i+1}: {l}')
