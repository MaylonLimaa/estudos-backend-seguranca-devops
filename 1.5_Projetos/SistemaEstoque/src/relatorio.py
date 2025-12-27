import produto

class Relatorio:
    """
    A classe relatório exibe dados sobre produto
    """

    def __init__(self, pdt):
        """
        Método construtor recebe a lista de produtos.
        
        :param pdt: lista de produtos
        """
        self.__produtos = pdt
        self.__menorPdt = None
        self.__maiorPdt = None
        self.__nome_maior = ''
        self.__nome_menor = ''

    def exibir_relatorio(self):
        """
        O método exibe os dados do produto
        """
        self.__menorPdt = self.__calc_menor()
        self.__maiorPdt = self.__calc_maior()

        for id, pdt in self.__produtos.items():
            print(f'ID: {id} | {pdt}')
        print(f'{self.__nome_menor} é o produto com menor valor total. Custo total {self.__menorPdt}')
        print(f'{self.__nome_maior} é o produto com maior valor total. Custo total {self.__maiorPdt}')
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

