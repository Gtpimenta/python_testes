#PARTE 1: Aquisição dos dados
# Nesse caso, se tratando de algo pequeno, apenas copiei todas as informações da página e filtrei com ajuda do Excel. Temos a seguinte lista:

tempo = ['14:31:00',
'16:46:00',
'16:00:00',
'17:46:00',
'17:43:00',
'18:56:00',
'13:59:00',
'13:46:00',
'13:27:00',
'16:06:00',
'15:12:00',
'16:52:00',
'10:56:00',
'09:16:00',
'13:25:00',
'14:22:00',
'10:45:00',
'12:35:00',
'12:21:00',
'11:51:00',
'13:44:00',
'11:39:00',
'16:07:00']

#PARTE 2: Estudo e tratamento do problema
# O objetivo desse código era apenas calcular o tempo restante de um curso (ou de futuros cursos que eu for fazer), em que não haja um contador ou algo que me indique quanto do curso já completei.
# Sabendo disso, será necessário tratar o formato que esses dados foram capturados para que seja possível desenvolver o código que atenda a essa necessidade:

tempo_tratado = []
for valor in tempo:
  correcao = valor[:-3]
  correcao = f'00:{correcao}'
  tempo_tratado.append(correcao)

print(tempo_tratado)

#PARTE 3: Mais tratamentos
# Agora que temos os dados no formato desejado, é preciso convertê-los. Existem várias abordagens aqui, eu optei por trabalhar com segundos e daí em diante converter para o formato final desejado.
# Assim sendo, temos a última etapa antes de iniciar as conversões.

lista_tempo = []
for valor in tempo:
  a = valor.split(':')
  a = [int(x) for x in a]
  lista_tempo.append(a)

print(lista_tempo)

#PARTE 4: Definição
# Em que ponto estamos do curso ou de uma playlist qualquer no youtube? É importante que o usuário forneça essa informação!

aula_atual = int(input('Em qual aula estamos?'))

#PARTE 5: Conversões
# Tendo os dados tratados e sabendo em que ponto estamos da nossa playlist, podemos converter os dados.
# A abordagem adotada foi: converter tudo para segundos, somar e, com funções nativas do Python, converter esses valores para horas, minutos e segundos.

contagem_minutos = []
contagem_segundos = []

for video in lista_tempo[aula_atual:]:
  contagem_minutos.append(video[0])
  contagem_segundos.append(video[1])

valor_total_minutos = sum(contagem_minutos)
valor_total_segundos = sum(contagem_segundos)

seg_total_soma = valor_total_segundos + (60*valor_total_minutos)

tempo_segundos = seg_total_soma%60
minutos_converter = seg_total_soma//60

tempo_minutos = minutos_converter%60
tempo_horas = minutos_converter//60

#PARTE 6: Resultado
# Agora só nos resta exibir o tempo de curso que nos aguarda!

print(f'TEMPO RESTANTE >>> {str(tempo_horas).zfill(2)}:{str(tempo_minutos).zfill(2)}:{str(tempo_segundos).zfill(2)}')

######################

# É possível melhorar esse código. Em breve transformarei em uma função e adicionarei mais funções.