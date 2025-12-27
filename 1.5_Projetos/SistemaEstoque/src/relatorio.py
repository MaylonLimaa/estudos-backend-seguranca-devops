"""
Módulo para a classe relatório
"""
class Relatorio:
    """
    A classe relatório exibe dados sobre produto
    Principalmente:
    Quais produtos existem e suas informações
    Produto com o maior e menor valor total
    """

    def __init__(self, pdt):
        """
        Método construtor recebe a lista de produtos.
        
        :param pdt: lista de produtos
        """
        self.__produtos = pdt
        self.__menor_pdt = None
        self.__maior_pdt = None
        self.__nome_maior = ''
        self.__nome_menor = ''

    def exibir_relatorio(self):
        """
        O método exibe os dados do produto
        """
        self.__menor_pdt = self.__calc_menor()
        self.__maior_pdt = self.__calc_maior()

        for id_pdt, pdt in self.__produtos.items():
            print(f'ID: {id_pdt} | {pdt}')
        print(f'{self.__nome_menor} é o produto com menor valor total. Total R$ {self.__menor_pdt}')
        print(f'{self.__nome_maior} é o produto com maior valor total. Total R$ {self.__maior_pdt}')
    def __calc_menor(self):
        """
        O método calcula o menor valor
        """
        menor = None

        for pdt in self.__produtos.values():
            valortotal = pdt.quantidade * pdt.preco
            if menor is None or valortotal < menor:
                menor = valortotal
                self.__nome_menor = pdt.nome
        return menor

    def __calc_maior(self):
        """
        O método calcula o maior valor
        """
        maior = None

        for pdt in self.__produtos.values():
            valortotal = pdt.quantidade * pdt.preco
            if maior is None or valortotal > maior:
                maior = valortotal
                self.__nome_maior = pdt.nome
        return maior
