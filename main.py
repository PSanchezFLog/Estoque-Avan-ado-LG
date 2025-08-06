# Importação de bibliotecas
import os
import shutil

# Caminho da pasta de origem
pasta_origem = r'.\teste'


# Criação da função para procurar as ocorrencias de N_A
def encontrar_todas_as_ocorrências(texto, substring):
    """
    Encontra todas as ocorrências de uma substring em uma string.

    Args:
        texto: A string onde a busca será realizada.
        substring: A substring a ser procurada.

    Returns:
        Uma lista com os índices de todas as ocorrências da substring.
    """
    indices = []
    inicio = 0
    while True:
        indice = texto.find(substring, inicio)
        if indice == -1:
            break
        indices.append(indice)
        inicio = indice + 1
    return indices

# Lista vazia para colocar todas as notas
listNotas = []
numNota = ""
# Loop para procura em todos os arquivos da pasta
for nome_arquivo in os.listdir(pasta_origem):
    if nome_arquivo.lower().endswith('.txt'):
        caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)

        with open(caminho_arquivo, 'r', encoding='latin1') as file:  # latin1 para evitar erros com cedilha, acentos etc.
            for linha in file:
                if linha.startswith("313"):
                    # Pegando a chave da NFe: do caractere 254 até 298 (atenção ao índice)
                    chave = linha[254:298].strip()
                    listNotas.append(chave)

for a in listNotas:
    numNota += a
    numNota += '\n'
with open('teste.txt', 'w') as teste:                           # Joga os arquivos em um novo arquivo de texto
    teste.write(numNota)
            
print(listNotas)
