#escalar o brasil que vai enfrentar o haiti usando o dicionario guardando o valor dos jogadores ( nome, numero da camisa, posição que joga) ( goleiro, meio campo, atacante, defensores) e o esquema tático, quantos atacantes, quantos meio campo, quantos defensores e não pode ter mais de 11 jogadores em campo, não pode ter mais de 1 goleiro, não pode colocar 1 goleiro no ataque e nem atacante na defesa. Vai imprimir.
#convocados = [None] * 11
#convocados[10] = {"nome": "Neymar Jr.", "camisa": 10, "posicao": "Atacante"}
#convocados.insert(10,{"nome": "Neymar Jr.", "camisa": 10, "posicao": "Atacante"})
convocados = {
    1: {"nome": "Alisson", "camisa": 1, "posicao": "Goleiro"},
    2: {"nome": "Éderson", "camisa": 2, "posicao": "Meio-campista"},
    3: {"nome": "Gabriel Magalhães", "camisa": 3, "posicao": "Defensor"},   
    4: {"nome": "Marquinhos", "camisa": 4, "posicao": "Defensor"},
    5: {"nome": "Casemiro", "camisa": 5, "posicao": "Meio-campista"},
    6: {"nome": "Alex Sandro", "camisa": 6, "posicao": "Defensor"},
    7: {"nome": "Vinicius Jr.", "camisa": 7, "posicao": "Atacante"},
    8: {"nome": "Bruno Guimarães", "camisa": 8, "posicao": "Meio-campista"},
    9: {"nome": "Matheus Cunha", "camisa": 9, "posicao": "Atacante"},
    10: {"nome": "Neymar Jr.", "camisa": 10, "posicao": "Atacante"},    
    11: {"nome": "Raphinha", "camisa": 11, "posicao": "Atacante"},
    12: {"nome": "Weverton", "camisa": 12, "posicao": "Goleiro"},
    13: {"nome": "Danilo", "camisa": 13, "posicao": "Defensor"},
    14: {"nome": "Bremer", "camisa": 14, "posicao": "Defensor"},
    15: {"nome": "Léo Pereira", "camisa": 15, "posicao": "Defensor"},
    16: {"nome": "Douglas Santos", "camisa": 16, "posicao": "Defensor"},
    17: {"nome": "Fabinho", "camisa": 17, "posicao": "Meio-campista"},
    18: {"nome": "Danilo Santos", "camisa": 18, "posicao": "Meio-campista"},
    19: {"nome": "Endrick", "camisa": 19, "posicao": "Atacante"},
    20: {"nome": "Lucas Paquetá", "camisa": 20, "posicao": "Meio-campista"},
    21: {"nome": "Luiz Henrique", "camisa": 21, "posicao": "Atacante"},
    22: {"nome": "Gabriel Martinelli", "camisa": 22, "posicao": "Atacante"},
    23: {"nome": "Ederson", "camisa": 23, "posicao": "Goleiro"},
    24: {"nome": "Ibañez", "camisa": 24, "posicao": "Defensor"},
    25: {"nome": "Igor Thiago", "camisa": 25, "posicao": "Atacante"},
    26: {"nome": "Rayan", "camisa": 26, "posicao": "Atacante"},
}
escalacao = []
print('Olá! Esse é um programa para montar a escalação do Brasil para o jogo contra o Haiti.')
print('Para selecionar um jogador, basta digitar o número da camisa. Não é possível convocar um jogador de uma posição para uma diferente da já existente na convocação. Ex: Ryan Atacante como defensor, não será possível.')
#qtd_meio_campista = input('Quantos jogadores meio-campista serão escalados ? ')
#qtd_atacantes = input('Quantos jogadores atacantes serão escalados ? ')
#qtd_defensores = input('Quantos jogadores defensores serão escalados ? ')

while len(escalacao) < 1:
  camisa = int(input('Número da camisa do jogador: ' ))
  
  escalacao.append(convocados[camisa])

for jogador in escalacao:
  print(f"Nome: {jogador['nome']} | Camisa: {jogador['camisa']} | Posicao: {jogador['posicao']}")
  print(escalacao)
