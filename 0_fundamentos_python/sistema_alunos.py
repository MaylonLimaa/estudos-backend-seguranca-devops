# ---------------------
# Funções
# ---------------------
def cadastrar_alunos(nome):
    """
    Cadastra um aluno no sistema.

    Parâmetros:
    nome (str): Nome do aluno a ser cadastrado.

    Retorna:
    None
    """
    existe = False
    for nomes in alunos:
        if nome == nomes['Nome']:
            print('O aluno já existe!')
            existe = True
            break
    if not existe:
        notas = []
        for i in range(0, 4):
            while True:
                try:
                    nota = float(input(f'Por gentileza, digite a {i+1} ° nota de {nome}: '))
                    notas.append(nota)
                    break
                except ValueError:
                    print('Por gentileza, é necessário que seja um número')
        media = sum(notas) / len(notas) # Faz a média de acordo com as notas recebidas
        situacao = 'Aprovado' if media >= 6 else 'Reprovado' # Aprova ou reprova de acordo com a média
        alunos.append({
                'Nome': nome, # Recebe o nome do aluno
                'Notas': notas, # Recebe a lista de notas do aluno
                'Media': media, # Recebe a média do aluno
                'Situacao': situacao # Recebe o a situação do aluno
            }) # Adiciona o aluno em uma lista no próximo índice

def listar_alunos():
    """
    Função para mostrar os alunos existentes

    Retorna:
    None
    """
    contador = 0
    for aluno in alunos:
        # Loop para mostrar os alunos
        contador += 1
        print(f'O {contador}° aluno é {aluno["Nome"]}, sua média é {aluno["Media"]} e por conta disto está {aluno["Situacao"]}') # Exibe os alunos, média e a situação

def buscar_aluno(nome):
    """
    Função para procurar um aluno pelo nome

    Retorna:
    None
    """
    encontrado = False
    for aluno in alunos:
        # Loop para porcurar o aluno pelo nome
        if nome == aluno['Nome']: 
            # Condição caso o nome seja igual exibir os dados do aluno
            print(f'O aluno {aluno["Nome"]} tem a média de {aluno["Media"]} e por conta disto está {aluno["Situacao"]}')
            encontrado = True
            break
    if not encontrado:
        print('Aluno não existe')

def remover_aluno():
    """
    Função utilizada para remover um aluno através do nome

    Retorna:
    None
    """
    print('Por gentileza, informe o nome do aluno que deseja remover. ')
    nome = input()
    encontrado = False
    for i, aluno in enumerate(alunos):
        # Loop para localizar o indice do aluno a ser removido
        if nome == aluno['Nome']:
            alunos.pop(i)
            encontrado = True
            break
    if not encontrado:
        print('Aluno não existe')

def menu():
    while True:
        print('------------------------------------------------------')
        print('----------------------  Menu  ------------------------')
        print('Digite 1 para cadastrar aluno')
        print('Digite 2 para listar os alunos')
        print('Digite 3 para visualizar as informações')
        print('Digite 4 para remover um aluno')
        print('Digite 0 para encerrar o programa')
        print('------------------------------------------------------')
        while True:
            try:
                opcao = int(input())
                break
            except ValueError:
                print('O valor deve ser um número!')
    
        if opcao == 1:
            cadastrar_alunos(input('Por gentileza, digite o nome do aluno a ser cadastrado: '))
        elif opcao == 2:
            listar_alunos()
        elif opcao == 3:
            buscar_aluno(input('Por gentileza, qual aluno deseja visualizar as informações: '))
        elif opcao == 4:
            remover_aluno()
        elif opcao == 0:
            return

# ---------------------
# Variáveis Globais
# ---------------------
alunos = []
# ---------------------
# Código Principal
# ---------------------
menu()
