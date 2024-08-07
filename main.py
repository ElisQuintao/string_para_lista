# transformar uma string que esta com os itens juntos em uma variavel em uma lista
# nome = 'John Corno'

# nome_completo = nome.split(' ') # em split o separador obrigatoriamente é o espaço nesse caso, de acordo como aparecer na variavel nome 

# # exibi a lista
# for parte_nome in nome_completo:
#     print(parte_nome)


# print(nome_completo, end = ' ') # esse comando (end=' ') retira a quebra de linha no resultado ex ['John', 'Corno'] 
 
 # converter o nome digitado todo em minusculo com as iniciais em maiusculo
nome = input('Informe o seu nome completo: ')

# separar as palaras
nome_lista = nome.split(' ')

for i in range(len(nome_lista)):
    # capitular a primeira letra do nome
    nome_lista[i] = nome_lista[i].capitalize()

# juntar o nome em uma vaiavel
nome_completo = ' '.join(nome_lista)

print(nome_completo) # ex  elis moreira p/ Elis Moreira