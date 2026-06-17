#escalar o brasil que vai enfrentar o haiti usando o dicionario guardando o valor dos jogadores ( nome, numero da camisa, posição que joga) ( goleiro, meio campo, atacante, defensores) e o esquema tático, quantos atacantes, quantos meio campo, quantos defensores e não pode ter mais de 11 jogadores em campo, não pode ter mais de 1 goleiro, não pode colocar 1 goleiro no ataque e nem atacante na defesa. Vai imprimir.
convocados = []
escalacao = []
print('Olá! Esse é um programa para montar a escalação do Brasil para o jogo contra o Haiti.')

while len(escalacao) < 1:
  nome = str(input('Digite o nome do jogador: ' ))
  camisa = int(input('Número da camisa do jogador: ' ))
  posicao = str(input('Qual o posição do jogador: '))
  
  escalacao.append({
    "nome": nome,
    "camisa": int(camisa),
    "posicao": posicao
  })

for jogador in escalacao:
  print(f"Nome: {jogador['nome']} | Camisa: {jogador['camisa']} | Posicao: {jogador['posicao']}")

