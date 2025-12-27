"""
Neste módulo estão as funções de requisição.
"""
import produto
import relatorio

def cadastro(estoque, cont):
    """
    Função para cadastro de um produto
    
    :param estoque: Estoque de produtos
    :param cont: Contador para o ID dos produtos
    """
    while True:
        try:
            nome = input('Digite o nome do produto: ')
            preco = float(input('Digite o valor do produto: '))
            qtd = int(input('Digite a quantidade do produto: '))
            if not nome or nome.isnumeric():
                raise ValueError('Nome precisa ser letras')
            break
        except ValueError:
            print('Por gentileza, digite os valores corretamente')
        except Exception as e:
            # Em um sistema real isso deveria ser enviado a alguém e não mostrado!
            print(f'Tivemos um erro de {e}')
            print('Por favor, tente novamente mais tarde!')
            print('Vamos analisar a situação o mais breve possível!')

    try:
        pdt = produto.Produto(nome, preco, qtd)
        cont += 1
        estoque[f'pdt{cont}'] = pdt
        print('Produto cadastrado com sucesso!')
    except ValueError:
        print('Tivemos um erro! Por gentileza, necessário que os dados sejam válidos!')
        print('Verifique e tente novamente')
    except Exception as e:
        # Em um sistema real isso deveria ser enviado a alguém e não mostrado!
        print(f'Tivemos um erro de {e}')
        print('Por favor, tente novamente mais tarde!')
        print('Vamos analisar a situação o mais breve possível!')
    return cont

def adicionar(estoque, cont):
    """
    chama o método para adicionar o produto
    
    :param estoque: variavel de controle de estoque
    :param id: id do produto
    :param qtd: quantidade do produto
    """

    while True:
        try:
            qtd = int(input('Qual a quantidade que vai adicionar? '))
            id_pdt = input('Digite o ID do produto: ')
            if 'pdt' not in id_pdt:
                # Não elimina o risco de gerar produtos indevidos mas mitiga um pouco
                raise ValueError('ID inválido')
            break
        except ValueError:
            print('Precisa ser um dado válido')
        except Exception as e:
            # Em um sistema real isso deveria ser enviado a alguém e não mostrado!
            print(f'Tivemos um erro de {e}')
            print('Por favor, tente novamente mais tarde!')
            print('Vamos analisar a situação o mais breve possível!')

    if id_pdt not in estoque:
        cadastro(estoque, cont)
        return
    if qtd <= 0:
        print('A quantidade adicionada precisa ser maior que 0!')
    else:
        estoque[id_pdt].adicionar_produto(qtd)

def remover(estoque):
    """
    chama o método para remover o produto
    
    :param estoque: variavel de controle de estoque
    :param id: id do produto
    :param qtd: quantidade do produto
    """
    while True:
        try:
            qtd = int(input('Qual a quantidade que vai remover? '))
            id_pdt = input('Digite o ID do produto: ')
            break
        except ValueError:
            print('Precisa ser um número válido')
        except Exception as e:
            # Em um sistema real isso deveria ser enviado a alguém e não mostrado!
            print(f'Tivemos um erro de {e}')
            print('Por favor, tente novamente mais tarde!')
            print('Vamos analisar a situação o mais breve possível!')
    if id_pdt not in estoque:
        print('ID incorreto! Por favor verifique e tente novamente.')
        return
    if qtd <= 0:
        print('Por gentileza, é necessário que a a quantidade seja maior que 0')
    else:
        n = estoque[id_pdt].remover_produto(qtd)
        if n == 0:
            if estoque[id_pdt].quantidade == 0:
                del estoque[id_pdt]
            else:
                print('A quantidade foi removida com sucesso!')
def ver_id(estoque):
    """
    Ver os ids dos respectivos produtos
    
    :param estoque: Variável de controle estoque
    """
    for id_pdt, pdt in estoque.items():
        print(f'O id é {id_pdt} e ele é respectivo ao produto {pdt.nome}')

def exibir_relat(estoque):
    """
    Função para exibir o relatório do estoque
    
    :param estoque: Variável de controle de estoque
    """
    relat = relatorio.Relatorio(estoque)
    relat.exibir_relatorio()
